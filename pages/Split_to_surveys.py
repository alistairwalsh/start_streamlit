from distutils.command.upload import upload
import pandas as pd
import streamlit as st
from utils import data_handler

# Expand the web app across the whole screen
st.set_page_config(layout="wide")

st.header("Data")

uploadedfiles = st.session_state.fileUploader

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
            st.dataframe(data_handler.dropper(data[c]).head())

            csv = data_handler.convert_df(data_handler.dropper(data[c]))

            st.download_button(
                "Press to Download",
                csv,
                "start_data.csv",
                "text/csv"
)