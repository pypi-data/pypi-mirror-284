import unittest
import os
import sys
import rasterio
import numpy as np
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, cohen_kappa_score, f1_score, confusion_matrix

# Add the src directory to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from satellite_image_classification.classification import classify, inference

class TestClassification(unittest.TestCase):
    def setUp(self):
        self.input_tiff = 'test_input.tiff'
        self.polygons_shapefile = 'test_polygons.shp'
        self.output_tiff = 'test_output.tiff'
        self.model_output = 'test_model.pkl'
        self.metrics_output = 'test_metrics.csv'
        self.cm_output = 'test_confusion_matrix.png'
        self.create_test_tiff(self.input_tiff)
        self.create_test_shapefile(self.polygons_shapefile)

    def tearDown(self):
        os.remove(self.input_tiff)
        os.remove(self.polygons_shapefile)
        os.remove(self.output_tiff)
        os.remove(self.model_output)
        os.remove(self.metrics_output)
        os.remove(self.cm_output)

    def create_test_tiff(self, filename):
        with rasterio.open(filename, 'w', driver='GTiff', height=10, width=10, count=3, dtype='uint8') as dst:
            data = np.random.randint(0, 255, (3, 10, 10), dtype='uint8')
            dst.write(data)

    def create_test_shapefile(self, filename):
        import fiona
        from fiona.crs import from_epsg
        schema = {
            'geometry': 'Polygon',
            'properties': {'class_id': 'int'}
        }
        with fiona.open(filename, 'w', driver='ESRI Shapefile', crs=from_epsg(4326), schema=schema) as dst:
            polygon = {
                'geometry': {
                    'type': 'Polygon',
                    'coordinates': [[
                        (-10, -10), (10, -10), (10, 10), (-10, 10), (-10, -10)
                    ]]
                },
                'properties': {'class_id': 1}
            }
            dst.write(polygon)

    def test_classify(self):
        classify(
            self.input_tiff, 
            self.polygons_shapefile, 
            self.output_tiff, 
            algorithm='random_forest', 
            val_split=0.3, 
            model_output=self.model_output, 
            metrics_output=self.metrics_output, 
            cm_output=self.cm_output
        )

        # Check if the output TIFF exists and has the correct dimensions
        with rasterio.open(self.output_tiff) as src:
            data = src.read(1)
            self.assertEqual(data.shape, (10, 10))

        # Check if the model file exists
        self.assertTrue(os.path.exists(self.model_output))

        # Check if the metrics file exists and has the correct content
        self.assertTrue(os.path.exists(self.metrics_output))
        df = pd.read_csv(self.metrics_output)
        self.assertIn('accuracy', df.columns)
        self.assertIn('kappa', df.columns)
        self.assertIn('f1_score', df.columns)

    def test_inference(self):
        # First, classify and train the model
        classify(
            self.input_tiff, 
            self.polygons_shapefile, 
            self.output_tiff, 
            algorithm='random_forest', 
            val_split=0.3, 
            model_output=self.model_output, 
            metrics_output=self.metrics_output, 
            cm_output=self.cm_output
        )

        # Now, run inference on a new image
        new_input_tiff = 'test_new_input.tiff'
        new_output_tiff = 'test_new_output.tiff'
        self.create_test_tiff(new_input_tiff)

        inference(new_input_tiff, self.model_output, new_output_tiff)

        # Check if the output TIFF from inference exists and has the correct dimensions
        with rasterio.open(new_output_tiff) as src:
            data = src.read(1)
            self.assertEqual(data.shape, (10, 10))

        # Cleanup the new files
        os.remove(new_input_tiff)
        os.remove(new_output_tiff)

if __name__ == '__main__':
    unittest.main()
