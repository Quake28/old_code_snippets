import random
list_original=[]
for a in range(10):
  list_original.append(random.randint(0,100))
print(list_original)



#Linear Search
yn1=False
inputvalue=int(input("Enter a number to run a search :"))
for b in range(len(list_original)):
  if list_original[b]==inputvalue:
    yn1=True
    break
if yn1:
  print("Found")    
else:
  print("Not found")



#Binary search

#1. Bubble Sort
midvar=0
list_copy=list_original
for c in range(len(list_copy)):
  for d in range(len(list_copy)-1):
    if list_copy[d]>list_copy[d+1]:
      midvar=list_copy[d]
      list_copy[d]=list_copy[d+1]
      list_copy[d+1]=midvar
      
#2. Binary search algorithm

yn2=False
while True:
  centerstage=len(list_copy)%2
  print(list_copy)
  if centerstage==1:
    length=(len(list_copy)//2)+1
    if list_copy[length]==inputvalue:
      yn2=True
      break
    elif list_copy[length]>inputvalue:
      list_copy=list_copy[0:length]
    else:
      list_copy=list_copy[length:len(list_copy)]
  else:
    length=(len(list_copy)//2)
    if list_copy[length]==inputvalue:
      yn2=True
      break
    elif list_copy[length]>inputvalue:
      list_copy=list_copy[0:length]
    else:
      list_copy=list_copy[length:len(list_copy)]
    
if yn2:
  print("Found")    
else:
  print("Not found")
