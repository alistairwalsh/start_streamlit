import pandas as pd
import streamlit as st
from atom import ATOMClassifier
from utils import data_handler

# Expand the web app across the whole screen
st.set_page_config(layout="wide")

st.sidebar.title("Pipeline")

# Data cleaning options
st.sidebar.subheader("Data cleaning")
scale = st.sidebar.checkbox("Scale", False, "scale")
encode = st.sidebar.checkbox("Encode", False, "encode")
impute = st.sidebar.checkbox("Impute", False, "impute")

# Model options
st.sidebar.subheader("Models")
models = {
    "gnb": st.sidebar.checkbox("Gaussian Naive Bayes", True, "gnb"),
    "rf": st.sidebar.checkbox("Random Forest", True, "rf"),
    "et": st.sidebar.checkbox("Extra-Trees", False, "et"),
    "xgb": st.sidebar.checkbox("XGBoost", False, "xgb"),
    "lgb": st.sidebar.checkbox("LightGBM", False, "lgb"),
}

st.header("Data")

uploadedfiles = st.file_uploader("Upload data:", type=['xlsx'],accept_multiple_files=True,key="fileUploader")

#If a dataset is uploaded, show a preview
if uploadedfiles is not None:
    for f in uploadedfiles:
        data = pd.read_excel(f)
        st.write("Data preview:", f.name)
        st.dataframe(data.head())

if uploadedfiles is not None:
    for f in uploadedfiles:
        data = pd.read_excel(f)
        survey_col_list = data_handler.slicer(data)
        for c in survey_col_list:
            st.dataframe(data[c].dropna().head())
