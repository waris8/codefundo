import numpy as py
import math
import openpyxl
#from xlwt import Workbook
import xlrd
import matplotlib.pyplot as plt 
#import array
loc = ("/home/waris/Desktop/tof/accelerometerCalibrate1.xlsx")
wb = xlrd.open_workbook(loc) 
z_down = wb.sheet_by_index(0) 
z_down.cell_value(0, 0)
y_down = wb.sheet_by_index(1) 
y_down.cell_value(0, 0)
x_down = wb.sheet_by_index(2) 
x_down.cell_value(0, 0)
z_up = wb.sheet_by_index(3) 
z_up.cell_value(0, 0)
y_up = wb.sheet_by_index(4) 
y_up.cell_value(0, 0)
x_up = wb.sheet_by_index(5) 
x_up.cell_value(0, 0)

# n1=z_down.nrows
# n2=z_up.nrows
# n3=y_down.nrows
# n4=y_up.nrows
# n5=x_down.nrows
# n6=x_up.nrows
n1=n2=n3=n4=n5=n6=400
n=n1+n2+n3+n4+n5+n6

gValue=9.80665

rawAcc=py.zeros((z_down.nrows,3))
Y = py.zeros((n,3))
W = py.ones((n,4))

for i in range(z_down.nrows):
	rawAcc[i][0]=z_down.cell_value(i, 1)
	rawAcc[i][1]=z_down.cell_value(i, 2)
	rawAcc[i][2]=z_down.cell_value(i, 3)

for i in range(n1):
	Y[i][2]=gValue
	W[i][0]=z_down.cell_value(i, 1)
	W[i][1]=z_down.cell_value(i, 2)
	W[i][2]=z_down.cell_value(i, 3)
	


for i in range(n2):
	Y[i+n1][2]=-gValue
	W[i+n1][0]=z_up.cell_value(i, 1)
	W[i+n1][1]=z_up.cell_value(i, 2)
	W[i+n1][2]=z_up.cell_value(i, 3)

for i in range(n3):
	Y[i+n1+n2][1]=gValue
	W[i+n1+n2][0]=y_down.cell_value(i, 1)
	W[i+n1+n2][1]=y_down.cell_value(i, 2)
	W[i+n1+n2][2]=y_down.cell_value(i, 3)

for i in range(n4):
	Y[i+n1+n2+n3][1]=-gValue
	W[i+n1+n2+n3][0]=y_up.cell_value(i, 1)
	W[i+n1+n2+n3][1]=y_up.cell_value(i, 2)
	W[i+n1+n2+n3][2]=y_up.cell_value(i, 3)


for i in range(n5):
	Y[i+n1+n2+n3+n4][0]=gValue
	W[i+n1+n2+n3+n4][0]=x_down.cell_value(i, 1)
	W[i+n1+n2+n3+n4][1]=x_down.cell_value(i, 2)
	W[i+n1+n2+n3+n4][2]=x_down.cell_value(i, 3)

for i in range(n6):
	Y[i+n1+n2+n3+n4+n5][0]=-gValue
	W[i+n1+n2+n3+n4+n5][0]=x_up.cell_value(i, 1)
	W[i+n1+n2+n3+n4+n5][1]=x_up.cell_value(i, 2)
	W[i+n1+n2+n3+n4+n5][2]=x_up.cell_value(i, 3)

# print(W)
# print('transpose')
# print(W.transpose().dot(W))
inverse = py.linalg.inv((W.transpose()).dot(W))
# print(inverse)
calibratedParameter = (inverse.dot(W.transpose())).dot(Y)
# print('fff')
# print(calibratedParameter)

def calculateAngles(calibratedParameter,accRaw):
	accCalib = accRaw.dot(calibratedParameter)
	eulerAngles = py.zeros((2,1))       #roll and pitch
	eulerAngles[0][0] = math.atan2(accCalib[0][0],accCalib[0][2])*(180/math.pi)   #pitch
	eulerAngles[1][0] = math.atan2(accCalib[0][1],accCalib[0][2])*(180/math.pi)   #roll
	# eulerAngles[2][0] = math.atan2(accCalib[0][0],accCalib[0][1])*(180/math.pi)
	# print(eulerAngles)
	return eulerAngles
	
#newData = py.asarray([[0.0001],[0.001],[9.88065],[1]]).transpose()
# print(calibratedParameter)

# wb = openpyxl.load_workbook(loc)
# sheet = wb.get_sheet_by_name('zDown')

# acceleration = py.zeros((z_down.nrows,3))
# for i in range(z_down.nrows):
	# data = py.ones((1,4))
	# data[0][0] = z_down.cell_value(i,1)
	# data[0][1] = z_down.cell_value(i,2)
	# data[0][2] = z_down.cell_value(i,3)
	# acceleration[i] = data.dot(calibratedParameter)

# plt.plot(acceleration)
# plt.plot(rawAcc)
# plt.show(block=True)	


#print(calculateAngles(calibratedParameter,newData))









