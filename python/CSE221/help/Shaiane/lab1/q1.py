# TASK01

recordedData = [0,0,0,0,0]
# METHOD FOR PARITY CHECK
def paritychecker(num):
    decimal = False
    count = 0
    while count < len(num):
        if num[count] == ".":
            decimal = True
        count += 1

    if decimal == True:
        storer(2)
        return (num, " cannot have parity and ")

    else:
        num = int(num)
        if num % 2 == 0:
            storer(1)
            return (num, " has even parity and ")

        else:
            storer(0)
            return (num, " has odd parity and ")
    
                    

# METHOD FOR storer
def storer(index):
    recordedData[index]+=1

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
        storer(3)
        return (word, " is a palindrome")
    else:
        storer(4)
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


inp.close()
out.close()

record = open("record.txt", "w")

record.write("Percentage of odd parity: {}%\n".format(int(100*recordedData[0]/(len(list1)/2))))
record.write("Percentage of even parity: {}%\n".format(int(100*recordedData[1]/(len(list1)/2))))
record.write("Percentage of no parity: {}%\n".format(int(100*recordedData[2]/(len(list1)/2))))
record.write("Percentage of palindrome: {}%\n".format(int(100*recordedData[3]/(len(list1)/2))))
record.write("Percentage of non-palindrome: {}%\n".format(int(100*recordedData[4]/(len(list1)/2))))

record.close()