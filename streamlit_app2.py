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
  st.button('Gun Violence', key=None)
  st.button('Refugee Crisis', key=None)
  st.button('Healthcare', key=None)
  st.button('Voting Rights', key=None)
  st.button('Income Gap', key=None)
  st.button('Black Lives Matter', key=None)
