import sensorcontrol as sc
import motorcontrol2 as mc
from time import sleep

s1
s2
s3
s4
s5
m11
m12
m21
m22

class Control
	def __init__(self):
		self.sensors=sc.Sensors(s1,s2,s3,s4,s5)
		self.motors=mc.MotorControl(m11,m12,m21,m22)

	def move(self):
		
		while 1:
			position=self.sensors.position()
			if position==10 || position =100:
				self.motors.turnLeftHard  #T point array code here
				#check for end point
				#if end point then break
			else if position==2 :
				self.motors.turnLeftHard
			else if position==1 :
				self.motors.turnLeft
			else if position==0 :
				self.motors.moveForward
			else if position==-2:
				self.motors.turnRightHard
			else if position==-1:
				self.motors.turnRight
			
			sleep(.01)
			self.motors.stop();
