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

# MAIN FUNCTION
def main():
    userName=input("What is your name? ")
    print('')
    print(f"---------- Welcome {userName} to 'Sink My Ship' ----------", '\n')
    print(f"The Goal Of The Game {userName} Is To Shoot & Sink All 5 Ships Around The Board Before You Have Missed All 20 missles", '\n')
# INITIALIZE VARIABLES
    BOARDSIZE = 10
    TOTALMISSES = 20
    missedGuess = 0
    boardround = 0
    shipsFound = set()
    BOARDER = '---------------------------------------------'
    GRID = [['A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['B', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['C', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['E', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             ['F', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['G', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['H', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['I', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['J', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
             ]
# CALLING FUNCTION WITHIN MAIN
    shipLocations(userName)    
    playChoice(userName, shipLocation, shipsFound, missedGuess)
    
    while missedGuess < TOTALMISSES:
        print(f"{'':>8}---------- Round {boardround} ----------", '\n')
        printBoard()
        boardround += 1

        userInput = playChoice(userName)
        if userInput == "QUIT":
            gameOver(userName, shipLocation, shipsFound, missedGuess)
            return
        
'''        
The purpose of the function of shipLocations is to read in the ship.txt file and convert the document into placeable ships on the board of the game.
The file will be read in as "inf" refering itself as the infile. Once the file is open and read through the there will be a for loop tthat checks to see what ship locations are within the document
Then the ships would be appeneded to another list titled shipLocation which holds all ship locations.
'''    
def shipLocations(userName):
    try:
        shipLocation = []
        with open('ship.txt', 'r') as inf:
            for line in inf:
                ship = line.strip()
                ship = ship.split(',')
                shipLocation.append(ship)
        return shipLocation
    except FileNotFoundError:   
            print(f"---------- {userName}, Stopping The Game. You Are Mising 'Ships.txt' ----------")
            gameOver(userName, playChoice)

            
'''
The purpose of the function of printBoard is to print the board as the player makes a guess whether the player's guess is correct or incorrect. 
'''
def printBoard():
    print(BOARDER)
    print('      1   2   3   4   5   6   7   8   9  10')
    print ('')
    for row in GRID:
        s = '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} | {10} |'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        print(s)
        #SPACE
        print('')
    print(BOARDER)

    
'''

'''
def playChoice(userName, shipLocation, shipsFound, missedGuess):
    while True:
        userInput = input(f"{userName}, Please Enter Your Guess (e.g., B7) or type 'quit' To End The Game: ").upper()
        print('')
        if userInput == "QUIT":
            gameOver(userName, shipLocation, shipsFound, missedGuess)
        elif len(userInput) != 2 or userInput[0] not in "ABCDEFGHIJ" or userInput[1] not in "12345678910":
            print(f"{userName}, That Is An Invalid Input. Please Enter A Valid Input Such As A9.")
        else:
            return userInput


'''

'''
def checkChoice(userName, shipLocation, shipsFound, missedGuess):
    Row = ord(userInput[0]) - ord('A')
    Col = int(userInput[1:]) - 1

    if (Row, Col) in misses:
        print(f"{userName}, You Already Have Enter This Positon Before. Please Try A Different Location")
        return "REEPAT", missedGuess
    if (Row, Col) in shipLocation:
        print("HIT")
        shipLocation.remove((Row, Col))
        return "HIT", misses
    else:
        print("MISS")
        misses.append((Row,Col))
        return "MISS", misses

    
'''

'''
def gameOver(userName, shipLocation, shipsFound, missedGuess):
    print('Hello World!')
    exit()
    
# CALL FUNCTION OF MAIN
main()
