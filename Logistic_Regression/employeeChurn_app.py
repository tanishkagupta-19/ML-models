import streamlit as st
import pandas as pd
import joblib

model = joblib.load('D:/ML-models/Logistic_Regression/employeeChurnModel.joblib')

st.title("Employee Churn Predictor")

satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
average_montly_hours = st.slider("Average Monthly Hours", 80, 320, 160)
promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1])
salary = st.selectbox("Salary Level", ['low', 'medium', 'high'])

input_dict = {
    'satisfaction_level': satisfaction_level,
    'average_montly_hours': average_montly_hours,
    'promotion_last_5years': promotion_last_5years,
    'salary': salary
}

input_df = pd.DataFrame([input_dict])

input_df = pd.get_dummies(input_df, columns=['salary'])

expected_columns = [
    'satisfaction_level',
    'average_montly_hours',
    'promotion_last_5years',
    'salary_high',
    'salary_low',
    'salary_medium'
]
for col in expected_columns:
    if col not in input_df.columns:
        input_df[col] = 0

input_df = input_df[expected_columns]

if st.button("Predict"):
    prediction = model.predict(input_df)[0]
    if prediction == 1:
        st.error("⚠️ This employee is likely to leave.")
    else:
        st.success("✅ This employee is likely to stay.")
