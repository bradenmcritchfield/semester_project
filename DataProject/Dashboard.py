import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.title("Board Games Bonanza")

bg = pd.read_csv("boardgamesdata.csv")

fig = px.line(bg.groupby('Year Published')['count'].sum())
st.plotly_chart(fig)