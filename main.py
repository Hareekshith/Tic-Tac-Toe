import random

from modules import placevalues, wincheck, printboard

print("Welcome to Tic-Tac-Toe! \n\n\n")
print("""TO INPUT A VALUE, IN THE TIC-TAC-TOE BOARD, REFER TO THE FOLLOWING:
1 2 3
4 5 6
7 8 9\n\n""")


enmode = input("Which letter are you playing with? (X or O): ")
usermode = enmode.upper()
pcmode = "X" if usermode == "O" else "O"
usplace = 0
compplace = 0
vac = [1,2,3,4,5,6,7,8,9]

print(f"You are playing with {usermode} and the computer is playing with {pcmode}.")
print("Let's start the game, shall we?")

while len(vac) != 0:
    print()
    printboard.printboard()

    while True:
        try:
            usplace = int(input("Where do you want to person your letter (1-9): "))
        except ValueError:
            print("Please input a number.")
            continue
        if usplace in vac:
            vac.remove(usplace)
            break
    placevalues.placevalues(usplace, usermode)
    while True:
        if len(vac) != 0:
            compplace = random.choice(vac)
        else:
            break
        if  compplace in vac:
            placevalues.placevalues(compplace, pcmode)
            vac.remove(compplace)
            break
        elif compplace not in vac:
            if len(vac) == 0:
                break
    
    wincheck.checklinematch(usermode)
    wincheck.checklinematch(pcmode)

    if len(wincheck.win) == 2:
        printboard.printboard()
        print("GAME OVER")
        break

    else:
        if len(vac) == 0:
            print("\n\n")
            printboard.printboard()
            print("IT IS A DRAW!!!")
            break