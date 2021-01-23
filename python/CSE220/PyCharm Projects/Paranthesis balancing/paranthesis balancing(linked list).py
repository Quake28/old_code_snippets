class Node:
    def __init__(self,value,next):
        self.value=value
        self.next=next

class Balancing:
    def __init__(self):
        self.stack=None
        self.pos=None

    def push(self,char,posArg):
        self.stack=Node(char,self.stack)
        self.pos=Node(posArg,self.pos)
    def pop(self):
        self.stack=self.stack.next
        self.pos=self.pos.next
    def peek(self):
        return([self.pos.value,self.stack.value])


def main(eqn):
    stackControl=Balancing()
    charCount=0
    opener=["(","[","{"]
    closer=[")","]","}"]
    status=True
    for symbol in eqn:
        charCount+=1
        if symbol not in (opener+closer):
            prev=symbol
            continue
        elif symbol in closer:
            if stackControl.stack is None:
                print("This expression is incorrect")
                print("Error at character #{}. ‘{}‘- not opened.".format(charCount,symbol))
                status=False
                break
            elif (stackControl.peek()[1]=="(" and symbol==")") or  (stackControl.peek()[1]=="[" and symbol=="]") or (stackControl.peek()[1] == "{" and symbol == "}"):
                stackControl.pop()
            else:
                print("The expression is incorrect")
                print("Error at character #{}. ‘{}‘- not closed.".format(stackControl.peek()[0], stackControl.peek()[1]))
                status=False
                break
        elif symbol in opener:
            stackControl.push(symbol,charCount)
    if status:
        print("This expression is correct")



main("1+2*(3/4)")
#This expression is correct.

main("1+2*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
#This expression is NOT correct.
#Error at character #10. ‘{‘- not closed.

main("1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14")
#This expression is correct.

main("1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14")
#This expression is NOT correct.
#Error at character #4. ‘]‘- not opened.
