import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

file = st.file_uploader("CSV upload karo", type=["csv"])

if file is not None:
    df = pd.read_csv(file)

    le = LabelEncoder()
    df["Gender"] = le.fit_transform(df["Gender"])

    st.dataframe(df)
