import numpy as py
#import random
import xlrd
import matplotlib.pyplot as plt 
#import array
loc = ("/home/waris/Desktop/tof/gyroCalibrate.xls")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

x=[0 for i in range(sheet.nrows-1)]
for i in range(1,sheet.nrows): 
    x[i-1]=sheet.cell_value(i, 1)

bias=py.mean(x)
y=[0 for i in range(sheet.nrows-1)]
for i in range(1,sheet.nrows): 
    y[i-1]=x[i-1]-bias

z=[0 for i in range(sheet.nrows-1)]
for i in range(1,sheet.nrows): 
    z[i-1]=round(y[i-1],4)

# plt.plot(z)
#plt.plot(x)
# plt.show(block=True)
#print(z)    