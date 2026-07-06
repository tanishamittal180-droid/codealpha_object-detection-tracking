import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px

st.title("AI Smart Surveillance Dashboard")

conn=sqlite3.connect(
"detections.db"
)

df=pd.read_sql(
"SELECT * FROM detections",
conn
)

st.dataframe(df)

if len(df)>0:

    chart=px.histogram(
    df,
    x="object_name"
    )

    st.plotly_chart(chart)