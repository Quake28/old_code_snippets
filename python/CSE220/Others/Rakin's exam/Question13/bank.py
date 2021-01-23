from account import Account
class Bank:
    def __init__(self,bankName):
        self.accountDict={}
        self.bankName=bankName

    def addAccount(self,account:Account):
        self.accountDict[account.accountID]=account

    def findAccount(self,ID):
        return self.accountDict[ID]