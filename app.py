
import streamlit as st

page1 = st.Page("page1.py", title="Page 1")
page2 = st.Page("page2.py", title="Page 2")

pg = st.navigation([page1, page2])

pg.run()
