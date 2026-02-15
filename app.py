import streamlit as st
import pandas as pd
import joblib
import os

st.title("Loan Prediction App")

if not os.path.exists("label_encoder.pkl"):
    st.error("label_encoder.pkl not found")
    st.stop()

if not os.path.exists("Loan_prediction_Model.pkl"):
    st.error("Loan_prediction_Model.pkl not found")
    st.stop()

encoder = joblib.load("label_encoder.pkl")
model = joblib.load("Loan_prediction_Model.pkl")

gender = st.selectbox("Gender", encoder["Gender"].classes_)
education = st.selectbox("Education", encoder["Education"].classes_)
income = st.number_input("Applicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
credit_history = st.selectbox("Credit History", [0, 1])

df = pd.DataFrame({
    "Gender": [gender],
    "Education": [education],
    "ApplicantIncome": [income],
    "LoanAmount": [loan_amount],
    "Credit_History": [credit_history]
})

df["Gender"] = encoder["Gender"].transform(df["Gender"])
df["Education"] = encoder["Education"].transform(df["Education"])

if st.button("Predict"):
    result = model.predict(df)
    if result[0] == 1:
        st.write("Loan Approved")
    else:
        st.write("Loan Rejected")
