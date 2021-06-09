
import random
list1=[random.randint(0,100) for a in range(10)]
class keyIndex:
    def __init__(self,listParam):
        self.listx=[a for a in listParam]
    def search(self,item):
        """
        if item in self.listx:
            return True
        """
        for a in self.listx:
            if a==item:
                return True
        return False
    def sort1(self):
        #bubble
        """
        for a in range(len(self.listx)):
            for b in range(len(self.listx)-1):
                if self.listx[b]>self.listx[b+1]:
                    temp=self.listx[b]
                    self.listx[b]=self.listx[b+1]
                    self.listx[b+1]=temp
        """
        #insertion
        """
        for a in range(1,len(self.listx)):
            temp=self.listx[a]
            for b in range(a-1,-1,-1):
                if self.listx[b]<temp:
                    self.listx[b+1]=temp
                    break
                else:
                    self.listx[b+1]=self.listx[b]
                if b==0:
                    self.listx[b]=temp
            #print(self.listx)
        """
        #selection sort
        for a in range(len(self.listx)-1):
            smallest=a
            for b in range(a,len(self.listx)):
                if self.listx[smallest]>self.listx[b]:
                    smallest=b
            temp=self.listx[a]
            self.listx[a]=self.listx[smallest]
            self.listx[smallest]=temp
x=keyIndex(list1)
print(x.listx)
x.sort1()
print(x.listx)

def insertion(hash,hashValue,listHash):
    status=True
    count=hash
    while status:
        if listHash[count]==0:
            listHash[count]=hashValue
            status=False
        count+=1
        if count==len(listHash):
            count=0
        elif count==hash:
            status=False
            print("Hashtable is full")
    
def main(x,listHash):
    listExcl="AEIOUaeiou" # [a for a in range(48,58),65,97,69,101,73,105,79,111,]
    count=0
    summation=0
    for a in x:
        try:
            summation+=int(a)
        except:
            if a not in listExcl:
            summation)%9
    print(value)    count+=1
    value=(count*24+
    insertion(value,x,listHash)
listz=["ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32","ST1E89B8A32"]
listHash=[0 for a in range(10)]
for a in listz:
    main(a,listHash)
print(len(listz))
print(listHash)