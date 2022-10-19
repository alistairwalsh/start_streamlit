import pandas as pd
import streamlit as st
from atom import ATOMClassifier
from utils import data_handler

# Expand the web app across the whole screen
st.set_page_config(layout="wide")

uploadedfiles = st.file_uploader("Upload data:", type=['xlsx'],accept_multiple_files=True,key="fileUploader")
