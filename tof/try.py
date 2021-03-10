import numpy as py
import xlrd
import matplotlib.pyplot as plt 
import math
from scipy import signal

loc = ("/home/waris/Desktop/sensorFusion.xls")
wb = xlrd.open_workbook(loc) 
accelerometer = wb.sheet_by_index(0) 
accelerometer.cell_value(0, 0) 
gyro = wb.sheet_by_index(1) 
gyro.cell_value(0, 0) 
linear = wb.sheet_by_index(2) 
linear.cell_value(0, 0) 

acceleration = py.zeros((accelerometer.nrows))

fs = 200
fc = 0.3

t = py.arange(200) / fs

for i in range(accelerometer.nrows-1):
	acceleration[i]= accelerometer.cell_value(i,1)

plt.plot(acceleration,'r',label='a')

b, a = signal.butter(1, 0.15, 'low')
output = signal.filtfilt(b, a, acceleration)
plt.plot(output, label='filtered')
plt.legend()
plt.show()
plt.show(block=True)	
