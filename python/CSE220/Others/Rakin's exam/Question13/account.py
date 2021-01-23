class Account:
    def __init__(self,accountID,accountBalance:float):
        self.accountID=accountID
        self.accountBalance=accountBalance

    def deposit(self,n):
        if n>0:
            self.accountBalance+=n

    def withdraw(self,n):
        if n>0 and n<=self.accountBalance:
            self.accountBalance-=n

    def fee(self,n):
        if n>=0 and n<=100:
            self.accountBalance*=(100-n)/100

    def getID(self):
        return self.accountID

    def getBalance(self):
        return self.accountBalance