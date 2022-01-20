import serial
from datetime import datetime
import time
import os
from tqdm import tqdm
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



### ALSO delay time.sleep() is added
N_of_readings = 10*60*10 #10Hz 60sec 10min
plot_update_factor = 100 #every 10

label = "lemon"
pathW = '/home/trix_arch/IIVspace/DataSc/DataCamp2021/DSR_B28_work/DSR28_portfolio_project/Measurements_n_Tests/GGS_arduino_readings/GGSv2I_complete/run3_two_sensors/'



###########################################
###########################################
###########################################
serial_port_ACM0 = '/dev/ttyACM0' #must be GGSv2I
serial_port_ACM1 = '/dev/ttyACM1' #must be GGSv2H
baud_rate = 9600

GGS_list_ggsI = []
GGS_list_ggsH = []
init_time = round(time.time(),3)*1000

plt.ion() 
# fig=plt.figure()
fig, axs = plt.subplots(2, 1)
GGS_df_ggsI = pd.DataFrame(GGS_list_ggsI)
GGS_df_ggsH = pd.DataFrame(GGS_list_ggsH)
axs[0].plot(GGS_df_ggsI.iloc[:,1:7])
axs[0].grid()
axs[0].title.set_text('ggsI')
axs[1].plot(GGS_df_ggsH.iloc[:,1:7])
axs[1].grid()
axs[1].title.set_text('ggsH')
plt.show()

# fig, axs = plt.subplots(2)
#     ...: fig.suptitle('Vertically stacked subplots')
#     ...: axs[0].plot(x, y)
#     ...: axs[1].plot(x, -y)


with serial.Serial(serial_port_ACM0, baud_rate) as serACM0:
    with serial.Serial(serial_port_ACM1, baud_rate) as serACM1:
        for cc1 in tqdm(range(10)):
            line_z0 = serACM0.readline();
            line_dec_z0 = line_z0.decode("utf-8")
            line_z1 = serACM1.readline();
            line_dec_z1 = line_z1.decode("utf-8")
            
        while len(GGS_list_ggsI) < N_of_readings:
            line0 = serACM0.readline();
            line_dec0 = line0.decode("utf-8") #serACM0.readline returns a binary, convert to string
            lst00 = line_dec0.split(",")
            lst10 = [int(x) for x in lst00]

            line1 = serACM1.readline();
            line_dec1 = line1.decode("utf-8") #serACM0.readline returns a binary, convert to string
            lst01 = line_dec1.split(",")
            lst11 = [int(x) for x in lst01]

            if len(lst10)==6 and len(lst11)==6:
                GGS_list_ggsI += [[int(round(time.time(),3)*1000-init_time)] + lst10]
                GGS_list_ggsH += [[int(round(time.time(),3)*1000-init_time)] + lst11]

                if len(GGS_list_ggsI)%plot_update_factor==0:
                    GGS_df_ggsI_t = pd.DataFrame(GGS_list_ggsI)
                    GGS_df_ggsH_t = pd.DataFrame(GGS_list_ggsH)
                    axs[0].plot(GGS_df_ggsI_t.iloc[:,1:7])
                    axs[1].plot(GGS_df_ggsH_t.iloc[:,1:7])
                    plt.pause(0.000001) 




GGS_df_ggsI = pd.DataFrame(GGS_list_ggsI, columns=["time_ms", "B102NO2", "B302C2H5OH", "B502VOC", "B702CO", "TdegC", "RH"])
GGS_df_ggsH = pd.DataFrame(GGS_list_ggsH, columns=["time_ms", "B102NO2", "B302C2H5OH", "B502VOC", "B702CO", "TdegC", "RH"])



filename_to_save_ggsI = pathW+"./ggsI_%s_%s.csv" % (label, datetime.now().strftime("%Y%m%d_%H%M%S"))
filename_to_save_ggsH = pathW+"./ggsH_%s_%s.csv" % (label, datetime.now().strftime("%Y%m%d_%H%M%S"))

with open(filename_to_save_ggsI, 'w') as output_file_ggsI:
    GGS_df_ggsI.to_csv(output_file_ggsI, index=False)
    print("Saved to file: " + filename_to_save_ggsI)
    print("Under the path: " + pathW)

with open(filename_to_save_ggsH, 'w') as output_file_ggsH:
    GGS_df_ggsH.to_csv(output_file_ggsH, index=False)
    print("Saved to file: " + filename_to_save_ggsH)
    print("Under the path: " + pathW)



plt.close()
fig, axs = plt.subplots(2, 1)
GGS_df_ggsI = pd.DataFrame(GGS_list_ggsI)
GGS_df_ggsH = pd.DataFrame(GGS_list_ggsH)
axs[0].plot(GGS_df_ggsI.iloc[:,1:7])
axs[0].grid()
axs[0].legend(GGS_df_ggsI.iloc[:,1:7].columns.to_list())
axs[1].title.set_text('ggsI')
axs[1].plot(GGS_df_ggsH.iloc[:,1:7])
axs[1].grid()
axs[1].legend(GGS_df_ggsH.iloc[:,1:7].columns.to_list())
axs[1].title.set_text('ggsH')
plt.show()
plt.show(block=True)
# plt.show()