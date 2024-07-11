# Satellite Image Classification
![alt text](image1.png)
## Overview
This project provides a set of tools for classifying satellite images using various machine learning algorithms. The package supports supervised and unsupervised classification with Random Forest, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Logistic Regression, Maximum Likelihood, and Neural Networks. It also includes functionality for evaluating the classification model and using the trained model for inference on new images.
## Features
- Classification with various machine learning algorithms
- Customizable validation split
- Evaluation metrics (accuracy, kappa, F1 score) and confusion matrix visualization
- Model saving and loading for inference on new data
## Installation
To install the package, use pip:

```pip install satellite-image-classification```
## Usage
### Training
To perform classification on a satellite image, use the `classify` function. This function allows you to choose the algorithm and its parameters, as well as specify the validation split for training and evaluation.

Example

```python
from satellite_image_classification.classification import classify

# Paths to your input image, labeled shapefile, and output files
input_image = 'path/to/input_image.tif'
label_shapefile = 'path/to/polygons.shp'
output_image = 'path/to/output_image.tif'
model_output = 'path/to/model.pkl'
metrics_output = 'path/to/metrics.csv'
cm_output = 'path/to/confusion_matrix.png'

# Perform classification using Random Forest
classify(input_image, label_shapefile, output_image, algorithm='random_forest', val_split=0.3, model_output=model_output, metrics_output=metrics_output, cm_output=cm_output, n_estimators=100)
```

Supported Algorithms
- `random_forest`:  RandomForestClassifier (parameters: `n_estimators`)
- `svm`: SVC (parameters: `C`, `kernel`)
- `knn`: KNeighborsClassifier(parameters:`n_neighbors`)
- `maximum_likelihood`: GaussianNB

### Inference
To use a trained model for inference on a new satellite image, use the `inference` function.

Example

```python
from satellite_image_classification.classification import inference

# Paths to your input image, trained model, and output file
test_image = 'path/to/new_input_image.tif'
model_path = 'path/to/model.pkl'
output_image = 'path/to/output_image.tif'

# Perform inference using the trained model
inference(test_image, model_path, output_image)
```


# 衛星画像分類

## 概要
このプロジェクトは、さまざまな機械学習アルゴリズムを使用して衛星画像を分類するためのツールセットを提供します。ランダムフォレスト、サポートベクターマシン（SVM）、K最近傍法（KNN）、ロジスティック回帰、最尤法、ニューラルネットワークを使用した分類をサポートしています。また、分類モデルの評価や新しい画像への推論のための機能も含まれています。
## 特徴
- さまざまな機械学習アルゴリズムを使用した分類
- カスタマイズ可能な学習検証分割
- 評価指標（精度、kappa、F1スコア）および混同行列の可視化
- 新しいデータに対する推論
## インストール
パッケージをインストールするには、pipを使用します：

```pip install satellite-image-classification```

## 使用
衛星画像の分類を行うには、`classify`関数を使用します。この関数では、アルゴリズムとそのパラメータを選択し、トレーニングと評価のための検証分割を指定できます。
```python
from satellite_image_classification.classification import supervised_classification

# Paths to your input image, labeled shapefile, and output files
input_image = 'path/to/input_image.tif'
label_shapefile = 'path/to/polygons.shp'
output_image = 'path/to/output_image.tif'
model_output = 'path/to/model.pkl'
metrics_output = 'path/to/metrics.csv'
cm_output = 'path/to/confusion_matrix.png'

# Perform classification using Random Forest
classify(input_image, label_shapefile, output_image, algorithm='random_forest', val_split=0.3, model_output=model_output, metrics_output=metrics_output, cm_output=cm_output, n_estimators=100)
```

新しい衛星画像に対して推論を行うには、`inference`関数を使用します。
```python
from satellite_image_classification.classification import inference

# Paths to your input image, trained model, and output file
test_image = 'path/to/new_input_image.tif'
model_path = 'path/to/model.pkl'
output_image = 'path/to/output_image.tif'

# Perform inference using the trained model
inference(test_image, model_path, output_image)
```