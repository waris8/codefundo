import accelerometerCalibrate as accC
import gyroCalibrate as gyroC
import linearAcceleration as lin
import numpy as py
import xlrd
import matplotlib.pyplot as plt 
import math
import zupt

loc = ("/home/waris/Desktop/sensorFusion.xls")
wb = xlrd.open_workbook(loc) 
accelerometer = wb.sheet_by_index(0) 
accelerometer.cell_value(0, 0) 
gyro = wb.sheet_by_index(1) 
gyro.cell_value(0, 0) 
linear = wb.sheet_by_index(2) 
linear.cell_value(0, 0) 

dt = 0.005
# print(float(-6.235))
# gyroangle=py.zeros((gyro.nrows,3))
def filter(dt,gyroData,accData,angle):
	# print(angle.shape)
	# print(gyroData.shape)
	gyroPart = (py.add(angle,(dt*gyroData)))
	# print("zzz")
	# print(gyroPart)
	# print('kkl')
	angle=py.zeros((3,1))
	angle[0][0]=0.99999*float(gyroPart[0][0])+0.00001*float(accData[0][0])
	angle[1][0]=0.83*float(gyroPart[1][0])+0.17*float(accData[1][0])
	# angle[0][0]=float(gyroPart[0][0])
	# angle[1][0]=float(gyroPart[1][0])
	angle[2][0]=float(gyroPart[2][0])
	#angle = py.add(0.98*gyroPart,0.02*accData)
	# print(angle)
	return angle

def toDegree(radian):
	return radian*(180.0/math.pi)

def toRadian(degree):
	return degree*(math.pi/180.0)	

initialAngle = py.zeros((3,1))
initialAngle[0][0]=dt*toDegree(float(gyro.cell_value(1,1)))
initialAngle[1][0]=dt*toDegree(float(gyro.cell_value(1,2)))
initialAngle[2][0]=dt*toDegree(float(gyro.cell_value(1,3)))
# print("kkk")
# print(initialAngle)
# print("kkk")
parameter = accC.calibratedParameter
count = 0
linAcc=py.zeros((gyro.nrows,3))
velocity = py.zeros((gyro.nrows,3))
position = py.zeros((gyro.nrows,3))
eulerAngleList = py.zeros((gyro.nrows,3))
linearAccelerationList=py.zeros((gyro.nrows,3))
# print(eulerAngleList)
accelerometerData = py.zeros((gyro.nrows,2))
eulerAngleList[0]=initialAngle.transpose()
while(count!=gyro.nrows-1):
	gyroData=py.zeros((3,1))
	accRaw=py.ones((4,1))
	gyroData[0][0]=toDegree(gyro.cell_value(count+1,1))
	gyroData[1][0]=toDegree(gyro.cell_value(count+1,2))
	gyroData[2][0]=toDegree(gyro.cell_value(count+1,3))
	accRaw[0][0]=accelerometer.cell_value(count+1,1)
	accRaw[1][0]=accelerometer.cell_value(count+1,2)
	accRaw[2][0]=accelerometer.cell_value(count+1,3)
	accData=accC.calculateAngles(parameter,accRaw.transpose())
	accelerometerData[count][0]=accData[0][0]
	accelerometerData[count][1]=accData[1][0]
	# print("ooo")
	# print(accData)
	# print("ppp")
	# eulerAngleList.append(filter(dt,gyroData,accData,eulerAngleList[count]))
	# print((eulerAngleList[count])[0])
	# print(eulerAngleList[count].shape)
	linAcc[count][0]=linear.cell_value(count+1,1)
	linAcc[count][1]=linear.cell_value(count+1,2)
	linAcc[count][2]=linear.cell_value(count+1,3)
	Angle=py.zeros((3,1))
	Angle[0][0]=(eulerAngleList[count])[0]   #pitch
	Angle[1][0]=(eulerAngleList[count])[1]   #roll
	Angle[2][0]=(eulerAngleList[count])[2]   #yaw
	rotation=lin.rotationMatrix(toRadian(Angle[1][0]),toRadian(Angle[0][0]),toRadian(Angle[2][0]))
	# print(rotation)
	# calibratedAcc=((accRaw.transpose()).dot(parameter)).transpose()
	linearAccelerationList[count]=(lin.inertialFrameAcc(accRaw[0:3,[0]],rotation)).transpose()
	eulerAngleList[count+1]=(filter(dt,gyroData,accData,Angle)).transpose()
	velocity[count+1][0]=velocity[count][0]+(linearAccelerationList[count][0])*dt
	velocity[count+1][1]=velocity[count][1]+(linearAccelerationList[count][1])*dt
	velocity[count+1][2]=velocity[count][2]+(linearAccelerationList[count][2])*dt
	position[count+1][0]=position[count][0]+(velocity[count][0]*dt)+(linearAccelerationList[count][0])*dt*dt
	position[count+1][1]=position[count][1]+(velocity[count][1]*dt)+(linearAccelerationList[count][1])*dt*dt
	position[count+1][2]=position[count][2]+(velocity[count][1]*dt)+(linearAccelerationList[count][2])*dt*dt

	count+=1

# eulerAngles = py.array(eulerAngleList)
# print(eulerAngleList)
eulerX=py.array(eulerAngleList[:,[0]])
eulerY=py.array(eulerAngleList[:,[1]])
eulerZ=py.array(eulerAngleList[:,[2]])
# print(eulerX.shape)
plt.plot(eulerX,'r',eulerY,'b',eulerZ,'g')
# plt.show(block=True)
# print(linearAccelerationList)
# zupt.main(linearAccelerationList,dt)



# plt.plot(linearAccelerationList[:,[0]],'y')
# plt.plot(velocity[:,[0]],'g',velocity[:,[1]],'r',velocity[:,[2]],'b')
# plt.plot(position,'r')
# plt.plot(linAcc[:,[0]],'r')
plt.show(block=True)
	




