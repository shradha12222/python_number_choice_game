import random
from art import logo
print("welcome to number guessing game")
print("i'm thinking of a number between 1 and 100")
level=input("Choose a level of the game [easy or hard ]:")
numbers=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60","61","62","63","64","65","66","67","68","69","70","71","72","73","74","75","76","77","78","79","80","81","82","83","84","85","86","87","88","89","90","91","92","93","94","95","96","97","98","99","100"]
number_random=random.choice(numbers)
print("you have 10 guesses left")
def condition():
    if guess <=number_random:
        print("it is low")
    elif guess>number_random:
        print("it  is  high")
if level == "easy":
    chance=9
    for left in range(chance,0,-1):
        guess=input("make a guess :\t")
        condition()
        if guess == number_random:
            print("you win")
            break
        else:
            print(f"you loss  {left}  chance")
    print("you loss the game and chance")
if level == "hard":
    chance=5
    for right in range(chance,0,-1):
        guess=input("make a guess :\t")
        condition()
        if guess == number_random:
            print("you win")
            break
        else:
            print(f"you loss  {right}  chance")
