game = True #keeps the game going as long as it is ture
turn = 0 #keeps a track of the turn so that we can identify who is playing
board = [str(x+1) for x in range (9)]
#creates a list consisting of 9 string charachters

def check_valid(move):
    move -= 1
    #-1 on move since lists are from 0 not 1 so any number the user inputs needs to be subtracted
    x = board[move]
    #checks the board spot from the given number
    return x.isnumeric()
    #checks if the string chars are numbers or not

def move_play(move, player_turn, func):
    move -= 1
    global turn
    #global varibales can mess with other modules (files) and can make code slower ao avoid using them
    #instead use class variables or make a mutable list, dict, sets to change the info
    #there are no other modules in this file and theres no plans to add them so creating classes are currently impracticle
    if func == True: #looks at assigned function (checking if valid) and if it returns true it continues
        board[move] = player_turn
        turn += 1 #both keeps a track of the player as doing it anywhere else results in one of the users missing out if their placement is invalid
        turn = turn %2
    else:
        print("\n***INVALID MOVE***\n")

def check_winner(turn): #returns a combination depending on what the user got
        return ((board[0] == turn and board[1] == turn and board[2] == turn) or  # top row
            (board[3] == turn and board[4] == turn and board[5] == turn) or  # middle row
            (board[6] == turn and board[7] == turn and board[8] == turn) or  # bottom row
            (board[0] == turn and board[3] == turn and board[6] == turn) or  # first column
            (board[1] == turn and board[4] == turn and board[7] == turn) or  # second column
            (board[2] == turn and board[5] == turn and board[8] == turn) or  # third column
            (board[0] == turn and board[4] == turn and board[8] == turn) or  # diagonal
            (board[2] == turn and board[4] == turn and board[6] == turn)) #diagonal

def check_full():
    x = (board[0] and board[1] and board[2] and board[3] and board[4] and board[5] and board[6] and board[7] and board[8]) #goes through entire board and collects values (has to be str since board nums created in str)
    return x.isnumeric() #checks if values are nums in str format only works in str not int or list 

while game:
    print(f" {board[0]} {board[1]} {board[2]} \n {board[3]} {board[4]} {board[5]} \n {board[6]} {board[7]} {board[8]} \n")
    #prints board out in the correct format

    move = int(input("chose a number from 1-9: "))
    if turn == 0:
        move_play(move, "x", func=check_valid(move))
    else:
        move_play(move, "o", func=check_valid(move))

    if check_winner("x"):
        print("X won")
        game = False
    elif check_winner("o"):
        print("O won")
        game = False
    elif check_full() == False:
        print("Draw")
        game = False