import random
from modules.placevalues import top, mid, bot
table = [top, mid, bot]

win = 0
usermode = random.choice(["X", "O"])
pcmode = "X" if usermode == "O" else "O"

def usorpc(person):
    if person == usermode:
        print("You won the game")
    elif person == pcmode:
        print("The computer won the game")

def checklinematch(person):
    global win
    for i in range(0,3):
        if table[0][i] == table[1][i] == table[2][i] == person:
            win += 1
            usorpc(person)
            break
        elif table[i][0] == table[i][1] == table[i][2] == person:
            win += 1
            usorpc(person)
            break
        elif table[0][2-i] == table[1][1] == table[2][i] == person:
            win += 1
            usorpc(person)
            break
        else:
            continue
