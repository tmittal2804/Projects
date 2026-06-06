# ❤️ Heart Risk Prediction System

## Overview

The Heart Risk Prediction System is a Machine Learning project that predicts the likelihood of heart disease based on a patient's medical attributes. The project performs data preprocessing, visualization, model training, evaluation, and real-time prediction using multiple machine learning algorithms.

The objective is to assist in early risk assessment by analyzing health-related parameters and generating a prediction of whether a patient is at high or low risk of heart disease.

---

## Features

### Exploratory Data Analysis

* Dataset overview and statistics
* Feature descriptions
* Correlation and trend analysis
* Scatter plot visualizations

### Multiple Machine Learning Models

The following algorithms are trained and compared:

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Support Vector Machine (SVM)

### Model Evaluation

The project evaluates model performance using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix
* ROC Curve

### Cross Validation

* 10-Fold Cross Validation
* Model generalization assessment

### Learning Curve Analysis

* Training vs Testing performance
* Overfitting and underfitting analysis

###  Feature Importance

* Identifies the most influential factors affecting heart disease prediction.

###  Real-Time Prediction System

Users can enter patient health details and receive:

* High Risk of Heart Disease
* Low Risk of Heart Disease

prediction results instantly.

---

## Dataset Features

| Feature  | Description                 |
| -------- | --------------------------- |
| age      | Age of patient              |
| sex      | Gender                      |
| cp       | Chest pain type             |
| trestbps | Resting blood pressure      |
| chol     | Cholesterol level           |
| fbs      | Fasting blood sugar         |
| restecg  | ECG results                 |
| thalach  | Maximum heart rate achieved |
| exang    | Exercise-induced angina     |
| oldpeak  | ST depression               |
| slope    | Slope of ST segment         |
| ca       | Number of major vessels     |
| thal     | Thalassemia                 |
| target   | Heart disease risk          |

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Google Colab

---

## Machine Learning Workflow

```text
Data Collection
      ↓
Data Preprocessing
      ↓
Feature Scaling
      ↓
Train-Test Split
      ↓
Model Training
      ↓
Performance Evaluation
      ↓
Heart Risk Prediction
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Heart-Risk-Prediction-System.git
cd Heart-Risk-Prediction-System
```

### Install Dependencies

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Run Project

```bash
python heart_risk_prediction.py
```

---

## Visualizations Included

* Age vs Heart Disease
* Cholesterol vs Heart Disease
* Blood Pressure vs Heart Disease
* Accuracy Comparison Graph
* Training vs Testing Accuracy Graph
* Learning Curve
* Confusion Matrix
* ROC Curve
* Feature Importance Analysis
* Risk Distribution Pie Chart

---

## Results

The project compares multiple machine learning algorithms and identifies the most effective model for heart disease prediction based on evaluation metrics.

Random Forest was selected as the primary prediction model due to its strong performance and reliability.

---

## Future Improvements

* Deploy as a web application using Flask or Streamlit
* Real-time patient dashboard
* Enhanced feature engineering
* Integration with healthcare datasets
* Explainable AI (XAI) support
* Model deployment on cloud platforms

---

## Learning Outcomes

This project helped develop skills in:

* Data Analysis
* Machine Learning
* Model Evaluation
* Data Visualization
* Predictive Analytics
* Healthcare Data Processing

---

## Dataset

This project uses the **Heart Disease Dataset** published on Kaggle by **M. F. Nazirkhan**.

**Dataset Source:**
https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset/data

### Citation

Nazirkhan, M. F. (2024). *Heart Disease Dataset*. Kaggle. Available at: https://www.kaggle.com/datasets/mfarhaannazirkhan/heart-dataset/data

The dataset contains patient health attributes such as age, cholesterol, blood pressure, heart rate, chest pain type, and other clinical indicators used for heart disease risk prediction.
