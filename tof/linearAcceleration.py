# import accelerometerCalibrate as accC
# import tof.gyroCalibrate as gyroC
# import tof.eulerAnglesWithComplimentry as comp
import numpy as py
import xlrd
import matplotlib.pyplot as plt 
import math

loc = ("/home/waris/Desktop/sensorFusion3.xls")
wb = xlrd.open_workbook(loc) 
accelerometer = wb.sheet_by_index(0) 
accelerometer.cell_value(0, 0) 
gyro = wb.sheet_by_index(1) 
gyro.cell_value(0, 0) 

g_vector = py.array([[0.0],[0.0],[-9.80665]])

def c(x):
	return math.cos(x)

def s(x):
	return math.sin(x)

def rotationMatrix(phi,theta,psi):   #roll,pitch,yaw
	matrix = py.zeros((3,3))
	matrix[0]=[c(psi)*c(theta),(c(psi)*s(phi)*s(theta))-(c(phi)*s(psi)),(s(phi)*s(psi))+(c(phi)*c(psi)*s(theta))]
	matrix[1]=[c(theta)*s(psi),(c(phi)*c(psi))+(s(phi)*s(psi)*s(theta)),(c(phi)*s(psi)*s(theta))-(c(psi)*s(phi))]
	matrix[2]=[-s(theta),c(theta)*s(phi),c(phi)*c(theta)]
	# print(matrix)
	return matrix

def inertialFrameAcc(accData,rotation):
	rotated=rotation.dot(accData)
	# print(rotated)
	# print(g_vector)
	accInertial = py.add(rotated,g_vector)
	#print(accInertial)
	return accInertial

	

