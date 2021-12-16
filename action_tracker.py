import streamlit as st
import pandas as pd
import numpy as np


st.title("Action Tracker")

df = pd.read_excel("KPI_ACTION_TRACKER.xlsx", header=0)

country_list = df["Country"].unique()

# file_path = "C:\Users\koota\OneDrive\デスクトップ\KOTA\STREAMLIT\10 ACTION TRACKER"

with open("KPI_ACTION_TRACKER.xlsx", 'rb') as my_file:
    st.sidebar.download_button(label = 'Download', data = my_file, file_name = 'KPI_ACTION_TRACKER.xlsx', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')      


selected_country = st.sidebar.selectbox("Counry", country_list)
# st.sidebar.file_uploader("File Upload")

# selected_country = st.sidebar.multiselect(
#     "Select your country",
#     ["Japan", "Korea"],
#     ["Japan", "Korea"]
# )

df_country = df[df["Country"] == selected_country]

# st.write(df_country)
st.table(df_country)
# st.dataframe(df_country, width=900, height=2000)


