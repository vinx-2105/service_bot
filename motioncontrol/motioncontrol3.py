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
sleep1=0.18
sleep2=0.03

class Control:
	def __init__(self):
		self.sensors=sc.Sensors(s1,s2,s3,s4,s5)
		self.motors=mc.MotorControl(m11,m12,m21,m22)
	#main function
	def __del__(self):
		self.motors.stop()
		#delete self.motors()
	def takeUTurn(self):
		newpos=53
		self.motors.moveForward()
		sleep(1)
		self.motors.stop()
		while newpos!=-1 and newpos!=-2:
			print "taking U turn"
			self.motors.turnRightHard()
			sleep(0.2)
			self.motors.stop()
			sleep(0.1)
			newpos=self.sensors.position()
			print "new position:" +str(newpos)	
		self.motors.stop()
		self.motors.moveForward()

	def move(self, arr):
		index=0
		self.takeUTurn()
		while 1: #index<len(arr)
			position=self.sensors.position()
			#print "arr: " 
			print "index"+str(index)
			newpos=53
			print "position:"+str(position)
			if position==10 or position ==100:
				sleep(0.1)
				i=1
				sum=0
				while i<=50:
					print"checking if line"
					self.motors.moveForward()
					sleep(0.01)
					self.motors.stop()
					sleep(0.03)
					pos=self.sensors.position()
					sleep(0.01)
					if pos==10 or pos==100:
						sum=sum+1
					i=i+1
				if sum<30:
					print "============"
					print "NOT A LINE"
					print "============"
					continue
				#self.motors.turnLeftHard  
				#T point array code here
				#check for end point
			#1st method	#self.motors.moveForward()
			#	sleep(.1)	#hard coded part here
			#	self.motors.stop()
			#	if self.sensors.position()==10 or self.sensors.position()==100 :		# assuming rectangular box at the end point
			#		break;
			#	else:
			#		self.motors.moveBackward()
			#		sleep(.01)	#hard coded part here		#second method
				if index>=len(arr):
					break
				else:
					#print "========== to turn"+str(arr[index])	
					self.motors.moveForward()
					sleep(0.8)
					self.motors.stop()
					sleep(0.1)
					char=arr[index]
					index=index+1
					if(char=='S'):	
									
						while newpos!=1 and newpos!=-1:
							print "====going straight on turn"
							self.motors.moveForward()
							sleep(sleep1)
							self.motors.stop()
							sleep(sleep2)
							newpos=self.sensors.position()
							print "new position:" +str(newpos)
	
						self.motors.stop()
						self.motors.moveForward()
					elif char=='L':
						
						while newpos!=1 and newpos!=2:
							print "=====going left on turn"
							self.motors.turnLeftHard()
							sleep(sleep1)
							self.motors.stop()
							sleep(sleep2)
							newpos=self.sensors.position()
							print "new position:" +str(newpos)
						self.motors.stop()
						self.motors.moveForward()
					elif char=='R':
						
						while newpos!=-1 and newpos!=-2:
							print"====going right on turn"
							self.motors.turnRightHard()
							sleep(sleep1)
							self.motors.stop()
							sleep(sleep2)
							newpos=self.sensors.position()
							print "new position:" +str(newpos)
						
						self.motors.stop()
						sleep(0.4)
						self.motors.moveForward()
					
	
				#if end point then break
			elif position==2 :
				self.motors.turnLeftHard()
			elif position==1 :
				self.motors.turnLeft()
			elif position==0 :
				self.motors.moveForward()
			elif position==-2 :
				self.motors.turnRightHard()
			elif position==-1 :
				self.motors.turnRight()
			sleep(0.07)
			self.motors.stop();
			sleep(0.01)
