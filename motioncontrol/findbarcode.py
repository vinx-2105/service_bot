#import sensorcontrol as sc
import motorcontrol2 as mc
#import barcodescanner
from time import sleep
from PiCam import PiCam

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

def find:
	motors=mc.MotorControl(m11,m12,m21,m22)
	i=1
	barcode_reader = PiCam()
	barcode = barcode_reader.read()
	if barcode!=None:
		return barcode
	while i<=distance:
		i=i+1
		print"checking if line"
		self.motors.turmRightHard()
		sleep(0.01)
		self.motors.stop()
		sleep(0.02)
		barcode = barcode_reader.read()
		sleep(0.04)
		if (!barcode):
			continue
		break
	if barcode:
		return barcode
			
	i=1
	while i<=distance:
		i=i+1
		print"checking if line"
		self.motors.turmLeftHard()
		sleep(0.01)
		self.motors.stop()
		sleep(0.02)
		barcode = barcode_reader.read()
		sleep(0.04)
		if (!barcode):
			continue
		break
	if barcode:
		return barcode	
	i=1
	while i<=distance:
		i=i+1
		print"checking if line"
		self.motors.turmRightHard()
		sleep(0.01)
		self.motors.stop()
		sleep(0.02)
		barcode = barcode_reader.read()
		sleep(0.04)
		if (!barcode):
			continue
		break
	if barcode:
		return barcode
	i=1
	while i<=distance:
		i=i+1
		print"checking if line"
		self.motors.turmLeftHard()
		sleep(0.01)
		self.motors.stop()
		sleep(0.02)
		barcode = barcode_reader.read()
		sleep(0.04)
		if (!barcode):
			continue
		break
	if barcode:
		return barcode
	return None
	
	


