    #Read in file
    # While the player still has misses and doesn't want to quit
    #Print the round
    #Print the board
    #Player chooses a spot
    #We check the spot to see if it's a miss/hit/repeat
        #If hit, we put an X on the board
        #if miss, we put an M on the board and increment missesGuess
        #if repeat, we tell the user to pick another spot
    # We check if player has chosen an option to quit the game.
        #If all the boats are hit, player wins
        #If all the misses are used, player loses
        #If quit, game ends

# Read in file
shipLocations(Grid, userName, userInput, missedGuess, shipCords)

# While the player still has misses and doesn't want to quit
while missedGuess != TOTALMISSES and userInput != 'QUIT'

#Print the round
print(f"{'':>8}---------- Round {boardRound} ----------", '\n')

#Print the board
printBoard(BOARDER, Grid)

#Player chooses a spot
playerChoice(userName, Grid, missedGuess, shipCords)

#We check the spot to see if it's a miss/hit/repeat
    #If hit, we put an X on the board
    #if miss, we put an M on the board and increment missesGuess
    #if repeat, we tell the user to pick another spot
checkChoice(userInput, Grid, missedGuess, shipCords)

# We check if player has chosen an option to quit the game.
    #If all the boats are hit, player wins
    #If all the misses are used, player loses
    #If quit, game ends
gameOver(userName, Grid, missedGuess, shipCords)
