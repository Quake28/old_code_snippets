# TASK01

# GLOBAL VARIABLE FOR STORING DATA
recordedData = [0, 0, 0, 0, 0]

# METHOD FOR PARITY CHECK
def paritychecker(num):
    decimal = False
    count = 0
    while count < len(num):
        if num[count] == ".":
            decimal = True
        count += 1

    if decimal == True:
        store(2)
        return (num, " cannot have parity and ")
    else:
        num = int(num)
        if num % 2 == 0:
            store(1)
            return (num, " has even parity and ")
        else:
            store(0)
            return (num, " has odd parity and ")


# METHOD FOR STORING THE DATA
def store(index):
    recordedData[index] += 1


# METHOD FOR PALINDROME
def palindrome(word):
    palindrome = True
    n = len(word)
    count = 0
    while count < n / 2:
        if word[count] != word[n - 1 - count]:
            palindrome = False
        count += 1
    if word == "":
        palindrome = False

    if palindrome == True:
        store(3)
        return (word, " is a palindrome")
    else:
        store(4)
        return (word, " is not a palindrome")


# MAIN CODE

# FILE INPUT
inp = open("input.txt", "r")
stored = inp.read()
list1 = stored.split()

# SEPARATING THE LIST INTO WORDS AND NUMBERS
numbers = []
words = []
count = 0
while count < len(list1):
    if count % 2 == 0:
        numbers.append(list1[count])
    else:
        words.append(list1[count])
    count += 1
# print(words, numbers)

# OUTPUT FILE
out = open("output.txt", "w")

# PARITY CHECK AND PALINDROME CHECK
count = 0
outputlist = []
while count < len(words):
    paritylist = list(paritychecker(numbers[count]))
    palindromelist = list(palindrome(words[count]))
    outputlist = paritylist + palindromelist

    # PRINT
    i = 0
    n = len(outputlist)
    while i < n:
        out.write(str(outputlist[i]) + "")
        i += 1
    out.write("\n")
    count += 1

# RECORD FILE
record = open("record.txt", "w")
total = len(list1) / 2
odd = int(recordedData[0] / total * 100 )
even = int(recordedData[1] / total * 100 )
noparity = int(recordedData[2] / total * 100 )
palinDrome = int(recordedData[3] / total * 100 )
notPalindrome = int(recordedData[4] / total * 100 )

record.write("Percentage of odd parity: " + str(odd) + "%" + "\n")
record.write("Percentage of even parity: " + str(even) + "%" + "\n")
record.write("Percentage of no parity: " + str(noparity) + "%" + "\n")
record.write("Percentage of palindrome: " + str(palinDrome) + "%" + "\n")
record.write("Percentage of non-palindrome: " + str(notPalindrome) + "%" + "\n")

# CLOSING FILES
record.close()
inp.close()
out.close()
