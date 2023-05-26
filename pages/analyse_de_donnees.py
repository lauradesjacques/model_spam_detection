import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title('Analyse de données')

data = pd.read_csv("./data/spam.csv")
message = data['MESSAGE'].value_counts()

fig = go.Figure(
    go.Pie(
        labels=['No Spam','Spam'],
        values=message,
        hole=0.5,
        pull=[0.1, 0, 0, 0,
              0],
    ))


st.plotly_chart(fig)
