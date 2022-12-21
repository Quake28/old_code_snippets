from datetime import datetime 

def transactionStoreToFile(transactions):
    print(transactions)
    file1 = open("transactions.txt","w")
    for a in transactions:
        arr = []
        for b in range(len(transactions[a])):
            arr.append(str(transactions[a][b]))
        file1.write(",".join(arr)+"\n")
    file1.close()


    
# Create a file for storing customers details 
def customerStoreToFile(customers):
    print(customers)
    file1 = open("customers.txt","w")
    # [uid,username,password]
    for a in customers:
        arr = []
        for b in range(len(customers[a])):
            arr.append(str(customers[a][b]))
        file1.write(",".join(arr)+"\n")
    file1.close()


# Create a file for storing admin staff accounts details
def adminStoreToFile(adminStaff):
    print(adminStaff)
    # [uid,username,password]
    file1 = open("adminStaff.txt","w")
    for a in adminStaff:
        arr = []
        for b in range(len(adminStaff[a])):
            arr.append(str(adminStaff[a][b]))
        file1.write(",".join(arr)+"\n")
    file1.close()


# Create a function for deposit operations
def deposit(customers,transactions,uid):
    amount = int(input("Please enter the amount you want to deposit : "))
    tid = "T"+"0"*(8-len(str(len(transactions))))+str(len(transactions))
    # TID, UID, Time, acc type, prev amount, deposit amount with (D), new amount
    transactions[tid] = [tid,uid,datetime.now(),customers[uid][1],customers[uid][5],customers[uid][6],"D"+str(amount),customers[uid][6]+amount]
    customers[uid][6]+=amount
    print("${} deposited into your account {}. TID {}.\nYour current balance is ${}".format(amount,uid,tid,customers[uid][6]))
    return transactions, customers
 

# Create a function for withdrawal operations with savings account
# Create a function for withdrawal operations with current account
def withdrawal(customers,transactions,uid):
    while True:
        amount = int(input("Please enter the amount you want to withdraw : "))
        if amount>=customers[uid][6]:
            print("You do not have the suifficient balance for withdrawing the specified amount.\nPlease try again!")
        elif amount<0:
            print("Please enter a valid amount to withdraw!")
        else:
            break    
    tid = "T"+"0"*(8-len(str(len(transactions))))+str(len(transactions))
    # TID, UID, Time, acc type, prev amount, withdrawal amount with (W), new amount
    transactions[tid] = [tid,uid,datetime.now(),customers[uid][1],customers[uid][5],customers[uid][6],"W"+str(amount),customers[uid][6]-amount]
    customers[uid][6]-=amount
    print("${} withdrawn from your account {}. TID {}.\nYour current balance is ${}".format(amount,uid,tid,customers[uid][6]))
    return transactions, customers

# Create a function for printing the bank statement 
def printStatement(transactions,uid):
    startDate = input("Enter start date ('/' separated, eg. dd/mm/yyyy) : ")
    startDate += " 00:00:00"
    endDate = input("Enter end date ('/' separated, eg. dd/mm/yyyy) : ")
    endDate += " 23:59:59"
    #print(startDate,endDate)
    startDate = datetime.strptime(startDate, '%d/%m/%Y %H:%M:%S')
    endDate = datetime.strptime(endDate, '%d/%m/%Y %H:%M:%S')
    #print(startDate,endDate)
    userTransactions = []
    for a in transactions:
        if transactions[a][1]==uid and transactions[a][2]>=startDate and transactions[a][2]<=endDate :
            userTransactions.append(transactions[a])
    print("Transactions for {}, UID - {},\nFrom date - {:%d/%m/%Y},\nTo date - {:%d/%m/%Y}\nStarting amount - ${}".format(userTransactions[0][3],userTransactions[0][1],startDate,endDate,userTransactions[0][5]))
    for transaction in userTransactions:
        typeOfTransation = "Deposit"
        if transaction[6][0] == "W" : 
            typeOfTransation = "Withdrawal"
        print("Date - {:%d/%m/%Y %H:%M:%S}, {} - ${}, new balance - {}".format(transaction[2],typeOfTransation,transaction[6][1:],transaction[7]))



