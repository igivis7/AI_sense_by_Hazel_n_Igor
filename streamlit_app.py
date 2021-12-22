import pandas as pd
import numpy as np
import streamlit as st
import time
import tensorflow as tf
from altair.vegalite.v4.schema.core import Header
import altair as alt
#import serial
from PIL import Image



##------------------------
## Initialize variables
##------------------------
## from
## https://docs.streamlit.io/library/advanced-features/session-state


##------------------------
## Page decorations
##------------------------
st.title('Hello World! :sunglasses:')
st.write('Welcome to Portfolio Project - AI Sense. We are Igor Isaev and Hazel Wat, current student at Data Science Retreat, Berlin. Batch 28 (Sept-Dec 2021). We use a machine learning model to detech smells and categorize it.')
st.write('6 Elements are extracted from the gas sensors. They are NO2, C2H5CH, VOC, CO, temperature and humidity. We utilize machine learning models to establish correlation and predict the result. Gas interval are collected at 10s.')


##------------------------
## Button Data reading
##------------------------

##------------------------
## Button Simulation
##------------------------



##------------------------
## Button Predicting
##------------------------



##------------------------
## Footnote
##------------------------
st.write('Connect with us')
st.write('Igor Isaev: https://www.linkedin.com/in/igor-isaev/')
st.write('Hazel Wat: https://www.linkedin.com/in/hazelwat/')
st.write("Github: https://github.com/igivis7/DRS28_Hazel_n_Igor_portfolio_project")

image=Image.open("pic_20Dec21.jpg")
st.image(image)