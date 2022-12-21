dataFile=open("input.txt","r")
x=dataFile.readline()
counte=0
countcp=0
countodd=0
countnonp=0
countyesp=0
outputFile=open("output.txt","w")
while x!="":
    x=x.split()
    x[0]=float(x[0])
    if x[0]%2==0:
        outputFile.write("{} has even parity and ".format(int(x[0])))
        counte+=1
    elif int(x[0]) != x[0]:
        outputFile.write("{} cannot have parity and ".format(x[0]))
        countcp+=1
    else:
        outputFile.write("{} has odd parity and ".format(int(x[0])))
        countodd+=1
        
    if x[1] != x[1][::-1]:
        outputFile.write("{} is not a palindrome".format(x[1]))
        countnonp+=1
    else:
        outputFile.write("{} is a palindrome".format(x[1]))
        countyesp+=1
    x=dataFile.readline()
    outputFile.write("\n")
dataFile.close()
outputFile.close()
recordsFile=open("record.txt","w")
x1=int((countodd/(counte + countodd + countcp))*100)
x2=int((counte/(counte + countodd + countcp))*100)
x3=int((countcp/(counte + countodd + countcp))*100)
x4=int((countyesp/(countyesp + countnonp))*100)
x5=int((countnonp/(countyesp + countnonp))*100)
recordsFile.write("""Percentage of odd parity: {}%
Percentage of even parity: {}%
Percentage of no parity: {}%
Percentage of palindrome: {}%
Percentage of non-palindrome: {}%""".format(x1,x2,x3,x4,x5))
recordsFile.close()