import streamlit as st

st.markdown("# Page 2 - advanced concepts")

# Cache saves a value across all sessions and users
# e.g., if pulling same data for all users
# Session state saves values for a single user
# e.g., if pulling data specific to a user

# Cacheing can be done using a decorator, either:

# - st.cache_data() (for computations that return data)
#   Creates new copy of data at each function call, making it safe against
#   mutations (changes to value after function call)

# - st.cache_resource() (for e.g., ML models or database connections)
#   Returns the cached object itself, which is shared across reruns and
#   sessions, and mutations exist across all reruns and sessions

# Session state
# When first create, check if not in session state then...
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

# An alternative to cache_resource() is to use st.connection (simpler,
# available for most popular connections)
# conn = st.connection("my_database")
# df = conn.query("select * from my_table")
# Username and password stored in .streamlit/secrets.toml

# If you want a direct URL to an image or file you'll need to host it
# This requires setting the correct configuration and placing the hosted files
# in a directory called static