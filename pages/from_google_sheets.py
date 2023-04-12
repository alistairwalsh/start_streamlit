import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect
import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache_resource(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

#st.write(type(rows))

#st.write(rows)
df = pd.DataFrame(rows)
st.dataframe(df)

# # Print results.
# for row in rows:
#     st.write(f"{row.name} has a :{row.pet}:")
pr = df.profile_report()

st_profile_report(pr)