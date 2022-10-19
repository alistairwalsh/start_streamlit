import pandas as pd
import streamlit as st
from atom import ATOMClassifier
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
uploadedFiles = st.file_uploader("Upload data:", type=['csv','xlsx'],accept_multiple_files=True,key="fileUploader")

st.write(uploadedFiles)
# If a dataset is uploaded, show a preview
# if datuploadedFilea is not None:
#     data = pd.read_csv(data)
#     st.text("Data preview:")
#     st.dataframe(data.head())
