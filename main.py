 #Display Art
from art import logo
from game_data import data
import random


def format_data(account):
    """Takes the account data and returns the printable format"""

    account_name = account['name']
    accont_descr = account["description"]
    account_country = account["country"]
    return(f" {account_name}, {accont_descr}, from {account_country}")


def check_answer(guess,a_followers,b_followers):
    """Takes the user guess and follower counts and returns if they go tit right."""
    if a_followers > b_followers:
        return guess == 'a'
    else:
        return guess == 'b'
            
        

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)


#Making the game repeatable.
while game_should_continue:
#Generate a random account
    #Making the account at position B become next the account at position A.
    account_a = account_b
    account_b = random.choice(data)


    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")

    from art import vs
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    #Ask for user guess
    guess = input("Who has more followers? Type 'A' or 'B':").lower()



    #Check if user is correct


    ##Getting follower count for each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']


    is_correct = check_answer(guess, a_follower_count,b_follower_count)

    #Give user feedback on their guess.
    if is_correct:
        score +=1
        print(f"You're right! current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, thats wrong.Final score is: {score}")



    #Tracking the score

    #Making the game repeatable

    #Moving the correct answer to the next round.


    #clear the screen between rounds.