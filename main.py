from data import data
from replit import clear
from Art import logo
from Art import vs
import random
def Game():
    print(logo)
    lose = False
    finalScore = 0
    Acounter = 0
    Bcounter = 0
    while not lose:
        firstParticipant = random.randint(0, 49)
        secondParticipant = random.randint(0, 49)
        while firstParticipant == secondParticipant:
            secondParticipant = random.randint(0, 49)
        print(data[firstParticipant]['follower_count'])
        print(data[secondParticipant]['follower_count'])

        print(f"Compare A: {data[firstParticipant]['name']}, {data[firstParticipant]['description']}, "
              f"from {data[firstParticipant]['country']}")
        print(vs)
        print(f"Against B: {data[secondParticipant]['name']}, {data[secondParticipant]['description']}, "
                  f"from {data[secondParticipant]['country']}")

        comparison = input("Who has more followers? Type 'A' or 'B': ").upper()

        if comparison == 'A' and data[firstParticipant]['follower_count'] > data[secondParticipant]['follower_count']:
            print(f"You are right!")
            Acounter += 1
            clear()

        elif comparison == 'B' and data[firstParticipant]['follower_count'] < data[secondParticipant]['follower_count']:
            print(f"You are right!")
            Bcounter += 1
            clear()
        else:
            print(f"Sorry, that was wrong!")
            print(f"Your final score is {Acounter+Bcounter}")
            lose = True
    NewGame = input("New game? Type 'Y' or 'N': ").upper()
    if NewGame == 'Y':
        Game()
    else:
        print("Have a good day! ")
Game()
