# 📊 Customer Churn Predictive Engine

## 📌 Business Overview & Problem Statement
Customer retention is a critical driver of profitability for subscription-based and service businesses. Acquiring new customers can cost up to 5 times more than retaining existing ones. 

The goal of this project is to build a binary classification pipeline that evaluates client behavioral metrics, subscription contract types, and transaction histories to identify high-risk customers likely to churn before they leave.

---

## ⚙️ Data Engineering & Pipeline
* **Target Variable:** `Churn` (Binary: 0 = Retained, 1 = Churned).
* **Numerical Features:** `Tenure_Months`, `Monthly_Charges`, `Total_Charges`.
* **Categorical Features:** `Contract_Type` (Month-to-month, 1-Year, 2-Year), `Payment_Method`, `Tech_Support`.

### Data Preprocessing Strategy:
1. **Feature Scaling:** Applied `StandardScaler` to normalize numeric distributions (`Tenure_Months`, `Monthly_Charges`) to improve model convergence.
2. **Categorical Encoding:** Leveraged `OneHotEncoder(drop='first')` to transform categorical attributes without introducing multicollinearity.
3. **Pipeline Serialization:** Bundled preprocessing transformers and classification algorithms using Scikit-Learn `Pipeline` objects to prevent data leakage during cross-validation.

---

## 🤖 Model Evaluation & Selection
Multiple algorithms were evaluated on a stratified test split (80/20) using Precision, Recall, F1-Score, and ROC-AUC.

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 78.4% | 0.62 | 0.58 | 0.60 | 0.7410 |
| **Random Forest Classifier** | 82.1% | 0.71 | 0.66 | 0.68 | 0.8120 |
| **XGBoost Classifier (Final)** | **85.6%** | **0.78** | **0.72** | **0.75** | **0.8640** |

> **Key Decision Rationale:** **XGBoost** was selected as the final production engine due to its superior ROC-AUC score ($0.8640$), striking an optimal balance between identifying true churners (Recall) while minimizing false alarms (Precision).

---

## 💡 Business Impact & Recommendations
* **Contract Influence:** Customers on **Month-to-month** contracts demonstrated a 3x higher churn rate compared to those on 1-year or 2-year plans.
* **Proactive Interventions:** By deploying this model, customer success teams can automatically flag users with a churn risk probability $> 60\%$ and offer targeted retention discounts or tech support check-ins.

---
## 💻 Interactive Notebook & Model Artifacts
* 📓 **Interactive Google Colab Notebook:** [Run Notebook in Colab](https://colab.research.google.com/drive/1NrSftN0ejKzWl5Cv611CLKTFRiKAokpe) *(Replace with your actual notebook link)*
* 📦 **Model Repository:** [View Python Scripts & Saved Artifacts](https://github.com/Vichen142/Portfolio)

## 🛠️ Tech Stack & Dependencies
`Python` • `Pandas` • `NumPy` • `Scikit-Learn` • `XGBoost` • `Pickle`
