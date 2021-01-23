def modded_hangman():
    player1=input("Player 1: Input the secret word\n")
    print("\r"*100)
    for guess in range(20):
        if guess==0:
            print("Player 2: Guess the word input by Player 1")
        player2=input()
        if player2==player1:
            print("You guesssed it! It took you "+str(guess+1)+" times")
            break
        elif player2!=player1 and guess!=19:
            print("Player 2: Guess again")
        else:
            print("Sorry, you ran out of guesses!")


modded_hangman()
