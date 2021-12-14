import streamlit as st
import numpy as np
import pandas as pd

public_gsheets_url = "https://docs.google.com/spreadsheets/d/1yXGRegA1jLHUw5uuOLt1djhaZjBKl8ZfRNgiK0haJZ8/edit?usp=sharing"

# Everything is accessible via the st.secrets dict:

st.write("DB username:", st.secrets["hahahazel"])
st.write("DB password:", st.secrets["Family#1"])
st.write("My cool secrets:", st.secrets["my_cool_secrets"]["things_i_like"])

# And the root-level secrets are also accessible as environment variables:

import os

st.write(
    "Has environment variables been set:",
    os.environ["db_username"] == st.secrets["db_username"],
)