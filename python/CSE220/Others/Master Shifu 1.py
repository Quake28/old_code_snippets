class Parenthesis:
    def __init__(self):
        self.stack=[]
    def peek(self):
        if len(self.stack)>0:
            return self.stack[-1]
        else:
            return None
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        self.stack.pop(-1)

def run(eqn):
    stack=Parenthesis()
    list1=["(","[","{"]
    list2=[")","]","}"]
    status=True
    for a in range(len(eqn)):
        b=eqn[a]
        if b in list1:
            stack.push(a)
        elif b in list2:
            if stack.peek()!=None:
                if (b==list2[0] and eqn[stack.peek()]==list1[0])or(b==list2[1] and eqn[stack.peek()]==list1[1])or(b==list2[2] and eqn[stack.peek()]==list1[2]):
                    stack.pop()
            else:
                status=False
                print("This expression is NOT correct.")
                print("Error at character #{}. ‘{}‘- not opened.".format(a+1,b))
                break
    if stack.peek()!=None:
        status=False
        print("This expression is NOT correct.")
        print("Error at character #{}. ‘{}‘- not closed.".format(stack.peek()+1,eqn[stack.peek()]))
    if status:
        print("This expression is correct.")

##Output 1
#run("1+2*(3/4)")
##This expression is correct.

##Output 2
#run("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
##This expression is NOT correct.
##Error at character # 10. ‘{‘- not closed.

##Output 3 
#run("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
##This expression is correct.

##Output 4
#run("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
##This expression is NOT correct.
##Error at character # 4. ‘]‘- not opened.
