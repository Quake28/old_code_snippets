import pickle

file1=open("file1.dat", 'wb')

x=[]
for a in range(65,91):
    x.append(chr(a))
print(x)

pickle.dump(x,file1)
file1.close()

file2=open("file1.dat",'rb')

print(pickle.load(file2))

file2.close()
