import findbarcode as fb

barcode_data = fb.find()
if(barcode_data):
	print(type(barcode_data))
else:
	print("no data recognised")
