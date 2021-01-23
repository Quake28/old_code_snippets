import random
import matplotlib.pyplot as plt

def casino():
    #initializing the variables
    total_money = 10000 #Player starts with 10000 CAD
    num_of_bets = 1000 #We will simulate 1000 bets
    bet_money = 10 # We are playeing 10 CAD every bet
    #initializing the lists to be plotted
    num_of_bet = []
    money = []
    #start with bet #1
    bet=1
    #########################################################################################
    #A loop to iterate over the number of bets
    while bet <= num_of_bets:
        #Generate a random number between 0 - 50
        roll=random.randint(0,50)
        #If the player wins
        if roll!=0 and roll%2==0:
            #update total_money
            total_money+=10
        #If the player lost
        else:
            #update total_money
            total_money-=10
        num_of_bet.append(bet)
        money.append(total_money)
        bet+=1
    #Plot the data
    plt.plot(num_of_bet,money)
    plt.ylabel("Money in player's hand")
    plt.xlabel("Number of bets")
    plt.show()

    # Hypothesis
    if money[-1]<10000:
        print("Yes the hypothesis is true.")
    else:
        print("No the hypothesis is false.")
    #########################################################################################
casino()