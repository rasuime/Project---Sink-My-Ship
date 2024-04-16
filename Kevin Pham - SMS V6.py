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
    userInput = input(f"{userName}, Please Enter Your Guess (e.g., B7) or type 'quit' To End The Game: ")
    print('')
    print(f"---------- Welcome {userName} to 'Sink My Ship' ----------", '\n')
    print(f"The Goal Of The Game {userName} Is To Shoot & Sink All 5 Ships Around The Board Before You Have Missed All 20 missiles", '\n')
# INITIALIZE VARIABLES
    TOTALMISSES = 20
    missedGuess = 0
    boardRound = 1
    shipsFound = set()
    shipCords = []
    previousChoice = ""
# BOARD INITIALIZE
    BOARDER = '---------------------------------------------'
    Grid = [['A', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['B', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['C', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['D', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['E', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            ['F', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['G', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['H', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['I', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],['J', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
# CALLING FUNCTION WITHIN MAIN
    shipLocations(Grid, userName, userInput, missedGuess, shipCords)
    while missedGuess < TOTALMISSES and playerInput != 'QUIT':
        print(f"{'':>8}---------- Round {boardRound} ----------", '\n')
        printBoard(BOARDER, Grid)
        if checkChoice(userInput, Grid, missedGuess, shipCords) == False:
            #print(f"CHECK CHOICE {missedGuess}")
            missedGuess += 1
            #   print(f"CHECK CHOICE {missedGuess}")
        print('MISSED MISSILES :', missedGuess)
        boardRound += 1
        print('SHIP DESTROYED :')

        userInput = playerChoice(userName, Grid, missedGuess, shipCords)
        if userInput == "QUIT":
            return
        

        
'''        
The purpose of the function of shipLocations is to read in the ship.txt file and convert the document into placeable ships on the board of the game.
The file will be read in as "inf" refering itself as the infile. Once the file is open and read through the there will be a for loop tthat checks to see what ship locations are within the document
Then the ships would be appeneded to another list titled shipLocation which holds all ship locations.
'''    
def shipLocations(Grid, userName, userInput, missedGuess, shipCords):
    #shipCords = []
    try:
        with open('ship.txt', 'r') as inf:
            for line in inf:
                ship = line.strip().split(',')
                shipCords.append(ship)
                for location in ship:
                    if len(location) < 2:
                        continue
                    row = ord(location[0]) - ord('A')
                    col = int(location[1:]) - 1
                    Grid[row][col + 1] = 0
        checkChoice(userInput, Grid, missedGuess, shipCords)
        return Grid
    except FileNotFoundError:   
            print(f"---------- {userName}, Stopping The Game. You Are Mising 'Ships.txt' ----------")

        
'''
The purpose of the function of printBoard is to print the board as the player makes a guess whether the player's guess is correct or incorrect. 
'''
def printBoard(BOARDER, Grid):
    print(BOARDER)
    print('      1   2   3   4   5   6   7   8   9  10')
    print ('')
    for row in Grid:
        s = '| {0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9} | {10} |'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
        print(s)
        #SPACE
        print('')
    print(BOARDER)

    
'''
COMMENT GOES HERE
'''
def playerChoice(userName, Grid, missedGuess, shipCords):
    while True:
        userInput = input(f"{userName}, Please Enter Your Guess (e.g., B7) or type 'quit' To End The Game: ").upper()
        print('')
        if userInput == "QUIT":
            gameOver(userName, Grid, missedGuess, shipCords)
        elif len(userInput) != 2 or userInput[0] not in "ABCDEFGHIJ" or userInput[1] not in "12345678910":
            print(f"{userName}, That Is An Invalid Input. Please Enter A Valid Input Such As A9.")
        else:
            checkChoice(userInput, Grid, missedGuess, shipCords)
            return userInput
        

'''
COMMENT GOES HERE
'''
def checkChoice(userInput, Grid, missedGuess, shipCords):
    row = ord(userInput[0]) - ord('A')
    col = int(userInput[1:]) - 1
    hit = False
    validInput = False
    userInput = ""

    while validInput == False:
        try:
            if Grid[row][col + 1] == 'X' or Grid[row][col + 1] == 'M':
                print('You already hit this spot!')
                userInput = input(f"Please Enter Your Guess (e.g., B7) or type 'quit' To End The Game: ").upper()
            else:
                validInput = True
        except:
             print("Pick a new spot!")

        
    
    for ship in shipCords:
        if userInput in ship:
            print('!!!A Ship Has Been Hit!!!','\n')
            Grid[row][col + 1] = 'X'
            ship.remove(userInput)  # Remove the hit location from the ship
            hit = True
            break  # Exit the loop once a hit is found
        else:
            print("You missed")
            Grid[row][col + 1] = 'M'
            hit = False
    
    return hit
    '''
    try:
        # Check if the spot has already been hit
        if Grid[row][col + 1] == 'X' or Grid[row][col + 1] == 'M':
            print('You already hit this spot!')
            
        
        for ship in shipCords:
            if userInput in ship:
                print('!!!A Ship Has Been Hit!!!','\n')
                Grid[row][col + 1] = 'X'
                ship.remove(userInput)  # Remove the hit location from the ship
                hit = True
                break  # Exit the loop once a hit is found
        if not hit:
            print('!!!You Missed Try Again!!!')
            missedGuess = missedGuess + 1
            Grid[row][col + 1] = 'M'
        return hit
    except:
        print("You've Already Hit This Location Please Try Again")
        return False
    '''
    
'''
COMMENT GOES HERE
'''
def gameOver(userName, Grid, missedGuess, shipCords,):
    print(f"---------- {userName} GAME OVER ----------", '\n')
    print('Final Board:')
    printBoard(BOARDER, Grid)
    
    #Read in file
#While the player still has misses and doesn't want to quit
    #Print the round
    #Print the board
    #Player chooses a spot
    #We check the spot to see if it's a miss/hit/repeat
        #If hit, we put an X on the board
        #if miss, we put an M on the board and increment missesGuess
        #if repeat, we tell the user to pick another spot
    #If all the boats are hit, player wins
    #If all the misses are used, player loses
    #If quit, game ends

    
# CALL FUNCTION OF MAIN
main()
