file1=open("File1.txt","w")
import random
array=[]
print(array)
for i in range(len(array)):
    file1.write(str(array[i]))
    file1.write(",")
file1.write("\n")
for a in range(20):
    array.append(random.randint(0,20))
print(array)
for j in range(len(array)):
    file1.write(str(array[j]))
    file1.write(",")
file1.write("\n")
x=0
for b in range(0,len(array)):
    for c in range(0,len(array)-1):
        if array[c+1]<array[c]:
            x=array[c]
            array[c]=array[c+1]
            array[c+1]=x
print(array)
for k in range(len(array)):
    file1.write(str(array[k]))
    file1.write(",")
file1.write("\n")
file1.close()
