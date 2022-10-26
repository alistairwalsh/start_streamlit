from distutils.command.upload import upload
import pandas as pd
import streamlit as st
from utils import data_handler

# Expand the web app across the whole screen
st.set_page_config(layout="wide")

st.header("Data")

if 'fileUploader' not in st.session_state:
    st.write('Please upload a datafile at home page')

else:
    
    uploadedfiles = st.session_state.fileUploader

    if uploadedfiles is not None:
        for f in uploadedfiles:
            st.title(f.name)
            data = pd.read_excel(f)
            survey_col_list = data_handler.slicer(data)

            for c in survey_col_list:
                st.dataframe(data_handler.dropper(data[c]).astype(str))

                csv = data_handler.convert_df(data_handler.dropper(data[c]))

                st.download_button(
                    "Press to Download",
                    csv,
                    "start_data.csv",
                    "text/csv"
                )