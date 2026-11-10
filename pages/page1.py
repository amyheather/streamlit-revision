import time

import numpy as np
import pandas as pd
import streamlit as st

# Create title using st.title() or st.markdown with #
st.title("Page 1 - basic concepts")
# st.markdown("# Page 1 - basic concepts")

st.sidebar.markdown("# Sidebar for page 1")

st.write("Hello world")

# ----------------------------------------------------------------------------
# Summary
# ----------------------------------------------------------------------------

# https://docs.streamlit.io/develop/api-reference

# ----------------------------------------------------------------------------
# Connecting to data
# ----------------------------------------------------------------------------

# Has support for various connections e.g., SQLLite

# ----------------------------------------------------------------------------
# Secrets
# ----------------------------------------------------------------------------

# Using secrets file

# ----------------------------------------------------------------------------
# User authentication
# ----------------------------------------------------------------------------

# User authentication now natively supported via OpenIC Connect
# There are functions st.login(), st.logout() and st.user

# ----------------------------------------------------------------------------
# Classes
# ----------------------------------------------------------------------------

# Define your classes in a separate module
# If you define it within the streamlit script, it will be redefined with
# every run of the page, which can have unwanted effects

# ----------------------------------------------------------------------------
# Multithreading (i.e., parallal processing)
# ----------------------------------------------------------------------------

# Not natively supported but docs do explain a way to do it

# ----------------------------------------------------------------------------
# Dataframes and tables
# ----------------------------------------------------------------------------

st.subheader("Dataframes")

dataframe = pd.DataFrame(
    np.random.randn(10, 20), columns=(f"col {i}" for i in range(20))
)

# Can pass almost anything to st.write()
# It will figure out and render in right way
# However, you may want to use more specific commands...
# - This calls st.dataframe() but you might want a static table - in which
#   case use st.table()
# - Also, might want to directly use st.dataframe() to pass additional
#   arguments
st.write(dataframe)

# Use pandas Styler object to highlight max value in each row
st.dataframe(dataframe.style.highlight_max(axis=0))

# Static table
st.table(dataframe)

# Editable dataframe
st.header("Editable dataframe")
df = pd.DataFrame(
    [
        {"command": "st.selectbox", "rating": 2},
        {"command": "st.balloons", "rating": 3},
        {"command": "st.time_input", "rating": 4},
    ]
)
edited_df = st.data_editor(df, num_rows="dynamic")
favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

# Editable other things! e.g., dictionaries
st.subheader("Editable dictionary")
st.data_editor({
	"st.text_area": "widget",
	"st.markdown": "element"
})

# Streamlit uses lazy loading for large dataframes
# (i.e., just load what is visible)

# ----------------------------------------------------------------------------
# Line charts and maps
# ----------------------------------------------------------------------------

st.header("Line charts and maps")

# Create line chart using Altair
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

# Create map using PyDeck and Carto
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(map_data)

# ----------------------------------------------------------------------------
# Widgets
# ----------------------------------------------------------------------------

# Widgets. These can be accessed either:
# - As a variable (so assign varname = st. ...)
# - By key (so provide a key argument)
# Using a key protects widget from resets when widget characteristics change
x = st.slider("x")
st.write(x)
st.text_input("Your name", key="name")
st.write(st.session_state.name)

# One of the usecases for checkboxes is to hide/show../
if st.checkbox("show dataframe"):
    st.table(dataframe)

# Selectbox

# Organise widgets in left panel sidebar. Can either:
# - Use object notation (st.sidebar. ...)
# - Use with sidebar: block (st.echo requires this)
st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# To preserve widget values between pages, set persist_state="session"
# Options are:
# - None (default) - value is dropped when widget isn't rendered
# - "page" - value is preserved while user stays on page
# - "session" - value is preserved across entire session
st.selectbox(
    label="Which number do you like best?",
    options=[1, 2, 3, 4],
    key="favouritenumber",
    persist_state="session",
)

# Alternatively can use bind
# THis will sync a widgets value with a URL query parameter
# Which makes it easy to create shareable URLs that preserve widget state
# and alllow users to bookmark specific app configurations
st.selectbox(
    label="Color", options=["Red", "Green", "Blue"], key="color", bind="query-params"
)

# st.expander() and st.time() also accept bind="query-params" with a key
# so a shared URL can keep an expander open or a specific tab selected

# ----------------------------------------------------------------------------
# Progress
# ----------------------------------------------------------------------------

# Progress bar using st.progress()
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)
