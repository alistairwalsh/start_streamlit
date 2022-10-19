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
