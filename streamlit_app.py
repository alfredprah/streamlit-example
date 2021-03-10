#app.py
import streamlit_app1
import streamlit_app2

import streamlit as st
PAGES = {
    "App1": streamlit_app1,
    "App2": streamlit_app2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
