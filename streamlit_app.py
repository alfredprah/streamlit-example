#app.py
import streamlit_app1
import streamlit_app2

import streamlit as st
#### This is our very first sample dashboard so cheers 🥂🍻
PAGES = {
     "Home": streamlit_app2,
    "Black Lives Matter": streamlit_app1
   
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
