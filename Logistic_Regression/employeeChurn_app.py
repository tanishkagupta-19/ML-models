import streamlit as st
import pandas as pd
import joblib

model = joblib.load('Logistic_Regression\employeeChurnModel.joblib')
st.title("Employee Churn Predictor")

satisfaction_level = st.slider("Satisfaction Level", 0.0, 1.0, 0.5)
average_montly_hours = st.slider("Average Monthly Hours", 80, 320, 160)
promotion_last_5years = st.selectbox("Promotion in Last 5 Years", [0, 1])
salary = st.selectbox("Salary Level", ['low', 'medium', 'high'])

if st.button("Predict"):
    input_data = pd.DataFrame([{
        'satisfaction_level': satisfaction_level,
        'average_montly_hours': average_montly_hours,
        'promotion_last_5years': promotion_last_5years,
        'salary': salary
    }])

    input_data = pd.get_dummies(input_data)

    for col in ['salary_low', 'salary_medium', 'salary_high']:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data.reindex(columns=model_columns, fill_value=0)

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("⚠️ This employee is likely to leave.")
    else:
        st.success("✅ This employee is likely to stay.")
