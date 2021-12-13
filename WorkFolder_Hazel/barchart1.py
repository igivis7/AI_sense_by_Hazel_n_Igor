
import pandas as pd
import numpy as np
import streamlit as st

# 50 rows and 3 columns Pandas DataFrame
chart_data = pd.DataFrame(
     np.random.randn(50, 3),
     columns=["a", "b", "c"])

st.bar_chart(chart_data)


