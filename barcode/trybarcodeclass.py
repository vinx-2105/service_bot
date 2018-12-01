from picamBarcode import picamBarcode

barcode_reader = picamBarcode()
barcode_data = barcode_reader.read()
if(barcode_data):
	print(barcode_data)
else:
	print("no data recognised")
