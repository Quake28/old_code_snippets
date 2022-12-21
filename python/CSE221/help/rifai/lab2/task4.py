def mergeSort(prev_array):
	if len(prev_array)==1:
		return prev_array
	
	half=int(len(prev_array)/2)
	new_array=[]
	arrayLeft = mergeSort(prev_array[:half])
	arrayRight = mergeSort(prev_array[half:])
	while len(arrayLeft)!=0 and len(arrayRight)!=0:
		if arrayLeft[0]==arrayRight[0]:
			new_array.append(arrayLeft[0])
			arrayLeft.pop(0)
			new_array.append(arrayRight[0])
			arrayRight.pop(0)
		elif arrayLeft[0]<arrayRight[0]:
			new_array.append(arrayLeft[0])
			arrayLeft.pop(0)
		elif arrayRight[0]<arrayLeft[0]:
			new_array.append(arrayRight[0])
			arrayRight.pop(0)
	if len(arrayLeft)==0:
		new_array+=arrayRight
	elif len(arrayRight)==0:
		new_array+=arrayLeft
	return new_array

rfile=open("input4.txt","r")
rdata=rfile.read()
rfile.close()

num=rdata.split()
n=int(num[0])
secondline=num[1:]
array=[]
for i in secondline:
    array.append(int(i))

wfile=open("output4.txt","w")
wdata = mergeSort(array)
for i in wdata:
    wfile.write(str(i))
    wfile.write(" ")
wfile.close()