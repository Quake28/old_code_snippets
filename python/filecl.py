file1=open("File1.txt","r")
for a in range(3):
    print(file1.readline())
file1.close()
file2=open("File1.txt","r")
print(file2.read())
