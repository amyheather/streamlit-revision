import streamlit as st

# If done once, it applies universally
# If done on each page, can have different ones for different pages
st.set_page_config(
    page_title="Streamlit revision",
    # page_icon="",
)

st.sidebar.success("Constant item in sidebar")

# Common widget that persist across all pages
# (Instead of having on one page with persist_station="session")
user_name = st.sidebar.text_input("Name", key="global_name")

# ----------------------------------------------------------------------------
# Pages and navigation
# ----------------------------------------------------------------------------

# Pages
# Declare any Python file or Callable as a page
# Each page can specify title, icon, url_path
# First will be opening page or can specify with default=True
page1 = st.Page("pages/page1.py", title="Page 1")
page2 = st.Page("pages/page2.py", title="Page 2")
page_layout = st.Page("pages/layout.py", title="Layout")
page_buttons = st.Page("pages/buttons.py", title="Buttons")

# This allows us to specify page order without using the filenames like
# 1_page 2_page etc.
# You can just auto create with pages directory but that bases on filenames...
# can override with st.page_link and client.showSidebarNavigation = false...
# prefer st.navigation...

# Can provide just straight list like below, or group with dict to make sections
pg = st.navigation(
    [page1, page2, page_layout, page_buttons],
    position="sidebar",  # Can change to "top"
)

pg.run()
