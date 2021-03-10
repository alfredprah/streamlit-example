#app.py
import streamlit_app1
import streamlit_app2

import streamlit as st
PAGES = {
     "Home": streamlit_app2,
    "Black Lives Matter": streamlit_app1,
     "Gun Violence"
   
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
