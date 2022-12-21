import task1

if __name__=="__main__":
    printData = task1.mainProcess()
    f2=open("output2.txt","w")
    for a in range(len(printData)):
        dictionary=printData[a]
        x=list(dictionary.keys())[-1]
        outputList=[]
        while x!=1:
            outputList.append(x)
            x=dictionary[x][2]
        outputList=[1]+outputList[::-1]
        for a in outputList:
            f2.write(str(a)+" ")
        f2.write("\n")
    f2.close()