# Create a function for changing the password
def changePassword(customers,uid): # will also work for staff :D
    x1=""
    x2=""
    x3=""
    while True:
        x1=input("Enter current password : ")
        if x1!=customers[uid][2]:
            print("Password does not match with existing password, please try again!")
        else:
            break
    while True:
        x2=input("Enter new password (type \"C\" to cancel) : ")
        x3=input("Enter new password AGAIN to cofirm : ")
        if x2 == "C":
            print("Password change request cancelled!")
            break
        elif x2==x3:
            customers[uid][2] = x2
            print("Password changed successfully!")
            break
        else:
            print("Passwords do not match,\nPlease try again!")
        print()
    return customers
        
 
# Create a function for adding a new customer current account # Create a function for adding a new customer savings account  
def newCustomer(customers,staffID): # D O N E
    name = input("Enter name for new customer account : ")
    accType = input("Enter type of account to be opened [S/C] : ")
    uid = "C"+"0"*(11-len(str(len(customers))))+str(len(customers)+1)
    password = name[:3]+uid[-5:]
    customers[uid] = [uid,name,password,staffID,datetime.now(),accType,0]
    if accType=="S":
        accType="Savings"
    elif accType=="C":
        accType="Current"
    print("New {} account successfully set up for {}, UID - {}".format(accType,customers[uid][1],customers[uid][0]))
    return customers


#  Create a function for creating a new admin staff account
def newAdminStaff(adminStaff):
    name = input("Enter name for new admin staff account : ")
    uid = "A"+"0"*(11-len(str(len(adminStaff))))+str(len(adminStaff)+1)
    password = name[:3]+uid[-5:]
    adminStaff[uid] = [uid,name,password,datetime.now()]
    print("New Staff Admin account successfully set up for {}, UID - {}".format(adminStaff[uid][1],adminStaff[uid][0]))
    return adminStaff


# Create a function for displaying the account balance 
def balance(customers,uid):
    print("The current balance of the account {} is ${}".format(customers[uid][1],customers[uid][-1]))


# create a function for the customers' menu options:
"""
1- Perform deposit
2- perform withdrawal
3- Print a bank statement
4- Check Balance
5- Change Password
6- Exit
"""
def customerMenu(customers,transactions,uid):
    print("\nHello {},".format(customers[uid][1]))
    while True:
        x = int(input("1- Perform deposit\n2- perform withdrawal\n3- Print a bank statement\n4- Check Balance\n5- Change Password\n6- Exit\n: "))
        if x==1:
            transactions, customers = deposit(customers,transactions,uid)
        elif x==2:
            transactions, customers = withdrawal(customers,transactions,uid)
        elif x==3:            
            printStatement(transactions,uid)
        elif x==4:
            balance(customers,uid)
        elif x==5:
            customers = changePassword(customers,uid)
        elif x==6:
            print("Logging out of Customer account,...")
            break
        else:
            print("Wrong input, please try again.")
        print()
    return customers,transactions


# Create a function for the admin staff's menu options:
"""
1- Add a new customer account
2- Edit customer's info
3- print a bank statement for the customer
4- Change Staff Account password (CUSTOM ADDED)
5- Exit
"""
def adminStaffMenu(adminStaff,customers,transactions,uid):
    print("\nHello {},".format(adminStaff[uid][1]))
    while True:
        x = int(input("1- Add a new customer account\n2- Edit customer's info\n3- Print a bank statement for the customer\n4- Change Staff Account password\n5- Exit\n : "))
        if x==5:
            print("Logging out of Admin Staff account,...")
            break
        elif x<5 and x>0:
            if x==1:
                customers = newCustomer(customers,uid)
            elif x==2:
                customerid = input("Enter customer's UID for changing password : ")
                customers = changePassword(customers,customerid)
            elif x==3:
                customerUid = ""
                while True:
                    customerUid = input("Enter customer UID : ")
                    if customerUid in customers:
                        break
                    print("UID does not exist,\nPlease try again!")
                printStatement(customers,customerUid)
            elif x==4:
                adminStaff = changePassword(adminStaff,uid)
        else:
            print("Wrong input, please try again.")
        print()
    return customers,transactions


