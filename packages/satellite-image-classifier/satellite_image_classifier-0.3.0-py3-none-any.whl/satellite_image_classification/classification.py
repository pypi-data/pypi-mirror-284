import rasterio 
# ラスタデータを処理するモジュール、ここでは学習用ラスタデータを
import numpy as np
from sklearn.ensemble import RandomForestClassifier
# RF分類器、効果が良い
from sklearn.svm import SVC
# SVM分類器、あまり効果がない
from sklearn.neighbors import KNeighborsClassifier
# KNN分類器、教師なし分類
from sklearn.linear_model import LogisticRegression
# ロジスティクス分類器
from sklearn.neural_network import MLPClassifier
# ニューラルネットワーク分類器、あまり効果がない
from sklearn.naive_bayes import GaussianNB
# GaussianNB、効果がよい
import fiona
# ベクターデータを処理するモジュール、ここで教師データを
from rasterio.features import rasterize
# 
from shapely.geometry import shape
#
import time
# 学習用時間を測る
from sklearn.model_selection import train_test_split
# データセットを学習、検証に分ける、デフォルト1:1
from sklearn.metrics import confusion_matrix, accuracy_score, cohen_kappa_score, f1_score
# 精度指標を出す
import matplotlib.pyplot as plt
# 混同行列を描く
import pandas as pd
# 
import joblib
#

def rasterize_polygons(shapefile, reference_image):
    # reference_imageはinput_image（学習用tifデータ）、shapefileは教師データ
    # この関数で、教師データ（shp、ベクター）をラスタ化することで、ラスタデータのinput_imageと合わせて、学習用に使う

    with rasterio.open(reference_image) as src:
        transform = src.transform
        # input_imageのアフィン変換の情報
        out_shape = (src.height, src.width)
        # input_imageの高さ、幅

    with fiona.open(shapefile, "r") as shpfile:
        shapes = [(shape(feature["geometry"]), int(feature["properties"]["class_id"])) for feature in shpfile]
        # 教師データのgeometryとclass idを記録

    rasterized_labels = rasterize(shapes, transform=transform, out_shape=out_shape, fill=0, dtype=np.uint8)
    # 教師データshapesをラスタ化する、input_imageと同じ形、

    return rasterized_labels
# ここまで教師データの前処理：ラスタ化

def plot_confusion_matrix(cm, classes, output_image):
    plt.figure(figsize=(10, 7))
    plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = 'd'
    thresh = cm.max() / 2.
    for i, j in np.ndindex(cm.shape):
        plt.text(j, i, format(cm[i, j], fmt),
                 ha="center", va="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()
    plt.savefig(output_image)

def get_classifier(algorithm, **kwargs):
    if algorithm == 'random_forest':
        return RandomForestClassifier(n_estimators=kwargs.get('n_estimators', 100), random_state=42)
    elif algorithm == 'svm':
        return SVC(C=kwargs.get('C', 1.0), kernel=kwargs.get('kernel', 'rbf'), random_state=42)
    elif algorithm == 'knn':
        return KNeighborsClassifier(n_neighbors=kwargs.get('n_neighbors', 5))
    elif algorithm == 'logistic_regression':
        return LogisticRegression(C=kwargs.get('C', 1.0), max_iter=kwargs.get('max_iter', 100), random_state=42)
    elif algorithm == 'neural_network':
        return MLPClassifier(hidden_layer_sizes=kwargs.get('hidden_layer_sizes', (100,)), max_iter=kwargs.get('max_iter', 200), random_state=42)
    elif algorithm == 'maximum_likelihood':
        return GaussianNB()
    else:
        raise ValueError(f"Unsupported algorithm: {algorithm}")

def classify(input_image, shapefile, output_image, algorithm='random_forest', val_split=0.0, model_output='model.pkl', metrics_output='metrics.csv', cm_output='confusion_matrix.png', **kwargs):
    
    start_time = time.time()

    
    with rasterio.open(input_image) as src:
        image = src.read()  
        # input_imageを読み込む
        profile = src.profile  
        # メタデータを取得する

    n_bands, height, width = image.shape
    print(f"Image dimensions: {n_bands} bands, {height} height, {width} width")

    image_2d = image.reshape((n_bands, height * width)).T
    # input_imageを2Dにreshapeする

    print("Rasterizing kyoshi data...")
    labels = rasterize_polygons(shapefile, input_image)
    labels_1d = labels.reshape(height * width)
    # 教師データをラスタ化し、1Dにreshapeする

    # ラベルのないピクセルを削除する
    mask = labels_1d > 0
    image_2d_masked = image_2d[mask]
    labels_1d_masked = labels_1d[mask]

    # 訓練セットと検証セットに分割する
    X_train, X_val, y_train, y_val = train_test_split(image_2d_masked, labels_1d_masked, test_size=val_split, random_state=42)

    # 指定されたアルゴリズムで分類器を取得する
    clf = get_classifier(algorithm, **kwargs)

    # 分類器を訓練する
    print(f"Training the {algorithm} classifier...")
    clf.fit(X_train, y_train)

    # ラベルを予測する
    print("Predicting labels...")
    predicted_labels = clf.predict(image_2d)
    classified_image = predicted_labels.reshape((height, width))

    # 分類後の画像を保存する
    profile.update(count=1, dtype=rasterio.uint8)
    with rasterio.open(output_image, 'w', **profile) as dst:
        dst.write(classified_image, 1)

    # モデルを評価する
    if val_split > 0:
        y_val_pred = clf.predict(X_val)
        cm = confusion_matrix(y_val, y_val_pred)
        accuracy = accuracy_score(y_val, y_val_pred)
        kappa = cohen_kappa_score(y_val, y_val_pred)
        f1 = f1_score(y_val, y_val_pred, average='weighted')

        metrics = {
            'accuracy': [accuracy],
            'kappa': [kappa],
            'f1_score': [f1]
        }
        df = pd.DataFrame(metrics)
        df.to_csv(metrics_output, index=False)

        plot_confusion_matrix(cm, classes=np.unique(y_train), output_image=cm_output)

    # モデルを保存する
    joblib.dump(clf, model_output)

    # 完了時間と経過時間を記録する
    end_time = time.time()
    print(f"classification completed and saved to {output_image} in {end_time - start_time:.2f} seconds")

def inference(input_image, model_path, output_image):
    # 入力画像を読み込む
    with rasterio.open(input_image) as src:
        image = src.read()  # 画像データを読み込む
        profile = src.profile  # 画像のメタデータを取得する

    # 画像の寸法を記録する
    n_bands, height, width = image.shape
    print(f"Image dimensions: {n_bands} bands, {height} height, {width} width")

    # 画像を2次元配列（ピクセル x バンド）に変換する
    image_2d = image.reshape((n_bands, height * width)).T

    # モデルをロードする
    clf = joblib.load(model_path)

    # ラベルを予測する
    print("Predicting labels...")
    predicted_labels = clf.predict(image_2d)
    classified_image = predicted_labels.reshape((height, width))

    # 分類後の画像を保存する
    profile.update(count=1, dtype=rasterio.uint8)
    with rasterio.open(output_image, 'w', **profile) as dst:
        dst.write(classified_image, 1)

    print(f"Inference completed and saved to {output_image}")
