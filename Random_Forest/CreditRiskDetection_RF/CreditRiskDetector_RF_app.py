import streamlit as st
import pandas as pd
import joblib

model_path = 'Random_Forest/CreditRiskDetection_RF/CreditRiskDetector_RF.joblib'
rf_model = joblib.load(model_path)

home_ownership_map = {'RENT': 0, 'OWN': 1, 'MORTGAGE': 2, 'OTHER': 3}
loan_intent_map = {'PERSONAL': 0, 'EDUCATION': 1, 'MEDICAL': 2, 'VENTURE': 3, 'HOMEIMPROVEMENT': 4}
loan_grade_map = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6}
cb_default_map = {'N': 0, 'Y': 1}

st.title("Credit Risk Prediction - Random Forest")

person_age = st.number_input("Person Age", min_value=18, max_value=100, value=30)
person_income = st.number_input("Person Income", min_value=0)
person_home_ownership = st.selectbox("Person Home Ownership", options=list(home_ownership_map.keys()))
person_emp_length = st.number_input("Person Employment Length (years)", min_value=0, max_value=50, value=5)
loan_intent = st.selectbox("Loan Intent", options=list(loan_intent_map.keys()))
loan_grade = st.selectbox("Loan Grade", options=list(loan_grade_map.keys()))
loan_amnt = st.number_input("Loan Amount", min_value=0)
loan_int_rate = st.number_input("Loan Interest Rate (%)", min_value=0.0, max_value=100.0, format="%.2f")
loan_percent_income = st.number_input("Loan Percent of Income", min_value=0.0, max_value=100.0, format="%.2f")
cb_person_default_on_file = st.selectbox("Person Default on File", options=list(cb_default_map.keys()))
cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=0)

input_dict = {
    'person_age': person_age,
    'person_income': person_income,
    'person_home_ownership': home_ownership_map[person_home_ownership],
    'person_emp_length': person_emp_length,
    'loan_intent': loan_intent_map[loan_intent],
    'loan_grade': loan_grade_map[loan_grade],
    'loan_amnt': loan_amnt,
    'loan_int_rate': loan_int_rate,
    'loan_percent_income': loan_percent_income,
    'cb_person_default_on_file': cb_default_map[cb_person_default_on_file],
    'cb_person_cred_hist_length': cb_person_cred_hist_length
}

input_df = pd.DataFrame([input_dict])

if st.button("Predict Credit Risk"):
    prediction = rf_model.predict(input_df)[0]
    prediction_proba = rf_model.predict_proba(input_df)[0]
    st.write(f"### Predicted Loan Status: **{prediction}**")
    st.write(f"Prediction Probability: {prediction_proba}")
    if prediction == 1:
        st.error("High Risk of Default")
    else:
        st.success("Low Risk of Default")
        