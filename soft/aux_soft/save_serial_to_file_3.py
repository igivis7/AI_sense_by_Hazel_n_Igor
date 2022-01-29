import serial
from datetime import datetime
import time

data_label = "Ambient_BAG"

sensor_name = "GGSV2"
serial_port = '/dev/ttyACM0'
baud_rate = 9600

write_to_file_path = "./%s_LOG_%s_%s.txt" % (datetime.now().strftime("%Y%m%d_%H%M%S"), sensor_name, data_label)
ser = serial.Serial(serial_port, baud_rate)

output_file = open(write_to_file_path, "w+");
while True:
    line = ser.readline();
    line = line.decode("utf-8") #ser.readline returns a binary, convert to string
    line = str(round(time.time())) + ',' + line
    # time.sleep(1)
    print(line);
    output_file.write(line);