## KEVIN PHAM
# SMS - Sink My Ship
#

'''
Hello, and welcome to my verison of the game SMS which is short for "Sink My Ship". The purpose of this program
is to run the game of SMS. The player must have a file of "ship.txt" or the game will not run and will recieve an error code.
If the player does have the correct file the game run as programmed. The goal of the player is to hit all of the ships hidden around the board.
Once all ships are hit the player will recieve a message stating that they have won the game other wise if the play quits or misses every shot.
There will be a message stating "Thank you for playing!"
'''

'''

'''

# MAIN FUNCTION
def main():
    userName=input("What is your name? ")
    print('')
    print(f"---------- Welcome {userName} to 'Sink My Ship' ----------", '\n')
    print(f"The Goal Of The Game {userName} Is To Shoot & Sink All 5 Ships Around The Board Before You Have Missed All 20 missles", '\n')
# TOTAL MISS AND INCREMENTING MISSES
    TOTALMISSES = 20
    missedGuess = 0
    boardround = 0

# CALLING FUNCTION WITHIN MAIN
    shipLocations(userName)    
    printBoard()
    playChoice(userName)
    
    while missedGuess < TOTALMISSES:
        print(f"{'':>8}---------- Round {boardround} ----------", '\n')
        printBoard()
        boardround += 1

        userInput = playChoice(userName)
        if userInput == "QUIT":
            gameOver(userName, shipLocation, shipsFound, misses)
            return
        
    
def shipLocations(userName):
    try:
        shipLocation = []
        with open('ship.txt', 'r') as inf:
            for line in inf:
                ship = line.strip()
                ship = ship.split(',')
                shipLocation.append(ship)
        return shipLocations
    except FileNotFoundError:   
            print(f"---------- {userName}, Stopping The Game. You Are Mising 'Ships.txt' ----------")
            gameOver(userName, playChoice)

def printBoard():
    ROW = 10
    COL = 10
    board = [['0' for row in range(ROW)] for col in range(COL)]
    colNum=('    1   2   3   4   5   6   7   8   9   10   ')
    lines=("  -----------------------------------------")
    print(colNum)
    print(lines)
    for i in range(len(board)):
        print(chr(65+i), "| ", end="")
        for j in range(len(board[i])):
            print(board[i][j], end=" | ")
        print("\n  -----------------------------------------")
    #SPACE
    print('')

def playChoice(userName):
    while True:
        userInput = input(f"{userName}, Please Enter Your Guess (e.g., B7) or type 'quit' To End The Game: ").upper()
        print('')
        if userInput == "QUIT":
            gameOver(userName, shipLocation, shipsFound, misses)
        elif len(userInput) != 2 or userInput[0] not in "ABCDEFGHIJ" or userInput[1] not in "12345678910":
            print(f"{userName}, That Is An Invalid Input. Please Enter A Valid Input Such As A9.")
        else:
            return userInput

def checkChoice(userInput, shipLocation, misses):
    Row = ord(userInput[0]) - ord('A')
    Col = int(userInput[1:]) - 1

    if (Row, Col) in misses:
        print(f"{userName}, You Already Have Enter This Positon Before. Please Try A Different Location")
        return "REEPAT", misses
    if (Rol, Col) in shipLocation:
        print("HIT")
        shipLocation.remove((Row, Col))
        return "HIT", misses
    else:
        print("MISS")
        misses.append((Row,Col))
        return "MISS", misses

def gameOver(userName, shipLocation, shipsFound, misses):
    print('Hello World!')
    exit()
    
# CALL FUNCTION OF MAIN
main()
