import time

import streamlit as st

# Use st.sidebar() for persistent controls visible across app
# Can write into sidebar (and all the other contains below) either...

# (A) Context manager (with)
with st.sidebar:
    st.write("Some text in the sidebar")

# (B) Method calls - handy if made container earlier in script
sidebar = st.sidebar
sidebar.write("More text in sidebar")

# ---------------------------------------------------------------------------
# Collapsible and overlay containers
# ---------------------------------------------------------------------------

# Use st.tabs, st.expander and st.popover to organise content in
# collapsible or overlay containers

# Tabs
tab1, tab2, tab3 = st.tabs(["Chart", "Data", "Settings"])
with tab1:
    st.line_chart({"data": [1, 5, 2, 6, 2, 1]})
with tab2:
    st.dataframe({"col1": [1, 2, 3], "col2": [4, 5, 6]})
with tab3:
    st.checkbox("Show gridlines")

# Expander
with st.expander("See hidden content"):
    st.write("Hello!")

# Popover (similar to expander but more like dropdown, and not full width)
with st.popover("Filter settings"):
    st.checkbox("Include archived")
    st.slider("Min score", 0, 100, 50)

# These can track their open/closed state and trigger reruns with on_change
# This enables lazy loading of content in tabs and expanders
st.header("Tabs - on change")
tab1, tab2 = st.tabs(["Chart", "Data"], on_change="rerun")
if tab1.open:
    with st.spinner("Loading Tab 1..."):
        time.sleep(2)
    with tab1:
        st.line_chart({"data": [1, 5, 2, 6]})
if tab2.open:
    with st.spinner("Loading Tab 2..."):
        time.sleep(2)
    with tab2:
        st.dataframe({"col1": [1, 2, 3]})

# Can pass callbacks to on_change to run a function when user opens, closes
# or switches containers
st.header("Tabs - callback")


def on_tab_change():
    st.toast(f"Tab changed to {st.session_state.tabs}!")


tab_input, tab_output = st.tabs(
    ["Input", "Output"], on_change=on_tab_change, key="tabs"
)
with tab_input:
    st.write("Input")
with tab_output:
    st.write("Output")

# If provide key to container, can manipulate state through session_state
st.header("Tabs - programmatic control")


def toggle_expander():
    st.session_state.details = not st.session_state.details


exp = st.expander("Details", key="details", on_change="rerun")
with exp:
    st.write("Detailed content here")
st.button("Toggle expander", on_click=toggle_expander)

# ---------------------------------------------------------------------------
# Columns
# ---------------------------------------------------------------------------

st.header("columns")
# Use st.columns to place elements side-by-side
col1, col2, col3 = st.columns(3)
col1.write("Column 1")
col2.write("Column 2")
col3.write("Column 3")

# Can have unequal widths
left, right = st.columns([2, 1])
left.write("This column is twice as wide.")
right.write("This column is narrower.")

# By default columns will stack on narrow views, but can use wrap=False to
# prevent that
cols = st.columns(6, wrap=False)
for i, col in enumerate(cols, start=1):
    col.button(f"{i}")

# ---------------------------------------------------------------------------
# Container
# ---------------------------------------------------------------------------

# Use st.container to:
# - Group elements
# - Control display order independent from script order
# Can add a visible border with border=True
with st.container(border=True):
    st.write("This has a border around it")

# Can layout contents of container horizonally.
# FOR SIDE BY SIDE LAYOUTS THIS IS PREFERRED OVER COLUMNS
# As it adapts naturally to content... each element only takes space it needs
with st.container(horizontal=True, border=True):
    st.button("One")
    st.button("Two")
    st.button("Three")

# ---------------------------------------------------------------------------
# Other CONTAINER AND COLUMN customisations...
# ---------------------------------------------------------------------------

# - wrap - will wrap to next line when overflow or make scrollbar
# - horizontal_alignment - push to left, right or centre
# - gap - control spacing between elements
# - height - control height to make scrollable region
with st.container(
    horizontal=True, border=True, horizontal_alignment="center", gap="large", height=200
):
    st.button("A")
    st.button("B")
    st.button("C")
    for i in range(20):
        st.write(f"Line {i}")

# Use st.space() for manual spacing
st.write("Above")
st.space("large")
st.write("Below, with a large gap")

# ---------------------------------------------------------------------------
# Empty
# ---------------------------------------------------------------------------

# Use st.empty to make placeholder
# It will be empty, or can have content which you write to it, but that will
# disappear and be replaced everytime you write to it
placeholder = st.empty()
for i in range(5):
    placeholder.write(f"Iteration {i}")
    time.sleep(0.5)
placeholder.empty()

# Can call empty on an object to clear it
# Or can also just replace with any other elements
el = st.text("Temporary message")
el.write("Done!")
el.empty()

# SOme elements have specific replace methods...
# Status containers can be updated with .update()
# Toast can be updated with .toast()
# Progress with .progress()

# To replace a group of objects, nest st.container inside st.empty
placeholder = st.empty()
with placeholder.container():
    st.write("First set of content")
    st.button("A button")
time.sleep(2)
with placeholder:
    st.write("Replacement content")
