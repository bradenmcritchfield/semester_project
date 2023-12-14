import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Board Games Bonanza")

with st.sidebar:
    with st.echo():
        st.write("This code will be printed to the sidebar.")

bg = pd.read_csv("DataProject/boardgamesdata.csv")

options = ['Year Published', 'Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price', 'Age (Years)', 'Time Category', 'AgeRating',
       'GroupSize']

selected_variable = st.selectbox('Select a variable', options) #First field is prompt, second field is options
title = "Histogram of " + selected_variable
plot = sns.histplot(data = bg, x = selected_variable).set_title(title)


st.pyplot(plot.get_figure())

