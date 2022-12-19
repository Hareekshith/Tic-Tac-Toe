import random
from modules.placevalues import top, mid, bot

win = [0]
usermode = random.choice(["X", "O"])
pcmode = "X" if usermode == "O" else "O"

def usorpc(person):
    if person == usermode:
        print("You won the game")
    elif person == pcmode:
        print("The computer won the game")

def checklinematch(person):
    global win
    if top[0] == top[1] == top[2] == person:
        usorpc(person)
        return win.append(1)
    elif mid[0] == mid[1] == mid[2] == person:
        usorpc(person)
        return win.append(1)
    elif bot[0] == bot[1] == bot[2] == person:
        usorpc(person)
        return win.append(1)
    elif top[0] == mid[0] == bot[0] == person:
        usorpc(person)
        return win.append(1)
    elif top[1] == mid[1] == bot[1] == person:
        usorpc(person)
        return win.append(1)
    elif top[2] == mid[2] == bot[2] == person:
        usorpc(person)
        return win.append(1)
    elif top[0] == mid[1] == bot[2] == person:
        usorpc(person)
        return win.append(1)
    elif top[2] == mid[1] == bot[0] == person:
        usorpc(person)
        return win.append(1)
