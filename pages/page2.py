import datetime
import numpy as np
import pandas as pd
import requests
import streamlit as st

st.markdown("# Page 2 - advanced concepts")

# ----------------------------------------------------------------------------
# Cacheing and session state
# ----------------------------------------------------------------------------

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

# Note: st.cache() is removed - replaced with these above.

# If its the first time streamlit has seen the input parameters for the
# function call and the code inside the function (this exact combination) then
# it runs the function and stores the result in local cache. Next time the
# function is called, if the two values (inputs and code) haven't changed
# then it knows it can skip executing the function
# Note: It only checks code of that function, not helper functions

DATE_COLUMN = "date/time"
DATA_URL = (
    "https://s3-us-west-2.amazonaws.com/"
    "streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

# Can do custom spinner message
@st.cache_data
def load_data(nrows, show_spinner="Fetching data from API..."):
    data = pd.read_csv(DATA_URL)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    # This will show everytime
    st.success("Fetched data")
    return data

#data_load_state = st.text("Loading data...")
#data = load_data(nrows=10000)
#data_load_state.text("Loading data...done (using st.cache)!")

# Another example... here, we set time to live to get new results from
# database, so streamlit invalidates any cached values after 1 hour (3600
# seconds) and runs the cached function again
# connection = database.connect()
#@st.cache_data(ttl=3600)
#def query():
#    return pd.read_sql_query("SELECT * FROM table", connection)

# It's also good to cache API calls
@st.cache_data
def api_call():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    return response.json()

# Whenever there is a long running computation in your code, consider
# refactoring it to use st.cache_data - e.g.,
@st.cache_data
def transform(df):
    df = df.filter(items=["one", "three"])
    df = df.apply(np.sum, axis=0)
    return df
# This includes e.g., running machine learning models

# An alternative to cache_resource() is to use st.connection (simpler,
# available for most popular connections)
# conn = st.connection("my_database")
# df = conn.query("select * from my_table")
# Username and password stored in .streamlit/secrets.toml

# ----------------------------------------------------------------------------
# Session state
# ----------------------------------------------------------------------------

# When first create, check if not in session state then...
if "counter" not in st.session_state:
    st.session_state.counter = 0
st.session_state.counter += 1
st.header(f"This page has run {st.session_state.counter} times.")
st.button("Run it again")

# ----------------------------------------------------------------------------
# Callbacks and forms
# ----------------------------------------------------------------------------

# Callbacks: have on_click which will run a function, and can pass args

if "count" not in st.session_state:
    st.session_state.count = 0
    st.session_state.last_updated = datetime.time(0,0)

def update_counter(sign):
    st.session_state.count += sign * st.session_state.increment_value
    st.session_state.last_updated = st.session_state.update_time

# Use forms to group widgets so they update app in single batch instead of invidiually
with st.form(key="counter_form"):
    st.subheader("Inputs within a form")
    st.time_input(label="Enter the time", value=datetime.datetime.now().time(), key="update_time")
    st.number_input("Enter a value", value=0, step=1, key="increment_value")
    submit = st.form_submit_button(label="Update", on_click=update_counter, kwargs={"sign": 1})

# These are not within form so doesn't happen all together
# When widget is not in form it will trigger rerun for every click
st.button("Increment", on_click=update_counter, args=(1,))
st.button("Decrement", on_click=update_counter, kwargs={"sign": -1})

st.write("Count = ", st.session_state.count)
st.write("Last updated = ", st.session_state.last_updated)

# Appears when form is submit
if submit:
    st.write("You ran the form")

# ----------------------------------------------------------------------------
# Static
# ----------------------------------------------------------------------------

# If you want a direct URL to an image or file you'll need to host it
# This requires setting the correct configuration and placing the hosted files
# in a directory called static

# ----------------------------------------------------------------------------
# Histogram
# ----------------------------------------------------------------------------

# This uses streamlit's native st.bar_chart(), but it also supports others
# (matplolib, altair, plotly, echarts, etc.)
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)

#hour_to_filter = st.slider(
#    label="hour",
#    min_value=0,
#    max_value=23,
#    value=17
#)
#filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
#st.subheader(f"Map of all pickups at {hour_to_filter}")
#st.map(filtered_data)