import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Decision_Trees\CreditRiskDetector.joblib')

st.title("Credit Risk Detector")

person_age = st.number_input('Person Age', min_value=18, max_value=100, value=30)
person_income = st.number_input('Person Income', min_value=0)
person_home_ownership = st.selectbox('Home Ownership', ['RENT', 'OWN', 'MORTGAGE', 'OTHER'])
person_emp_length = st.number_input('Employment Length (years)', min_value=0, max_value=50, value=5)
loan_intent = st.selectbox('Loan Intent', ['PERSONAL', 'EDUCATION', 'VENTURE', 'MEDICAL', 'HOME IMPROVEMENT'])
loan_grade = st.selectbox('Loan Grade', ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
loan_amnt = st.number_input('Loan Amount', min_value=0)
loan_int_rate = st.number_input('Loan Interest Rate (%)', min_value=0.0, max_value=100.0, value=10.0)
loan_percent_income = st.number_input('Loan Percent of Income (%)', min_value=0.0, max_value=100.0)
cb_person_default_on_file = st.selectbox('Person Default On File?', ['N', 'Y'])
cb_person_cred_hist_length = st.number_input('Credit History Length (months)', min_value=0)

home_ownership_map = {'RENT':0, 'OWN':1, 'MORTGAGE':2, 'OTHER':3}
loan_intent_map = {'PERSONAL':0, 'EDUCATION':1, 'VENTURE':2, 'MEDICAL':3, 'HOMEIMPROVEMENT':4}
loan_grade_map = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6}
default_map = {'N':0, 'Y':1}

input_data = pd.DataFrame({
    'person_age': [person_age],
    'person_income': [person_income],
    'person_home_ownership': [home_ownership_map[person_home_ownership]],
    'person_emp_length': [person_emp_length],
    'loan_intent': [loan_intent_map[loan_intent]],
    'loan_grade': [loan_grade_map[loan_grade]],
    'loan_amnt': [loan_amnt],
    'loan_int_rate': [loan_int_rate],
    'loan_percent_income': [loan_percent_income],
    'cb_person_default_on_file': [default_map[cb_person_default_on_file]],
    'cb_person_cred_hist_length': [cb_person_cred_hist_length]
})

if st.button('Predict Loan Status'):
    prediction = model.predict(input_data)
    result = 'Default' if prediction[0] == 1 else 'Paid Back'
    st.success(f'Predicted Loan Status: {result}')
