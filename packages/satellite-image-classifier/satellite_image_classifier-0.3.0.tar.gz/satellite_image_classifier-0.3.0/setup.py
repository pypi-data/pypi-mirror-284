from setuptools import setup, find_packages
import os

# Read the contents of the README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='satellite_image_classifier',
    version='0.3.0',
    description='A package for satellite image classification',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/satellite_image_classifier',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'rasterio',
        'numpy',
        'scikit-learn',
        'fiona',
        'shapely',
        'matplotlib',
        'pandas',
        'joblib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
