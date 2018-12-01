from time import sleep
from picamera import PiCamera
from io import BytesIO
from pyzbar.pyzbar import decode
from PIL import Image

class picamBarcode:
	def __init__(self):
		pass
    
	def read(self):
		camera = PiCamera()
	
		stream = BytesIO()
		camera.capture(stream, format="jpeg")
		stream.seek(0)
		image = Image.open(stream)
		decoded_image = decode(image)
		camera.close()
		del(camera)
		if decoded_image:
			#returns the value of the data
			#if successful
			return decoded_image[0][0]

		else:
			return None
		
		

