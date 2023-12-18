import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import plotly.express as px

st.title("Board Games Bonanza")

# Build sidebar
sidebar1 = st.sidebar
sidebar1.info("This app is maintained by Braden Critchfield. All data comes from Board Games Geek and was accessed November 17, 2023.")
sidebar1.image("DataProject/BGG.webp")
url1 = "https://bradenmcritchfield.github.io/2023/12/12/Board-Game-Bonanza-Data-Collection.html"
url2 = "https://bradenmcritchfield.github.io/2023/12/13/Board-Game-Bonanza-EDA.html"
url3 = "https://github.com/bradenmcritchfield/semester_project/tree/main/DataProject"
sidebar1.write("For more information, visit [my data collection blog post.](%s)" % url1)
sidebar1.write("You can also visit [my data exploration blog post.](%s)" % url2)
sidebar1.write("For relevant code, visit [my github repository.](%s)" % url3)

st.info("This dashboard explores data from the top 1000 rated board/card games on Board Games Geek.")
#set tabs
tab1, tab2, tab3 = st.tabs(["Histograms", "Violin Plots", "Over Time"])

#get data
bg = pd.read_csv("DataProject/boardgamesdata.csv")
bg["GroupSize"] = pd.Categorical(bg["GroupSize"], categories = ["Individual", "Small", "Large", "Massive"], ordered = True)
bg["Time Category"] = pd.Categorical(bg["Time Category"], categories = ["Quick", "Short", "Moderate", "Long", "Very Long", "Marathon"], ordered = True)
bg["AgeRating"] = pd.Categorical(bg["AgeRating"], categories = ["Young", "PreTeen", "Teen", "Adult", "Any"], ordered = True)

#set up alternate data frames
bg_1950plus = bg.drop([49, 200, 441, 690, 816, 916, 949])
bg_grouped = bg_1950plus.groupby("Year Published")
bg_agg = bg_grouped.mean(numeric_only = True)
bg_o = bg.drop(index = [49, 131, 164, 156, 51, 93, 200, 441, 473, 690, 816, 823, 916, 949])

#set dropdown options
options1 = ['Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings', 'Year Published',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price', 'Time Category', 'AgeRating',
       'GroupSize']
options2 = ['Time Category', 'AgeRating','GroupSize']
options3 = ['Min Players', 'Max Players', 'Playing Time',
       'Age Minimum', 'Number of Accessories', 'Number of Ratings',
       'Average Rating', 'Bayes Rating', 'Standard Deviation',
       'Average USD Price']


with tab1:
       st.header("Distributions of Variables")
       selected_variable = st.selectbox('Select a variable', options1)
       outlier_switch = st.checkbox("Remove Outliers", value = False)
       if(outlier_switch == False):
              bg1 = bg
       else: bg1 = bg_o
       title = "Histogram of " + selected_variable
       plot = sns.histplot(data = bg1, x = selected_variable).set_title(title)
       st.pyplot(plot.get_figure(), clear_figure = True)
       st.caption("A histogram for the selected variable. Remove outliers if the distribution is difficult to see.")
      
with tab2:
       st.header("Distributions of Number of Ratings")
       select_variable = st.selectbox('Select a variable', options2)
       title = 'Distribution of Number of Ratings by ' + select_variable
       plot1 = sns.violinplot(data=bg, y = "Number of Ratings", x = select_variable, palette="Reds").set_title(title)
       st.pyplot(plot1.get_figure(), clear_figure = True)
       st.caption("The distribution of number of ratings for the selected variable. Notice that there is little significant difference between the different values.")

with tab3:
       st.header("Trends over Time")
       select_variable2 = st.selectbox("Choose Variable", options3)
       title = "Average " + select_variable2 + " by Year Published"
       bg_agg1 = {select_variable2: bg_agg[select_variable2]}
       df = pd.DataFrame(bg_agg1).reset_index()
       plot2 = sns.lineplot(data = df, x = "Year Published", y = select_variable2).set_title(title)
       st.pyplot(plot2.get_figure(), clear_figure = True)
       st.caption("Average of selected variable by year published. For most variables, there is a change as the year gets closer to the present.")

st.header("Explanation of Variables")
st.markdown("**Min Players:** the minimum number of players the game requires.")
st.markdown("**Max Players:** the maximum number of players the game allows.")
st.markdown("**Playing Time:** estimated amount of time a game takes.")
st.markdown("**Age Minimum:** recommended minimum age of players.")
st.markdown("**Number of Accessories:** number of accessories in the game.")
st.markdown("**Number of Ratings:** number of people who have given a rating for the game.")
st.markdown("**Year Published:** the year the game was first published.")
st.markdown("**Average Rating:** average of all ratings.")
st.markdown("**Bayes Rating:** average of all ratings plus 30 average ratings.")
st.markdown("**Standard Deviation:** the standard deviation of the ratings.")
st.markdown("**Average USD Price:** average price of games being sold in BGG's marketplace at time of data pull.")
st.markdown("**Age (Years):** age of the game in years.")
st.markdown("**Time Category:** category of game based on legnth of gameplay.")
st.markdown("**AgeRating:** category based on age minimum.")
st.markdown("**GroupSize:** category based on maximum number of players.")