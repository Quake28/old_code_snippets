from bank import Bank
from account import Account

def main():
    bank1=Bank("Best Bank Ever")
    users=["AwesomeUser1","AwesomeUser2","AwesomeUser3"]
    bank1.addAccount(Account(users[0],1000))
    bank1.addAccount(Account(users[1],10000))
    bank1.addAccount(Account(users[2],50000))
    for user in users:
        bank1.findAccount(user).deposit(100)
        bank1.findAccount(user).withdraw(200)
    bank1.findAccount(users[1]).fee(30)
    for user in users:
        print(bank1.findAccount(user).getID(),bank1.findAccount(user).getBalance())

main()