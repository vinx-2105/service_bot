from gpiozero import Motor


class MotorControl:
	def __init__(self,motor1Pin1,motor1Pin2,motor2Pin1,motor2Pin2):
		self.motor1=Motor(forward=motor1Pin1,backward=motor1Pin2)
		self.motor2=Motor(forward=motor2Pin1,backward=motor2Pin2)

	def moveForward(self):
		self.motor2.forward()
		self.motor1.forward()
	
	def moveBackward(self):
		self.motor2.backward()
		self.motor1.backward()

	def stop(self):
		self.motor1.stop()
		self.motor2.stop()
	
	def turnLeft(self):
		self.motor1.stop()
		self.motor2.forward()

	def turnReft(self):
		self.motor2.stop()
		self.motor1.forward()

	def turnLeftHard(self):
		self.motor1.backward()
		self.motor2.forward()

	def turnReftHard(self):
		self.motor2.backward()
		self.motor1.forward()

