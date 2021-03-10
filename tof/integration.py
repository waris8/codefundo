import scipy.integrate as it
import numpy as py 
import matplotlib.pyplot as plt 


def integration(timeInterval,signal):
	time = timeInterval*signal[:,[0]].size
	# plt.plot(signal[:,[1]])
	x = py.zeros(signal[:,[0]].size)
	y = py.zeros(signal[:,[0]].size)
	z = py.zeros(signal[:,[0]].size)
	for i in range(x.size):
		x[i]=signal[i][0]
		y[i]=signal[i][1]
		z[i]=signal[i][2]

	# print(x.shape)
	# t = py.linspace(0,time,num = signal[:,[0]].size)
	# print(signal[:,[1]].shape)
	# print(t.shape)
	# plt.plot(it.cumtrapz(x,None,0.005, initial=0.0))
	xPrime = it.cumtrapz(x,None,timeInterval, initial=0.0)
	yPrime = it.cumtrapz(y,None,timeInterval, initial=0.0)
	zPrime = it.cumtrapz(z,None,timeInterval, initial=0.0)
	integrated = py.vstack((xPrime,yPrime,zPrime)).transpose()
	# print(integrated.shape)

	# integrated[:,[0]] = (it.cumtrapz(x,None,timeInterval,initial=0.0))
	# integrated[:,[1]] = it.cumtrapz(y,None,timeInterval, initial=0.0)
	# integrated[:,[2]] = it.cumtrapz(z,None,timeInterval, initial=0.0)

	return integrated