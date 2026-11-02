import time

import numpy as np
import pandas as pd
import streamlit as st

st.write("Hello world")

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

# Create line chart using Altair
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

# Create map using PyDeck and Carto
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
)
st.map(map_data)

# Widgets. These can be accessed either:
# - As a variable (so assign varname = st. ...)
# - By key (so provide a key argument)
x = st.slider("x")
st.write(x)
st.text_input("Your name", key="name")
st.write(st.session_state.name)

# One of the usecases for checkboxes is to hide/show../
if st.checkbox("show dataframe"):
    st.table(dataframe)

# Selectbox
st.selectbox(label="Which number do you like best?", options=[1, 2, 3, 4])

# Organise widgets in left panel sidebar. Can either:
# - Use object notation (st.sidebar. ...)
# - Use with sidebar: block (st.echo requires this)
st.sidebar.selectbox(
    "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
)

# Columns
left_col, right_col = st.columns(2)
with right_col:
    st.radio("Hat", ("Hat 1", "Hat 2", "Hat 3"))

# Expander
with st.expander("See hidden content"):
    st.write("Hello!")

# Progress bar using st.progress()
latest_iteration = st.empty()
bar = st.progress(0)
for i in range(100):
    latest_iteration.text(f"Iteration {i + 1}")
    bar.progress(i + 1)
    time.sleep(0.1)
