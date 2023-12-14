import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Board Games Bonanza")

bg = pd.read_csv("boardgamesdata.csv")

options = ['Year Published', 'Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price', 'Age (Years)', 'Time Category', 'AgeRating',
       'GroupSize']
selected_variable = st.selectbox('Select a variable', bg) #First field is prompt, second field is default

fig = sns.histplot(data = bg, x = selected_variable)

st.pyplot(fig)
