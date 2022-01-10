import random

user_wins= 0
com_wins = 0
games_played = 0
plays = ['rock','paper','scessors']
while True:
    games_played+=1
    user_input = input("Please enter Rock/Paper/Scessors or Q to quit: ").lower()
    if user_input == 'q':
        break

    if user_input not in plays:
        continue

    com_input = random.randint(0,2)
    com_input = plays[com_input]
    print("computer picked",com_input)

    if user_input== com_input:
        print("DRAW. Try again")
        continue
    elif user_input=='rock' and com_input=='scessors':
        print("User Wins !!!")
        user_wins+=1
    elif user_input == 'paper' and com_input == 'rock':
        print("User Wins !!!")
        user_wins += 1
    elif user_input == 'scessors' and com_input == 'paper':
        print("User Wins !!!")
        user_wins += 1
    else:
        print("Computer Wins !!!")
        com_wins+=1
print("number of games played are",games_played)
print("number of games user won",user_wins)
print("number of games computer won",com_wins)
print("Thank you for playing!!!")