# 🤖 Machine Learning Models 

A curated portfolio of end-to-end ML projects — data prep, EDA, model training, evaluation, persistence, and deployment.

### 🔗 Quick Links
[![GitHub](https://img.shields.io/badge/GitHub-Repo-black?logo=github)](https://github.com/tanishkahupta-19/ML-models)<br>
[![Streamlit](https://img.shields.io/badge/Live%20Demo-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://share.streamlit.io/user/tanishkagupta-19)

---

## 📂 Repository Structure
```text
├── Decision_Trees/
│   ├── CreditRiskDetector.joblib
│   ├── CreditRiskDetector_app.py
│   ├── credit_risk_dataset.csv
│   ├── model.ipynb
│   └── requirements.txt
│
├── Linear_Regression/
│   ├── HousePricePrediction.joblib
│   ├── HousePricePrediction_app.py
│   ├── USA_Housing.csv
│   ├── model.ipynb
│   └── requirements.txt
│
├── Logistic_Regression/
│   ├── employeeChurnModel.joblib
│   ├── employeeChurn_app.py
│   ├── HR_comma_sep.csv
│   ├── model.ipynb
│   └── requirements.txt
│
├── Random_Forest/
│   ├── CreditRiskDetector_RF.joblib
│   ├── CreditRiskDetector_RF_app.py
│   ├── DfvsRF.ipynb
│   ├── credit_risk_dataset.csv
│   └── requirements.txt
│
├── SVM/
│   ├── EmailSpamDetection.joblib
│   ├── EmailSpamDetection_app.py
│   ├── spam.csv
│   ├── tfidf_vectorizer.joblib
│   ├── model.ipynb
│   └── requirements.txt

```
## 📝 Projects Overview

### 1) House Price Prediction — *Linear Regression*
- **Goal:** Predict housing prices using features such as area, bedrooms, bathrooms, and year built.  
- **Dataset:** `USA_Housing.csv`  
- **Artifacts:** `HousePricePrediction.joblib`, `HousePricePrediction_app.py`, `model.ipynb`  

### 2) Credit Risk Detection — *Decision Tree / Random Forest*
- **Goal:** Predict loan default risk based on applicant demographics and financials.  
- **Dataset:** `credit_risk_dataset.csv`  
- **Artifacts (DT):** `CreditRiskDetector.joblib`, `CreditRiskDetector_app.py`  
- **Artifacts (RF):** `CreditRiskDetector_RF.joblib`, `CreditRiskDetector_RF_app.py`, `DfvsRF.ipynb`  

### 3) Employee Churn Prediction — *Logistic Regression*
- **Goal:** Predict whether an employee will leave the company.  
- **Dataset:** `HR_comma_sep.csv`  
- **Artifacts:** `employeeChurnModel.joblib`, `employeeChurn_app.py`, `model.ipynb`  

### 4) Email Spam Detection — *SVM + NLP*
- **Goal:** Classify emails as *Spam* or *Not Spam*.  
- **Techniques:** Text cleaning, TF-IDF vectorization.  
- **Dataset:** `spam.csv`  
- **Artifacts:** `EmailSpamDetection.joblib`, `tfidf_vectorizer.joblib`, `EmailSpamDetection_app.py`, `model.ipynb`  

---

## 🛠️ Tech Stack

- **Core:** Python, NumPy, Pandas, scikit-learn, Matplotlib, Seaborn  
- **NLP & Deployment:** NLTK, TF-IDF, Streamlit, joblib  

---

## ▶️ Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/tanishkahupta-19/ML-models.git
   cd ML-models
2. Navigate into a project (example: Linear Regression)
   ```bash
   cd Linear_Regression
3. Install dependencies
   ```bash
   pip install -r requirements.txt
4. Run the app
   ```bash
   streamlit run HousePricePrediction_app.py

📈 Results 

- House Price Prediction: Accuracy ≈ 91%

- Credit Risk Prediction: Decision Tree → Accuracy ≈ 91%, Recall (risky): 59%
Random Forest → Accuracy ≈ 93%, Recall (risky): 71% <br>
✅ +2.2% accuracy and better recall → Random Forest is more reliable for credit risk prediction.

- Employee Churn: Accuracy ≈ 76%

- Email Spam Detection: Accuracy ≈ 98%




