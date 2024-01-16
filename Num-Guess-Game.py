import random
randNumber = random.randint(1, 50)
print("Welcome to Num-Guess Game")
print("This game is made by Umang Singh")
name = input("Enter your name : ")
print("Hello ", name)
print("Enter the number betweeen 1 & 50 ")
guess = int(input("You : Guess your Number : "))
print("You - ", guess)
print("Bot - ", randNumber)
if guess == randNumber:
    print('You Won 7.... Crore.......')
else:
    print("You Loose")
exit()
