import sensorcontrol as sc
import motorcontrol2 as mc
from time import sleep

s1=3
s2=5
s3=7
s4=11	#near=12
s5=13
m11=29
m12=33
m21=35
m22=37


motors=mc.MotorControl(m11,m12,m21,m22)
motors.stop()
#motors.moveForward()
#sleep(5)
#motors.turnRightHard()
motors.turnLeftHard()
#motors.moveForward()
#motors.moveBackward()
sleep(5)
#motors.moveForward()
#sleep(0.2)
#i=1
#sum=0
#while i<=40:
#	motors.moveForward()
#	sleep(0.01)
#	motors.stop()
#	sleep(0.04)
	#if pos==10 or pos==100:
	#	sum=sum+1
#	i=i+1
#motors.stop()	
	
				#if end point then break
		#	elif position==2 :
		#		self.motors.turnLeftHard
		#	elif position==1 :
		#		self.motors.turnLeft
		#	elif position==0 :
		#		self.motors.moveForward
		#	elif position==-2 :
		#		self.motors.turnRightHard
		#	elif position==-1 :
		#		self.motors.turnRight
		#	sleep(.1)
		#	self.motors.stop();

