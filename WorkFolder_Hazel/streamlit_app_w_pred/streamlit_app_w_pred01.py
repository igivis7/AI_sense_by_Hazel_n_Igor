import pandas as pd
import numpy as np
import streamlit as st
import time
import tensorflow as tf


##------------------------
## Initialize variables
##------------------------
## from
## https://docs.streamlit.io/library/advanced-features/session-state
if 'data2predictArrST' not in st.session_state:
    st.session_state['data2predictArrST'] = np.array([])

if 'data2predictLabelST' not in st.session_state:
    st.session_state['data2predictLabelST'] = "no_label"

classes_values = [ "air", "beer", "bread", "carrot", "coffee", "orange", "potato", "wheatbread", "wine" ]

## Load into a new model
new_model = tf.keras.models.load_model('saved_model/TFNN_model_05')

## Data to predict
X_init = np.load('x_train.npy')
Y_init = np.load('y_train.npy')[:,0]



##------------------------
## Page decorations
##------------------------
st.title('Hello World! :sunglasses:')
st.write('Welcome to AI Sense. We are Igor Isaev and Hazel Wat, current student at Data Science Retreat, Berlin. Batch 28. Our final portfolio project is AI Sense. We use a machine learning model to detech smells and categorized it.')
st.write('4 Elements are extracted from the gas sensors. They are NO2, C2H5CH, VOC, CO. We utilize machine learning models to establish correlation and predict the result. Gas interval are collected at 10s.')


##------------------------
## Button Predicting
##------------------------
if st.button('Going into smelling mode:'):
     my_bar = st.progress(0)

     ## Data to predict
     randt_index_X = np.random.randint(low=0, high=X_init.shape[0], size=1, dtype=int)
     data2predictArr = X_init[randt_index_X, :]
     data2predictLabel = classes_values[Y_init[randt_index_X][0]-1]
     st.session_state['data2predictArrST'] = data2predictArr
     st.session_state['data2predictLabelST'] = data2predictLabel

     # Progressbar
     for percent_complete in range(100):
        time.sleep(0.0001)
        my_bar.progress(percent_complete + 1)
else:
    pass


##------------------------
## Button Predicting
##------------------------
if st.button('Predicting:'):
     
     ## Prediction
     if st.session_state['data2predictArrST'].size == 4:
          predictionN = new_model.predict(st.session_state['data2predictArrST'])
          st.write(':smile:'*3)
     
          #just for test data
          st.write("The Orig Label is: " + st.session_state['data2predictLabelST'] )
          
          #Plot
          chart_data = pd.DataFrame(
               predictionN.transpose(),
               index=classes_values,
               )

          st.bar_chart(chart_data)
     else:
          st.write('Please try to Collect data again!!!')

     
else:
     st.write('Smelling ...1...2...3:')

##------------------------
## Footnote
##------------------------
st.write('Connect with us')
st.write('Igor Isaev: https://www.linkedin.com/in/igor-isaev/')
st.write('Hazel Wat: https://www.linkedin.com/in/hazelwat/')
