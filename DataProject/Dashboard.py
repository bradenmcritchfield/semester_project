import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Board Games Bonanza")

st.sidebar.info("This app is maintained by Braden Critchfield. All data comes from Board Games Geek and was accessed November 18, 2023.")

tab1, tab2, tab3 = st.tabs(["Histograms", "Violin Plots", "Scatterplots"])
bg = pd.read_csv("DataProject/boardgamesdata.csv")
bg["GroupSize"] = pd.Categorical(bg["GroupSize"], categories = ["Individual", "Small", "Large", "Massive"], ordered = True)
bg["Time Category"] = pd.Categorical(bg["Time Category"], categories = ["Quick", "Short", "Moderate", "Long", "Very Long", "Marathon"], ordered = True)
bg["AgeRating"] = pd.Categorical(bg["AgeRating"], categories = ["Young", "PreTeen", "Teen", "Adult", "Any"], ordered = True)


options = ['Year Published', 'Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price', 'Age (Years)', 'Time Category', 'AgeRating',
       'GroupSize']

with tab1:
       selected_variable = st.selectbox('Select a variable', options) #First field is prompt, second field is options
       title = "Histogram of " + selected_variable
       plot = sns.histplot(data = bg, x = selected_variable).set_title(title)
       st.pyplot(plot.get_figure())

