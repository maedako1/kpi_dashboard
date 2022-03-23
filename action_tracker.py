import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go



st.title("Action Tracker")

df = pd.read_excel("KPI_ACTION_TRACKER.xlsx", header=0)

country_list = df["Country"].unique()

# file_path = "C:\Users\koota\OneDrive\デスクトップ\KOTA\STREAMLIT\10 ACTION TRACKER"

with open("KPI_ACTION_TRACKER.xlsx", 'rb') as my_file:
    st.sidebar.download_button(label = 'Download', data = my_file, file_name = 'KPI_ACTION_TRACKER.xlsx', mime = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')      


selected_country = st.sidebar.selectbox("Country", country_list)
# st.sidebar.file_uploader("File Upload")

# selected_country = st.sidebar.multiselect(
#     "Select your country",
#     ["Japan", "Korea"],
#     ["Japan", "Korea"]
# )

df_country = df[df["Country"] == selected_country]

fig = go.Figure(data=[go.Table(
    columnorder = [1, 2, 3, 4, 5, 6, 7], 
    columnwidth = [100, 150, 200, 150, 150, 500, 100],
    header = dict(values=["Country", "What_Action Items","Why", "Who_Responsible","When_Due_date", "How",  "Progress"],
                  fill_color="paleturquoise",
                  align="left"),
    cells=dict(values=[df_country.Country, df_country.What_Action_Items, df_country.Why, df_country.Who_Responsible, 
                       df_country.When_Due_date, df_country.How, df_country.Progress],
               align=["left", "left"],
               font_size=13,
               height=30)
)])

# st.write(df)
# st.table(df_country)
# fig.show()


st.plotly_chart(fig)