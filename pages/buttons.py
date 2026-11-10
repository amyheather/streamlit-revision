import streamlit as st

# ----------------------------------------------------------------------------
# If want button to REMAIN True (ordinarily, returns to False)
# ----------------------------------------------------------------------------

st.header("Stateful button")

# Click, but on next rerun, go back to False
# If want to maintain true, set in session state
if "clicked" not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.button("Permanently show the slider", on_click=click_button)
if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write("Button clicked!")
    st.slider("Select a value")

# ----------------------------------------------------------------------------
# Disable things based on button click
# (CONSIDER st.checkbox instead)
# ----------------------------------------------------------------------------

st.header("Toggle button")

# Or can use value of session state in disabled parameter
if "button" not in st.session_state:
    st.session_state.button = False


def click_button():
    st.session_state.button = not st.session_state.button


st.button("Disable the slider", on_click=click_button)
st.slider("Select a value 2", disabled=st.session_state.button)

# ----------------------------------------------------------------------------
# Buttons to continue or control between stages
# ----------------------------------------------------------------------------

# Buttons to continue or control stages...
st.header("Stages")
if "stage" not in st.session_state:
    st.session_state.stage = 0


def set_state(i):
    st.session_state.stage = i


if st.session_state.stage == 0:
    st.button("Begin", on_click=set_state, args=[1])

if st.session_state.stage >= 1:
    name = st.text_input("Name", on_change=set_state, args=[2])

if st.session_state.stage >= 2:
    st.write(f"Hello {name}!")
    color = st.selectbox(
        "Pick a Color",
        [None, "red", "orange", "green", "blue", "violet"],
        on_change=set_state,
        args=[3],
    )
    if color is None:
        set_state(2)

if st.session_state.stage >= 3:
    st.write(f":{color}[Thank you!]")
    st.button("Start Over", on_click=set_state, args=[0])

# ----------------------------------------------------------------------------
# There's some complicated stuff around modifying session state using button...
# Also around clearing session state with a button...
# Not worrying about for now
# ----------------------------------------------------------------------------
