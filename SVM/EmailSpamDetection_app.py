import streamlit as st
import joblib
import re
import string
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "EmailSpamDetection.joblib")
tfidf_path = os.path.join(current_dir, "tfidf_vectorizer.joblib")
model = joblib.load(model_path)
tfidf = joblib.load(tfidf_path)

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+|www.\S+", "", text)
    text = re.sub(r"<.*?>", "", text)
    text = re.sub(r"\d+", "", text)
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = re.sub(r"\s+", " ", text).strip()
    return text

st.title("📧 Email Spam Detector with SVM")
st.write("Enter your email message below to check whether it's spam or not:")

user_input = st.text_area("✉️ Email Content", "")

if st.button("🔍 Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(user_input)
        vectorized = tfidf.transform([cleaned])
        pred = model.predict(vectorized)[0]

        if pred == 1:
            st.error("🚫 This is SPAM!")
        else:
            st.success("✅ This is NOT spam.")
