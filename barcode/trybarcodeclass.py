from PiCam import PiCam

barcode_reader = PiCam()
barcode_data = barcode_reader.read()
if(barcode_data):
	print(type(barcode_data))
else:
	print("no data recognised")
