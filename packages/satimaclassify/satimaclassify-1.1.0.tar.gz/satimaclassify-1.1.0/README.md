# Satellite Image Classification
![alt text](image1.png)
## Overview
This project provides a comprehensive set of tools for classifying satellite images using various machine learning algorithms. The package supports both supervised and unsupervised classification methods, including Random Forest, Support Vector Machine (SVM), K-Nearest Neighbors (KNN), Logistic Regression, Maximum Likelihood, and Neural Networks. Additionally, it offers functionality for evaluating classification models and applying trained models to new datasets for inference.
## Features
- Classification Algorithms: Supports multiple machine learning algorithms for versatile classification tasks.
- Customizable Validation Split: Allows specifying a validation split for training and evaluation.
- Evaluation Metrics: Calculates accuracy, kappa, F1 score, and provides confusion matrix visualization.
- Model Persistence: Enables saving and loading models for future use.
## Installation
To install the package, use the following pip command:

```pip install satimaclassify```
## Usage
### Training
The `classify` function is used for training classification models on satellite images. This function supports a range of algorithms and parameters, and allows specifying a validation split for model evaluation.

Example:

```python
from satimaclassify.classification import classify

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
The `inference` function is used to apply a trained model to new satellite images for classification.

Example:

```python
from satimaclassify.classification import inference

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
- さまざまな機械学習アルゴリズムをサポートし、多用途の分類タスクに対応
- トレーニングと評価のために検証分割を指定可能
- 精度、カッパ係数、F1スコアを計算し、混同行列の視覚化を提供
- モデルの保存と読み込みを可能にし、将来の推論に対応
## インストール
パッケージをインストールするには、次のpipコマンドを使用します。

```pip install satimaclassify```

## 使用
衛星画像の分類を行うには、`classify`関数を使用します。この関数では、アルゴリズムとそのパラメータを選択し、トレーニングと評価のための検証分割を指定できます。
```python
from satimaclassify.classification import supervised_classification

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
from satimaclassify.classification import inference

# Paths to your input image, trained model, and output file
test_image = 'path/to/new_input_image.tif'
model_path = 'path/to/model.pkl'
output_image = 'path/to/output_image.tif'

# Perform inference using the trained model
inference(test_image, model_path, output_image)
```