import streamlit as st
import pandas as pd
import joblib
import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

model = joblib.load("HousePricePrediction_joblib")
model_features = ['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                  'Avg. Area Number of Bedrooms', 'Area Population']

st.title("House Price Prediction")
st.write("Enter the following features:")

avg_income = st.number_input('Avg. Area Income', value=50000.0)
avg_house_age = st.number_input('Avg. Area House Age', value=5.0)
avg_rooms = st.number_input('Avg. Area Number of Rooms', value=7.0)
avg_bedrooms = st.number_input('Avg. Area Number of Bedrooms', value=4.0)
area_population = st.number_input('Area Population', value=30000)

input_df = pd.DataFrame({
    'Avg. Area Income': [avg_income],
    'Avg. Area House Age': [avg_house_age],
    'Avg. Area Number of Rooms': [avg_rooms],
    'Avg. Area Number of Bedrooms': [avg_bedrooms],
    'Area Population': [area_population]
})

if st.button('Predict House Price'):
    prediction = model.predict(input_df)
    st.success(f'Predicted House Price: ${prediction[0]:,.2f}')
