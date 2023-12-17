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

bg_o = bg.drop(index = [49, 131, 164, 156, 51, 93, 200, 441, 473, 690, 816, 823, 916, 949])

options = ['Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings', 'Year Published',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price', 'Age (Years)', 'Time Category', 'AgeRating',
       'GroupSize']

with tab1:
       selected_variable = st.selectbox('Select a variable', options) #First field is prompt, second field is options
       outlier_switch = st.checkbox("Remove Outliers", value = False)
       if(outlier_switch == False):
              bg1 = bg
       else: bg1 = bg_o
       title = "Histogram of " + selected_variable
       plot = sns.histplot(data = bg1, x = selected_variable).set_title(title)
       st.pyplot(plot.get_figure())

with tab2:
       st.info("This is filler right now")
       options2 = ['Time Category', 'AgeRating','GroupSize']
       select_variable = st.selectbox('Select a variable', options2)
       title = 'Distribution of Number of Ratings by ' + select_variable
       plot1 = sns.violinplot(data=bg, y = "Number of Ratings", x = select_variable, palette="Reds").set_title(title)
       st.pyplot(plot1.get_figure())