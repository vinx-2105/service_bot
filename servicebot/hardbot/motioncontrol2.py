import sensorcontrol as sc
import motorcontrol2 as mc
from time import sleep

s1=3
s2=5
s3=7
s4=11	#near=12
s5=13
m11=15
m12=19
m21=21
m22=23

class Control:
	def __init__(self):
		self.sensors=sc.Sensors(s1,s2,s3,s4,s5)
		self.motors=mc.MotorControl(m11,m12,m21,m22)
	#main function
	def move(self, arr):
		index=0
		while 1: #index<len(arr)
			position=self.sensors.position()
			print "position:"+str(position)
			if position==10 or position ==100:
				
				#self.motors.turnLeftHard  
				#T point array code here
				#check for end point
				self.motors.moveForward()
				sleep(.01)	#hard coded part here
				self.motors.stop()
				if self.sensors.position()==10 or self.sensors.position()==100 :		# assuming rectangular box at the end point
					break
				else:
					self.motors.moveBackward()
					sleep(.01)	#hard coded part here
					self.motors.stop()
					char=arr[index]
					index=index+1
					if(char==F):
						self.motors.moveForward
					elif char==L:
						while self.sensors.position()!=0 :
							self.motors.turnLeftHard()
						self.motors.stop()
						self.motors.moveForward()
					elif char==R:
						while self.sensors.position()!=0 :
							self.motors.turnRightHard()
						self.motors.stop()
						self.motors.moveForward()
					
	
				#if end point then break
			elif position==2 :
				self.motors.turnLeftHard
			elif position==1 :
				self.motors.turnLeft
			elif position==0 :
				self.motors.moveForward
			elif position==-2 :
				self.motors.turnRightHard
			elif position==-1 :
				self.motors.turnRight
			sleep(.01)
			self.motors.stop()
