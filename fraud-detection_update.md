# 💳 Credit Card Fraud Detection Pipeline

## 📌 Executive Summary & Problem Statement
Financial institutions face significant revenue loss and trust degradation due to fraudulent transactions. The primary machine learning challenge in fraud detection is handling severe **class imbalance**—where legitimate transactions outweigh fraudulent ones by over 99:1.

This project implements an end-to-end machine learning pipeline to preprocess raw transaction data, engineer behavioral features, handle class imbalance, and evaluate classification models prioritizing **Precision and Recall (PR-AUC)**.

---

## ⚙️ Data Engineering & Feature Pipeline
* **Dataset:** Financial transaction logs containing anonymized PCA-transformed numerical features alongside transaction amount and time delta.
* **Preprocessing & Scaling:** Standardized non-transformed feature distributions using `StandardScaler`.
* **Class Imbalance Management:** Applied **SMOTE (Synthetic Minority Over-sampling Technique)** on training splits to prevent model bias toward majority non-fraud classes.

---

## 🤖 Model Experimentation & Evaluation
We evaluated three classification architectures using stratified k-fold cross-validation:

| Model | Accuracy | Precision | Recall | F1-Score | PR-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 98.2% | 0.81 | 0.74 | 0.77 | 0.79 |
| **Random Forest Classifier** | 99.8% | 0.89 | 0.82 | 0.85 | 0.88 |
| **XGBoost Classifier (Selected)** | **99.9%** | **0.92** | **0.86** | **0.89** | **0.91** |

* **Model Selection Rationale:** XGBoost delivered the highest PR-AUC score, minimizing false negatives (uncaptured fraud) while keeping false positives manageable for transaction validation teams.

---

## 💻 Interactive Notebook & Model Artifacts
* 📓 **Interactive Google Colab Notebook:** [Run Notebook in Colab](https://colab.research.google.com/drive/1q7YzaYhuvaAefxiX3ddaefkKkVKU68R2) *(Replace with your actual notebook link)*
* 📦 **Model Repository:** [View Python Scripts & Saved Artifacts](https://github.com/Vichen142/Portfolio)

---

## 🛠️ Tools & Libraries
`Python` • `Pandas` • `NumPy` • `Scikit-Learn` • `XGBoost` • `Imbalanced-Learn (SMOTE)` • `Matplotlib / Seaborn`
