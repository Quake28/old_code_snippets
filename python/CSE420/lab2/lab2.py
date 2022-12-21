import readline
import string


file1=open("input.txt","r")
count = int(file1.readline().rstrip())
for a in range(count):
    status=0
    string1 = file1.readline().rstrip()
    if string1[0].isalpha():
        if string1[0:4]=="www.":
            status=1
        else:
            position=0
            for b in enumerate(string1):
                if b[1]=="@":
                    position==b[0]
                    status=2
                    break
        if not string1[-4:]==".com":
            status=0
    if status==1:
        print("Web, {}".format(a+1))
    elif status==2:
        print("Email, {}".format(a+1))
    else:
        print("Invalid, {}".format(a+1))