#app.py
import streamlit_app1
import streamlit_app2

import streamlit as st
PAGES = {
     "Home": streamlit_app2,
     "Black Lives Matter": streamlit_app1,
     "Gun Violence": streamlit_app1,
     "Refugee Crisis":streamlit_app1,
     "Income Gap":streamlit_app1,
     "Healthcare":streamlit_app1,
     "Voting Rights":streamlit_app1
   
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
