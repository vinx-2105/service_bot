import SimpleCV
import picamera
cam=picamera.Picamera()
cam.capture('snap1.png')
from SimpleCV import Image
img=Image('snap1.png')
def position():
	crop1=img.crop(60,140,40,200)
	crop2=img.crop(140,140,40,200)
	crop3=img.crop(220,140,40,200)
	crop4=img.crop(300,140,40,200)
	crop5=img.crop(380,140,40,200)
	crop6=img.crop(460,140,40,200)
	crop7=img.crop(540,140,40,200)
	col1=crop1.meanColor()
	col2=crop2.meanColor()
	col3=crop3.meanColor()
	col4=crop4.meanColor()
	col5=crop5.meanColor()
	col6=crop6.meanColor()
	col7=crop7.meanColor()
	m1=-1
	m2=-1
	m3=-1
 	m4=-1
	m5=-1
	m6=-1
	m7=-1
	print col1
	print col2
	print col3
	print col4
	print col5
	print col6		#black=0 and white=1
	print col7
	if col1[2]>200 and col1[1]>200 and col1[0]>200:
		m1=1
	elif col1[2]<50 and col1[1]<50 and col1[0]<50:
		m1=0
	if col2[2]>200 and col2[1]>200 and col2[0]>200:
		m2=1
	elif col2[2]<50 and col2[1]<50 and col2[0]<50:
		m2=0
	if col3[2]>200 and col3[1]>200 and col3[0]>200:
		m3=1
	elif col3[2]<50 and col3[1]<50 and col3[0]<50:
		m3=0
	if col4[2]>200 and col4[1]>200 and col4[0]>200:
		m4=1
	elif col4[2]<50 and col4[1]<50 and col4[0]<50:
		m4=0
	if col5[2]>200 and col5[1]>200 and col5[0]>200:
		m5=1
	elif col5[2]<50 and col5[1]<50 and col5[0]<50:
		m5=0
	if col6[2]>200 and col6[1]>200 and col6[0]>200:
		m6=1
	elif col6[2]<50 and col6[1]<50 and col6[0]<50:
		m6=0
	if col7[2]>200 and col7[1]>200 and col7[0]>200:
		m7=1
	elif col7[2]<50 and col7[1]<50 and col7[0]<50:
		m7=0
	if m1>=0 and m2>=0 and m3>=0 and m4>=0 and m5>=0 and m6>=0 m7>=0
		return m1*1+m2*2+m3*4+m4*8+m5*16+m6*32+m7*64
	else
		return -1 
