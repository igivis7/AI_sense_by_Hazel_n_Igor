import pandas as pd
import numpy as np
import streamlit as st
import time
import tensorflow as tf
from altair.vegalite.v4.schema.core import Header
import altair as alt
import serial
from PIL import Image



##------------------------
## Initialize variables
##------------------------
## from
## https://docs.streamlit.io/library/advanced-features/session-state
if 'data2predictArrST' not in st.session_state:
    st.session_state['data2predictArrST'] = np.array([])


if 'GGS_df' not in st.session_state:
    st.session_state['GGS_df'] = pd.DataFrame([])




## Load into a new model
model_ff = tf.keras.models.load_model("./model_c5_n36d02n24d02_mk1")

N_of_readings = 100 #10Hz=100ms : 10 -> 1sec

classes_values = ['beer',
                  'coffee',
                  'orange']


## Data to predict
test_sample_l = [[2378, 728, 642, 540, 210,  25,  34],
                    [2378,  548, 153, 514, 318 , 25 , 34],
                    [2378,  900, 372, 804, 359,  26,  33]]

test_sample = [2378, 64, 15, 64, 93, 15, 66]



##------------------------
## Page decorations
##------------------------
st.title('Hello World! :sunglasses:')
st.write('Welcome to Portfolio Project - AI Sense. We are Igor Isaev and Hazel Wat, current student at Data Science Retreat, Berlin. Batch 28 (Sept-Dec 2021). We use a machine learning model to detech smells and categorize it.')
st.write('6 Elements are extracted from the gas sensors. They are NO2, C2H5CH, VOC, CO, temperature and humidity. We utilize machine learning models to establish correlation and predict the result. Gas interval are collected at 10s.')


##------------------------
## Button Data reading
##------------------------
if st.button('Read data from sensor:'):
    my_bar = st.progress(0)

    ## collect data to predict
    # N_of_readings = 10 #5Hz=200ms : 10 -> 2sec
    # serial_port = '/dev/ttyACM0' #for linux
    serial_port = '/dev/cu.usbmodem1401' #for mac
    baud_rate = 9600

    GGS_list = []
    init_time = round(time.time(),3)*1000
    percent_complete_counter = 0
    percent_complete = 0

    with serial.Serial(serial_port, baud_rate) as ser:
        for cc1 in range(10):
            line_z = ser.readline();
            line_dec_z = line_z.decode("utf-8")
        while len(GGS_list) < N_of_readings:
            line = ser.readline();
            line_dec = line.decode("utf-8") #ser.readline returns a binary, convert to string
            lst0 = line_dec.split(",")
            lst1 = [int(x) for x in lst0]
            if len(lst1)==6:
                GGS_list += [[int(round(time.time(),3)*1000-init_time)] + lst1]
                percent_complete_counter += 1
                my_bar.progress(int(percent_complete_counter / N_of_readings * 100))
    my_bar.progress(100)  #just for visualization    
    
    st.session_state['GGS_df'] = pd.DataFrame(GGS_list,
                     columns=["time_ms", "NO2", 
                     "C2H5OH", "VOC", "CO",
                      "Temperature", "Humidity"])


else:
    pass

##------------------------
## Button Simulation
##------------------------
if st.button('Get random premeasured test data:'):
    my_bar = st.progress(0)

    ## collect data to predict
    # N_of_readings = 10 #5Hz=200ms : 10 -> 2sec
    serial_port = '/dev/ttyACM0'
    baud_rate = 9600

    GGS_list = []
    rand_sample_ind = np.random.randint(3)
    test_sample = test_sample_l[rand_sample_ind]
    ## Simulations
    ##----------------------------
    time_ms    = np.linspace(start=test_sample[0], stop=test_sample[0]+10000, num=N_of_readings, dtype=int)
    #normal(loc=0.0, scale=1.0, size=None)
    B102NO2    = np.random.normal(loc=test_sample[1], scale=test_sample[1]/30, size=N_of_readings)
    B302C2H5OH = np.random.normal(loc=test_sample[2], scale=test_sample[2]/30, size=N_of_readings)
    B502VOC    = np.random.normal(loc=test_sample[3], scale=test_sample[3]/30, size=N_of_readings)
    B702CO     = np.random.normal(loc=test_sample[4], scale=test_sample[4]/30, size=N_of_readings)
    TdegC      = np.random.normal(loc=test_sample[5], scale=test_sample[5]/30, size=N_of_readings)
    RH         = np.random.normal(loc=test_sample[6], scale=test_sample[6]/30, size=N_of_readings)

    st.session_state['GGS_df'] = pd.DataFrame([time_ms, 
            B102NO2,
            B302C2H5OH,
            B502VOC,
            B702CO,
            TdegC,
            RH], 
            index=["time_ms", "NO2", 
                     "C2H5OH", "VOC", "CO",
                      "Temperature", "Humidity"]).T

    for my_bar_c in range(100):
        time.sleep(0.0001)
        my_bar.progress(my_bar_c+1)
    ##----------------------------

else:
    pass


##------------------------
## Button Predicting
##------------------------
if st.button('Predicting:'):
    # st.write(':thinking_face:'*3) 
    # st.balloons()
    col1, col2 = st.columns(2)
    
    with col1: 
        ## Prediction
        # if data2predictArr.size == 6:
        st.balloons()
        if st.session_state['GGS_df'].shape == (N_of_readings, 7):
            
            data2predictArr = st.session_state['GGS_df'].iloc[:,1:].to_numpy()
            data2predictArr.shape=(data2predictArr.shape[0],6)
            predictionN = model_ff.predict(data2predictArr)
            print(predictionN)
            data2predictArrAver = predictionN.mean(axis=0)
            print(data2predictArrAver)


            predictionN = model_ff.predict(data2predictArr)
            #Plot
            chart_data = pd.DataFrame(
               predictionN.transpose(),
               index=classes_values,
               )
            data = pd.melt(chart_data.reset_index(), id_vars=["index"])
            chart = (
                alt.Chart(data)
                .mark_bar()
                .encode(
                    x=alt.X("value", type="quantitative", title="Probability"),
                    y=alt.Y("index", type="nominal", title="Category"),
                    #color=alt.Color("variable", type="nominal", title=""),
                    order=alt.Order("variable", sort="descending"),
                    ).properties(title='Predictions'
                    ).properties(width=100, height=305)
                )
            st.altair_chart(chart, use_container_width=True)
        else:
            st.write('Please try to Collect data again!!!')
    
    with col2:
        # st.session_state['GGS_df']
        df2plot = st.session_state['GGS_df'].iloc[:,1:7]
        # st.line_chart(df2plot, height=290)
        df2plot = st.session_state['GGS_df'].iloc[:,1:7]
        df2plot2 = pd.melt(df2plot.reset_index(), id_vars=["index"])
        line_chart2 = alt.Chart(df2plot2).mark_line().encode(
            alt.X('index', title='Sample index'),
            alt.Y('value', title='Value'),
            color=alt.Color("variable", type="nominal", title=""),
        ).properties(
            title='Raw Data'
        ).properties(width=400, height=290)

        st.altair_chart(line_chart2)
     
else:
     st.write('Smelling ...1...2...3:')


##------------------------
## Footnote
##------------------------
st.write('Connect with us')
st.write('Igor Isaev: https://www.linkedin.com/in/igor-isaev/')
st.write('Hazel Wat: https://www.linkedin.com/in/hazelwat/')
st.write("Github: https://github.com/igivis7/DRS28_Hazel_n_Igor_portfolio_project")

image=Image.open("pic_20Dec21.jpg")
st.image(image)