import streamlit as st

# Click, but on next rerun, go back to False
# If want to maintain true, set in session state
if "clicked" not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.button("Click me", on_click=click_button)
if st.session_state.clicked:
    # The message and nested widget will remain on the page
    st.write("Button clicked!")
    st.slider("Select a value")

# Or can use value of session state in disabled parameter
if "button" not in st.session_state:
    st.session_state.button = False


def click_button():
    st.session_state.button = not st.session_state.button


st.button("Click me 2", on_click=click_button)
st.slider("Select a value 2", disabled=st.session_state.button)

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
