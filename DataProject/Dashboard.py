import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Board Games Bonanza")

sidebar1 = st.sidebar
sidebar1.info("This app is maintained by Braden Critchfield. All data comes from Board Games Geek and was accessed November 17, 2023.")
sidebar1.image("DataProject/BGG.webp")
#sidebar1.info("Visit bradenmcritchfield.github.io for blog posts about this data.")

tab1, tab2, tab3 = st.tabs(["Histograms", "Violin Plots", "Over Time"])
bg = pd.read_csv("DataProject/boardgamesdata.csv")
bg["GroupSize"] = pd.Categorical(bg["GroupSize"], categories = ["Individual", "Small", "Large", "Massive"], ordered = True)
bg["Time Category"] = pd.Categorical(bg["Time Category"], categories = ["Quick", "Short", "Moderate", "Long", "Very Long", "Marathon"], ordered = True)
bg["AgeRating"] = pd.Categorical(bg["AgeRating"], categories = ["Young", "PreTeen", "Teen", "Adult", "Any"], ordered = True)

bg_1950plus = bg.drop([49, 200, 441, 690, 816, 916, 949])
bg_grouped = bg_1950plus.groupby("Year Published")
bg_agg = bg_grouped.mean(numeric_only = True)

bg_o = bg.drop(index = [49, 131, 164, 156, 51, 93, 200, 441, 473, 690, 816, 823, 916, 949])

options = ['Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings', 'Year Published',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price', 'Age (Years)', 'Time Category', 'AgeRating',
       'GroupSize']
options3 = ['Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price']


with tab1:
       selected_variable = st.selectbox('Select a variable', options) #First field is prompt, second field is options
       outlier_switch = st.checkbox("Remove Outliers", value = False)
       if(outlier_switch == False):
              bg1 = bg
       else: bg1 = bg_o
       title = "Histogram of " + selected_variable
       plot = sns.histplot(data = bg1, x = selected_variable).set_title(title)
       st.pyplot(plot.get_figure(), clear_figure = True)
       st.info("View specific games:")
       value_min_input = st.text_input("Insert minimum value for " + selected_variable)
       value_max_input = st.text_input("Insert maximum value for " + selected_variable)                                
       st.dataframe(bg.loc[(bg[selected_variable] >= value_min_input) and (bg[selected_variable] <= value_max_input) ])

with tab2:
       options2 = ['Time Category', 'AgeRating','GroupSize']
       select_variable = st.selectbox('Select a variable', options2)
       title = 'Distribution of Number of Ratings by ' + select_variable
       plot1 = sns.violinplot(data=bg, y = "Number of Ratings", x = select_variable, palette="Reds").set_title(title)
       st.pyplot(plot1.get_figure(), clear_figure = True)


with tab3:
       select_variable2 = st.selectbox("Choose Variable", options3)
       title = "Average " + select_variable2 + " by Year Published"
       bg_agg1 = {select_variable2: bg_agg[select_variable2]}
       df = pd.DataFrame(bg_agg1).reset_index()
       plot2 = sns.lineplot(data = df, x = "Year Published", y = select_variable2).set_title(title)
       st.pyplot(plot2.get_figure(), clear_figure = True)