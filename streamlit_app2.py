from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import datetime
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

def app():
  st.title("Welcome to c4projects's Dashboard for Protests.")
  ####"This is our very first sample dashboard so cheers 🥂🍻"
  st.text("") 
  st.text("")  
  st.text("")
  st.button('Gun Violence', key=None)
  st.button('Refugee Crisis', key=None)
  st.button('Healthcare', key=None)
  st.button('Voting Rights', key=None)
  st.button('Income Gap', key=None)
  st.button('*Black Lives Matter', key=None)
  """
  """
  st.text("")
  st.text("") 
  st.text("")  
  st.text("")
  st.write("The '*' is used to mark a label that's a subcategory but of great interest to researchers and scholars.")
