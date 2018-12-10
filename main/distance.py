import RPi.GPIO as GPIO
import time
#white=1
#black=0
class UV:
	def __init__(self,pingPin,echoPin):
		#self.motor1=Motor(forward=motor1Pin1,backward=motor1Pin2)
		#self.motor2=Motor(forward=motor2Pin1,backward=motor2Pin2)
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		self.pingPin=pingPin
		self.echoPin=echoPin
		GPIO.setup(echoPin,GPIO.IN)
		GPIO.setup(pingPin,GPIO.OUT)
		
	def getDistance(self):
		# set Trigger to HIGH
		GPIO.output(self.pingPin, True)
		 		    # set Trigger after 0.01ms to LOW
		time.sleep(0.00001)
		GPIO.output(self.pingPin, False)
		 
		StartTime = time.time()
		StopTime = time.time()
		 
		# save StartTime
		while GPIO.input(self.echoPin) == 0:
			StartTime = time.time()
		 
		# save time of arrival
		while GPIO.input(self.echoPin) == 1:
			StopTime = time.time()
		 
		# time difference between start and arrival
		TimeElapsed = StopTime - StartTime
		# multiply with the sonic speed (34300 cm/s)
		# and divide by 2, because there and back
		distance = (TimeElapsed * 34300) / 2
		 
		return distance
