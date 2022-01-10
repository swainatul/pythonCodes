import random

top_range = input("Please select a number : ")

if top_range.isdigit():
    top_range=int(top_range)
    if top_range <= 0:
        print("Please enter a number greater than 0 ")
        quit()
else:
    print("Please enter a valid number next time!")
    quit()

random_number = random.randrange(top_range)

# guessed_number= int(input("Enter the number you think is present: "))
attempt_number=0
while(True):
    attempt_number += 1
    guessed_number = int(input("Enter the number you think is present: "))
    if guessed_number > random_number:
        print("Please select a value lower than you guessed")
        continue
    elif guessed_number < random_number:
        print("Please select a value higher than you guessed")
        continue
    else:
        print("You have Guessed correctly !!!")
        break
print("You have taken "+str(attempt_number)+" attempts")