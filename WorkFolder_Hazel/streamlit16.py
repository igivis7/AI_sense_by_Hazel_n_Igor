
import pandas as pd
import numpy as np
import streamlit as st
import time

st.title('Hello World! :sunglasses:')
st.write('Welcome to AI Sense. We are Igor Isaev and Hazel Wat, current student at Data Science Retreat, Berlin. Batch 28. Our final portfolio project is AI Sense. We use a machine learning model to detech smells and categorized it.')
st.write('4 Elements are extracted from the gas sensors. They are NO2, C2H5CH, VOC, CO. We utilize machine learning models to establish correlation and predict the result. Gas interval are collected at 10s.')

if st.button('Going into smelling mode:'):
     my_bar = st.progress(0)

     for percent_complete in range(100):
        time.sleep(0.1)
        my_bar.progress(percent_complete + 1)
else:
    pass

if st.button('Predicting:'):
     st.write(':smile:'*3)
     chart_data = pd.DataFrame(
     np.random.rand(9, 4),
     columns=["NO2","C2H5CH","VOC","CO"],
     index=["air", "coffee", "orange","whitebread","potato","wine","beer","wheatbread","carrot"]
     )

     st.bar_chart(chart_data)
else:
     st.write('Smelling ...1...2...3:')

st.write('Connect with us')
st.write('Igor Isaev: https://www.linkedin.com/in/igor-isaev/')
st.write('Hazel Wat: https://www.linkedin.com/in/hazelwat/')