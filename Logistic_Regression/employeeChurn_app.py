import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('employeeChurnModel.joblib') 

st.title("Employee Churn Predictor")

satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
average_montly_hours = st.slider("Average Monthly Hours", 80, 320, 160)
promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1])
salary = st.selectbox("Salary Level", ['low', 'medium', 'high'])

salary_map = {'low': 0, 'medium': 1, 'high': 2}
salary_encoded = salary_map[salary]

if st.button("Predict"):
    input_data = pd.DataFrame([[
        satisfaction_level,
        average_montly_hours,
        promotion_last_5years,
        salary_encoded
    ]], columns=['satisfaction_level', 'average_montly_hours', 'promotion_last_5years', 'salary'])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ This employee is likely to leave.")
    else:
        st.success("✅ This employee is likely to stay.")
