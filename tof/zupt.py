import numpy as py
# import xlrd
import matplotlib.pyplot as plt 
import integration as intg
import filters as filt
from scipy import signal
import math

threshhold=0.7
fs = 100   #sampling frequency


def driftRate(startVelocity,endVelocity,samples):
	return ((endVelocity-startVelocity)/samples)

def norm(acceleration):
	x = acceleration[0][0]
	y = acceleration[0][1]
	z = acceleration[0][2]
	return math.sqrt(math.pow(x,2)+math.pow(y,2)+math.pow(z,2))

def l2Norm(data):
	newData = py.zeros((data[:,[0]].size,1))
	for i in range(data[:,[0]].size):
		newData[i][0] = norm(data[[i],:])
	return newData	

def setToZero(acceleration,velocity):
	# count = 0
	if acceleration<threshhold:
		# print('verygood')
		velocity[0][0] = 0
		velocity[0][1] = 0
		velocity[0][2] = 0
	# print(velocity)
	return velocity

def driftValue(i,rate):
	return i*rate

def absolute(data):
	newData = py.zeros((data[:,[0]].size,1))
	for i in range(data[:,[0]].size):
		newData[i][0] = abs(data[i][0])
	return newData

def zeroVRegion(acceleration):
	# print len(acceleration)
	output = []
	count = 1
	while count < len(acceleration)-1:
		if acceleration[count] < threshhold:
			# print count
			indices = []
			if acceleration[count-1] > threshhold and acceleration[count+1] < threshhold:
				indices.append(count)
				indices.append(0)
			if acceleration[count-1] < threshhold and acceleration[count+1] > threshhold:
				indices.append(count)
				indices.append(1)
			if len(indices) > 0:
				output.append(indices)
		count += 1
	# print output
	final = []
	# for i in range(len(output)):
	return output	

# def smoothPulse(labels):
	# count = 0
	# cumsum = 0
	# while count < len(labels):
		# if labels[count] == 1:
			# cumsum += 1
			# count += 1
		# else:
			


def integrate(timeInterval, acceleration,region):
	# for i in range(len(acceleration)):
		# if acceleration[i] > threshhold:
	output = py.zeros((len(acceleration),3))
	count = 0
	# while count < len(acceleration):

def basicIntegrate(timeInterval,acceleration,smoothData):
	vel_xRaw = py.cumsum(timeInterval*acceleration[:,[0]])
	print(acceleration[:,[0]].shape)
	# print(len(smoothData))
	label = py.zeros((len(smoothData),1))
	print label.shape
	for i in range(len(smoothData)):
		if(smoothData[i] > threshhold):
			label[i] = 1
		else:
			label[i] = 0
	# plt.plot(label,'b')

	vel_x = py.cumsum(timeInterval*label*acceleration[:,[0]])
	print(vel_x.shape)
	plt.plot(vel_xRaw,'r',vel_x,'g')
	# def advIntegrate():




def main(acceleration,timeInterval):
	velocity = intg.integration(timeInterval,acceleration)
	# plt.plot(velocity[:,[0]],'g',velocity[:,[1]],'r',velocity[:,[2]],'b')
	# plt.plot(velocity[:,[0]],'b')	
	normMatrix = l2Norm(acceleration)
	# plt.plot(normMatrix)
	absoluteData = absolute(filt.butterWorthFilter(normMatrix,0.02,5,'low'))
	# plt.plot(absoluteData,'g')
	smoothenedData = filt.butterWorthFilter(absoluteData,0.01,5,'low')
	smoothenedData = smoothenedData - 0.6
	# plt.plot(smoothenedData,'r')
	# count = 0
	# while count < len(acceleration):
		# if
	# print zeroVRegion(smoothenedData)
	basicIntegrate(timeInterval,acceleration,smoothenedData)
	# for i in range(velocity[:,[0]].size):
		# print(velocity[[i],:])
		# velocity[[i],:] = setToZero(smoothenedData[i][0],velocity[[i],:])
		# print('good')
		# print(velocity[[i],:])
		# velocity[i][0] += 0.3*i*timeInterval
		# velocity[i][1] -= 0.05*i*timeInterval
		# velocity[i][2] -= 0.5*i*timeInterval

	# plt.plot(velocity[:,[0]],'g',velocity[:,[1]],'r',velocity[:,[2]],'b')
	
	# position = intg.integration(timeInterval,velocity)
	# plt.plot(velocity[:,[0]],'r')


	# return velocity	






