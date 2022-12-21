class StringType:
    def __init__(self):
        self.charList = ""
        self.sign = 0 # 0 - None , 1 - not operation , 
        self.count = 0 # 0 - normal, 1 - binary(exist or don't, not multiple times), 2 - 0-to-infinite, 3 - 1-to-infinite, 4+ - n-4 times (type n+1 in code)
    def __str__(self) -> str:
        returnString= self.charList+" "+str(self.sign)+" "+str(self.count)
        return returnString

def stringCreator(string1):
    string2=""
    if len(string1)==3 and string1[1]=="-":
        for a in range(ord(string1[0]),ord(string1[2])+1):
            string2=string2+chr(a)
    else:
        string2=string1
    return string2

def regex(str,re):
    p1=0 # pointer 1
    restr=[]
    s1=""
    restr.append(StringType())
    while p1<len(re):
        if re[p1]=="[":
            p1+=1
            if re[p1]=="^":
                restr[-1].sign=1
                p1+=1
            p2=p1+1
            while re[p2]!="]":
                p2+=1
            restr[-1].charList=stringCreator(re[p1:p2])
            p1=p2
            
        elif re[p1]=="(":
            p1+=1
            if re[p1]=="^":
                restr[-1].sign=1
                p1+=1
            p2=p1+1
            while re[p2]!=")":
                p2+=1
            restr[-1].charList=stringCreator(re[p1:p2])
            p1=p2
            
        elif re[p1]=="{":
            p1+=1
            p2=p1+1
            while re[p2]!="}":
                p2+=1
            restr[-1].count=int(re[p1:p2])+4
            p1=p2
        else:
            restr[-1].charList=restr[-1].charList+re[p1]
        
        p1+=1
        if p1==len(re):
            print(restr[-1])
            break
        elif re[p1]=="?":
            restr[-1].count=1
        elif re[p1]=="*":
            restr[-1].count=2
        elif re[p1]=="+":
            restr[-1].count=3
        else:
            continue
        p1+=1
        print(restr[-1])
        restr.append(StringType())
    return True

def main():
    listOfFiles=["input1.txt","input2.txt"]
    for a in listOfFiles:    
        listRegex=[]
        listString=[]
        file1=open(a,"r")
        for b in range(2):
            count=int(file1.readline())
            if b==0:
                for c in range(count):
                    listRegex.append(file1.readline().rstrip())
            elif b==1:
                for c in range(count):
                    listString.append(file1.readline().rstrip())
        for d in listString:
            successCount=0
            success="NO"
            for e in listRegex:
                if regex(d,e):
                    successCount+=1
            if successCount!=0:
                success="YES"
            print("{},{}".format(success,successCount))

    #print(listRegex,listString)
main()