# Create a function for the super admin's menu options:
"""
1- Create an admin staff account
2- Create a customer account
3- Edit customer's info
4- Print a bank statement for the customer
5- Exit
"""
def superAdminMenu(superAdmin,adminStaff,customers,transactions,uid):
    print("\nHello {},".format(superAdmin[1]))
    while True:
        x = int(input("1- Create an admin staff account\n2- Create a customer account\n3- Edit customer's info\n4- Print a bank statement for the customer\n5- Exit\n : "))
        if x==5:
            print("Logging out of Super Admin account,...")
            break
        elif x<5 and x>0:
            if x==1:
                adminStaff = newAdminStaff(adminStaff)
            elif x==2:
                customers = newCustomer(customers,uid)
            elif x==3:
                customerid = input("Enter customer's UID for changing password : ")
                customers = changePassword(customers,customerid)
            elif x==4:
                transactions = {
                    "T1":["T1","U1",datetime.strptime("1/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User1","S",0,"D100",100],
                    "T2":["T2","U1",datetime.strptime("2/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User1","S",100,"D100",200],
                    "T3":["T3","U2",datetime.strptime("3/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User2","S",0,"D90",90],
                    "T4":["T4","U2",datetime.strptime("4/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User2","S",90,"D90",180],
                    "T5":["T5","U1",datetime.strptime("5/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User1","S",200,"D100",300],
                    "T6":["T6","U1",datetime.strptime("6/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User1","S",300,"D100",400],
                    "T7":["T7","U3",datetime.strptime("7/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User3","S",0,"D30",30],
                    "T8":["T8","U1",datetime.strptime("8/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User1","S",400,"W100",300],
                    "T9":["T9","U3",datetime.strptime("9/1/2000 00:00:00",'%d/%m/%Y %H:%M:%S'),"User3","S",30,"W10",20]
                }
                customers = {"U1":[]}
                customerUid = ""
                while True:
                    customerUid = input("Enter customer UID : ")
                    if customerUid in customers:
                        break
                    print("UID does not exist,\nPlease try again!")
                printStatement(transactions,customerUid)
        else:
            print("Wrong input, please try again.")
        print()
    
    return adminStaff,customers,transactions


# Create a function for the login menu UI:
"""
1- Customer
2- Admin Staff                                                                                                                                                                                                   
3- Super Admin
4- Exit
"""
def login(superAdmin,adminStaff,customers,transactions):
    while True:
        x = int(input("1- Customer\n2- Admin Staff\n3- Super Admin\n4- Exit\n : "))
        if x==4:
            print("Thank you for using the program.\nExiting,...")
            break
        elif x<4 and x>0:
            while True:
                try:
                    uid = input("Enter User ID : ")
                    password = input("Enter password : ")
                    if x==1:
                        if not customers[uid][2] == password:
                            print("Wrong password, try again!")
                            continue
                        customers,transactions = customerMenu(customers,transactions,uid)
                    elif x==2:
                        if not adminStaff[uid][2] == password:
                            print("Wrong password, try again!")
                            continue
                        adminStaff,customers,transactions = adminStaffMenu(adminStaff,customers,transactions,uid)
                    elif x==3:
                        if not superAdmin[2] == password:
                            print("Wrong password, try again!")
                            continue
                        adminStaff,customers,transactions = superAdminMenu(superAdmin,adminStaff,customers,transactions,superAdmin[0])
                except:
                    print("Invalid input.\nPlease try again.\n")
                break
        else:
            print("Wrong input, please try again.")
        print()
    return superAdmin,adminStaff,customers,transactions



# Finally, write the mother (general) While loop that controls the entire interactive program, functions calls, and conditions
def main():
    # Create the super admin account
    superAdmin = ["S1","Super Admin", "root"] # [uid,username,password] - UID by default should be like this 'S00000000001', but we have 1 superadmin only, so we can do S1
    
    customers = {}
    adminStaff = {}
    transactions = {}
    superAdmin,adminStaff,customers,transactions = login(superAdmin,adminStaff,customers,transactions)

    adminStoreToFile(adminStaff)
    customerStoreToFile(customers)
    transactionStoreToFile(transactions)
    

main()