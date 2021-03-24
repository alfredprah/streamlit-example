from collections import namedtuple
import textblob
from textblob import TextBlob
import altair as alt
import math
import pandas as pd
import streamlit as st

import datetime
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

"""
# Welcome to the c4project Dashboard!
#### This is our very first sample dashboard so cheers 🥂🍻
"""
"""
"""
"""
#### Black Lives Matter (BLM)
Tweets:
"""
def app():
    st.title('c4project - Black Lives Matter')
    st.text("") 
    st.text("")  
    """
    """
    #st.write("Tweets")
    data = pd.read_csv('sample_tweets.csv')
    data_size = data.shape[0]

    html = f"<a href='<img src='blm.jpeg;base64,{image_base64}'></a>" 
    st.markdown(html, unsafe_allow_html=True)
    
    st.write("There are " + str(data_size) + " tweets available on BLM")
    
    st.dataframe(data, width=None, height=None)
    
    #st.line_chart(data.Time)

    st.text("") 
    st.text("")  
    st.text("")
    #st.write("Web links from Tweets")
    data2 = pd.read_csv('urls.csv')
    data_size2 = data2.shape[0]
    st.write("There are " + str(data_size2) + " urls associated with the tweets")
    st.dataframe(data2, width=None, height=None)
    """
    """
    fig, ax = plt.subplots(figsize=(8, 6))

    # Create textblob objects of the tweets
    sentiment_objects = [TextBlob(tweet) for tweet in data['Tweet']]

    # Create list of polarity values and tweet text
    sentiment_values = [[tweet.sentiment.polarity, str(tweet)] for tweet in sentiment_objects]

    # Create dataframe containing the polarity value and tweet text
    sentiment_df = pd.DataFrame(sentiment_values, columns=["polarity", "tweet"])

    # plot polarities on a histogram:
    fig, ax = plt.subplots(figsize=(8, 6))
    st.text("") 
    st.text("")  
    st.text("")
    st.write("Current Sentiments on Tweets on BLM as of 2 PM CST")
    # Plot histogram of the polarity values
    st.bar_chart(sentiment_df.polarity)
    
    
    st.text("") 
    st.text("")  
    st.text("")
    st.line_chart(data.Time)
    
    
    
    total_points = st.slider("Number of points in tweets", 1, 5000, 200)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)
    Point = namedtuple('Point', 'x y')
    data = []
    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))
    
    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
                .mark_circle(color='#0068c9', opacity=0.5)
                .encode(x='x:Q', y='y:Q'))
