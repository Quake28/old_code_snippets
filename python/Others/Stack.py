stack=[""]*5
print(stack)
for a in range (len(stack)):
    stack[a]=chr(65+a)
print(stack)

ptr=len(stack)-1

def write():
    global ptr
    stack[ptr+1]=input("Enter value to be input :")
    ptr+=1

def delete():
    global ptr
    stack[ptr]=""
    ptr-=1

def main():
    b=input("Enter W/w to write and D/d to delete :")
    if ((b=="w")or(b=="W")):
        if(ptr==4):
            print("Stack is full")
        else:
            write()
    elif ((b=="d")or(b=="D")):
        if(ptr==-1):
            print("Stack is empty")
        else:
            delete()
    else:
        print("Invalid input!")
        main()

c=True
while(c):
    main()
    print(stack)
    while(True):
        d=input("Do you want to do more operations of the stack?[y/n] :")
        if(d=="y"):
            c=True
            break
        elif(d=="n"):
            c=False
            break
        else:
            print("Please re-enter correct value")
            continue
print(stack)
