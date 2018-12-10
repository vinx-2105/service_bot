#arr1 is the directions for current position, arr2 is the directions for new position

#if bot moves back arr is traced from back and L becomes R, R becomes L

def compliment(a):
	if a=='L':
		a='R'
	elif a=='S':
		a='S'
	else:
		a='L'
	return a


def third(a,b):
	if a=='L' and b=='R':
		a='S'
	elif a=='R' and b=='L':
		a='S'
	elif a=='S' and b=='L':
		a='R'
	elif a=='L' and b=='S':
		a='R'
	elif a=='S' and b=='R':
		a='L'
	elif a=='R' and b=='S':
		a='L'
	return a

#this function returns the directions array for one position p1 to position p2, where arr1 is the directions array for position p1 and arr2 is the positions array for position p2

def getDirections(arr1,arr2):
	l1=len(arr1)
	l2=len(arr2)
	print("In getDirections source, arr1:")
	print(arr1)
	print("In getDirections dest, arr2:")
	print(arr2)
	if l1==0:
		print("In getDirections source, output:")
		print(arr2)
		return arr2
	if l2==0:
		l1=l1-1
		finalList=[]
		while l1>=0:
			finalList.append(compliment(arr1[l1]))
			l1=l1-1
		print("In getDirections source, output:")
		print(finalList)
		return finalList 
	print ("sizes"+str(l1)+" "+str(l2)+"\n")
	finalList=[]
	same=0
	while arr1[same]==arr2[same] and same<l1 and same<l2:
		same=same+1
	print ("same chars:"+str(same)+"\n")
	# both arrays have same character till arr[same] ie arr[same] is different for arr1 and arr2
	# we can remove the same part
	# now for the first different element i.e. for arr1[same] and arr2[same] we have to see the values in them
	# for the next just compliment for arr1 and same for arr2
	while(l1-1>same):
		print("1")
		finalList.append(compliment(arr1[l1-1]))
		l1=l1-1
	finalList.append(third(arr1[same] , arr2[same] ))
	i=same+1 
	while(i<l2):
		print("2")
		finalList.append( arr2[i] )
		i=i+1
	print("In getDirections source, output:")
	print(finalList)
	return finalList
def test():
	arr1=['L','L','R','S','R','L']
	#arr2=['L','L','R','R','S','L']
	arr2=['L','R']
	print(getDirections(arr1,arr2))
	 

	





















		
		
