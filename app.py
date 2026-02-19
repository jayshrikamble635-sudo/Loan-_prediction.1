# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("loan_prediction_model.pkl")
encoder = joblib.load("label_encoder.pkl")

st.title("Loan Approval Prediction App")

# Inputs
gender = st.selectbox("Gender", encoder["Gender"].classes_)
married = st.selectbox("Married", encoder["Married"].classes_)
education = st.selectbox("Education", encoder["Education"].classes_)
self_employed = st.selectbox("Self Employed", encoder["Self_Employed"].classes_)
property_area = st.selectbox("Property Area", encoder["Property_Area"].classes_)

applicant_income = st.number_input("Applicant Income", min_value=0)
coapplicant_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount", min_value=0)
loan_amount_term = st.number_input("Loan Amount Term", min_value=0)
credit_history = st.selectbox("Credit History", encoder["Credit_History"].classes_)

# DataFrame
df = pd.DataFrame({
    "Gender": [gender],
    "Married": [married],
    "Education": [education],
    "Self_Employed": [se]()_
