#=========================== NODE CLASS ============================
class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next

#========================== FUNCTION CODE ============================

#TASK01
def factorial(n):
    if (n == 1):
        return n
    else:
        return (n * factorial(n - 1))

#TASK02
def fibonacci_series(count, firstTerm = 0, summation = 1):
    if (count == 0):
        return summation
    elif (count == 1):
        return summation
    else:
        return (fibonacci_series(count - 1, firstTerm = summation, summation = firstTerm + summation))
    
#TASK03
def print_elements(source, count = 0):
    if (len(source) == count):
        return ""
    else:
        print (source[count])
        print_elements(source, count + 1)

#TASK04
def decimal_to_binary(decimal_number, binary = ""):
    if (decimal_number == 0):
        return binary[::-1]

    else:
        if (decimal_number % 2 == 0) :
            binary += "0"
        else:
            binary += "1"
            
        decimal_number = int(decimal_number/2)
        return (decimal_to_binary(decimal_number, binary))

#TASK05
def exponential(base, power):
    if (power == 0):
        return 1
    else:
        return (base * exponential(base, power - 1))

#TASK06
def summation(head):
    if head.next == None:
        return head.element
    else:
        return (head.element + summation(head.next))

#TASK07
def reversed_order(head):
    if head.next == None:
        return str(head.element)
    else:
        return reversed_order(head.next)+"\n"+str(head.element)

    
#=========================== TESTER CODE =============================
print (factorial(5))
print (fibonacci_series(6))
print_elements([10, 20, 30, 40, 50])
print (decimal_to_binary(4))
print (exponential(5, 4))

list01 = Node(60, Node(70, Node(80, Node(90, Node(100))))) 
print (summation(list01))
print (reversed_order(list01))