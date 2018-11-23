import SimpleCV
import time
from SimpleCV import Camera
cam= Camera()
"""default img size (640,480) of image captured
	for cropped images the bottommost is 3 topmost is 1
	"""
def position():
	img=cam.getImage()
	cropped1=img.crop(160,0,320,160)
	cropped2=img.crop(160,160,320,160)
	cropped3=img.crop(160,320,320,160)
	col1=cropped1.meanColor()
	col2=cropped2.meanColor()
	col3=cropped3.meanColor()			#red-->0   green-->1    blue-->2
	if col1[2]<50 and col1[1]<50 and col1[0]<50:
		strip1='black'
	elif col1[0]>180:
		strip1='blue'
		m1=2
	elif col1[1]>180:
		strip1='green'
		m1=1
	elif col1[2]>180:
		strip1='red'
		m1=0
	else:
		m1=0
		strip1='none'
		

	if col2[2]<50 and col2[1]<50 and col2[0]<50:
		strip2='black'
	elif col2[0]>180:
		strip2='blue'
		m2=2
	elif col2[1]>180:
		strip2='green'
		m2=1
	elif col2[2]>180:
		strip2='red'
		m2=0
	else:
		m2=0
		strip2='none'

	if col3[2]<50 and col3[1]<50 and col3[0]<50:
		strip3='black'
	elif col3[0]>180:
		strip3='blue'
		m3=2
	elif col3[1]>180:
		strip3='green'
		m3=1
	elif col3[2]>180:
		strip3='red'
		m3=0
	else:
		m3=0
		strip3='none'
	
	if strip1=='black' or strip2=='black' or strip3=='black':
		return -1
	else:
		return m1*1 + m2*3 + m3*9







