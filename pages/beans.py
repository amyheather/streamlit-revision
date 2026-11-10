"""app.py"""
import streamlit as st

st.selectbox("A", [1,2,3], None, help="Pick a number", placeholder="Pick me")

# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)

st.title("Bean counter :paw_prints:")

addend = st.number_input("Beans to add", 0, 10, key="bean_increment")
if st.button("Add", key="bean_add"):
    st.session_state.beans += addend
st.markdown(f"Beans counted: {st.session_state.beans}")