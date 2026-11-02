
import streamlit as st

# If done once, it applies universally
# If done on each page, can have different ones for different pages
st.set_page_config(
    page_title="Streamlit revision",
    # page_icon="",
)

st.sidebar.success("Constant item in sidebar")

page1 = st.Page("pages/page1.py", title="Page 1")
page2 = st.Page("pages/page2.py", title="Page 2")

# This allows us to specify page order without using the filenames like
# 1_page 2_page etc.
pg = st.navigation([page1, page2])

pg.run()
