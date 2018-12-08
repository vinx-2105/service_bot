import RPi.GPIO as GPIO

#white=1
#black=0
class Sensors:
	def __init__(self,s1,s2,s3,s4,s5):
		#self.motor1=Motor(forward=motor1Pin1,backward=motor1Pin2)
		#self.motor2=Motor(forward=motor2Pin1,backward=motor2Pin2)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		self.s1=s1
		self.s2=s2
		self.s3=s3
		self.s4=s4
		self.s5=s5
		GPIO.setup(s1,GPIO.IN)
		GPIO.setup(s2,GPIO.IN)
		GPIO.setup(s3,GPIO.IN)
		GPIO.setup(s4,GPIO.IN)
		GPIO.setup(s5,GPIO.IN)
		
	def position(self):
		m1=GPIO.input(self.s1)
		m2=GPIO.input(self.s2)
		m3=GPIO.input(self.s3)			#led off is 1 and led off is white
		m4=GPIO.input(self.s4)
		m5=GPIO.input(self.s5)
		print "sensor outputs:"+str(m1)+" " +str(m2)+" "+str(m3)+" "+str(m4)+" "+str(m5)

		if m1==1 and m4==1 and m2==1 and m3==1 and m5==1:	#T point
			return 100
		
		if m4==1 and m2==1 and m3==1 :	#T point
			return 10

		if m1==1 and m2==1 and m3==1 :	#L and S point
			return 100

		if m4==1 and m5==1 and m3==1 :	#R and S point
			return 100
		if m2==1 :
			return 1
		if m1==1 :
			return 2
		if m4==1 :
			return -1
		if m5==1 :
			return -2
		if m3==1 :
			return 0
		else:
			return 20
	

