import random
import os
def printHorDiv():
    print ("-------------")
def PrintBoard(board):
    print (" " + board[6] + " " + "|" + " "  + board[7] + " " + "|" + " " + board[8])
    printHorDiv()
    print (" " + board[3] + " " + "|" + " "  + board[4] + " " + "|" + " " + board[5])
    printHorDiv()
    print (" " + board[0] + " " + "|" + " "  + board[1] + " " + "|" + " " + board[2])
def WinCheck (board):
    if (board[0] == board[1] and board[0] == board[2] and not (board[0] ==" ")):
        return True
    elif (board[3] == board[4] and board[3] == board[5] and not (board[3] ==" ")):
        return True
    elif (board[6] == board[7] and board[6] == board[8] and not (board[6] ==" ")):
        return True
    elif (board[0] == board[3] and board[0] == board[6] and not (board[0] ==" ")):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and not (board[1] ==" ")):
       return True
    elif (board[2] == board[5] and board[2] == board[8] and not (board[2] ==" ")):
       return True
    elif (board[0] == board[4] and board[0] == board[8] and not (board[0] ==" ")):
       return True
    elif (board[2] == board[4] and board[2] == board[6] and not (board[2] ==" ")):
       return True
    else:
        return False
def TieChecker(board):
    blankdetector = False
    for i in range (0,9):
        if board[i] == " ":
            blankdetector = True
    return not blankdetector 
def GetPlayerLetter():
    choice = ""
    validchoice = False
    while (not validchoice):
        choice = input("Player 1, please choose your side (x or o):")
        if ((not choice == "x") and (not choice == "o")):
            print ("please check your input and try again")
        else:
            validchoice = True
    return choice
def GetPlayMode():
    choice = ""
    validchoice = False
    while not validchoice:
        choice = input("Would you like to play a player or cpu? (type p or c)")
        if ((not choice == "p") and (not choice == "c")):
            print ("Please check your input and try again")
        else:
            validchoice = True
    return choice

def ComputerMoveFinder(board):
    availablemoves = [i for i, position in enumerate(board) if position == " "]
    return availablemoves
def ComputerCriticalMoveDetector(availablemoves, board, playerletter, computerletter):
    winningmoves = []
    blockingmoves = []
    for possiblemove in availablemoves:
        board[possiblemove] = playerletter
        if WinCheck(board):
            blockingmoves.append(possiblemove)
        board[possiblemove] = computerletter
        if WinCheck(board):
            winningmoves.append(possiblemove)
        board[possiblemove] = " "
    return (winningmoves, blockingmoves)
def NewGame ():
    wincondition = 0
    print ("Please refer to the following input map when making your moves")  
    board = ["1","2","3","4","5","6","7","8","9"]
    PrintBoard(board)
    os.system('clear')
    for i in range(0,9):
        board[i]= " "
    playmode = GetPlayMode()
    playerone = GetPlayerLetter()
    if playerone == "x":
        playertwo = "o"
    else:
        playertwo = "x"
    print ("Player one is " + playerone)
    print ("Player two is " + playertwo)
    currentplayer =  random.randint(1,2)
    if currentplayer == 1:
        print ("Player one is going first")
    else:
        print ("Player two is going first")
    while not WinCheck(board) and not TieChecker(board):
        wincondition = 0
        if currentplayer == 1:
            print (" ")
            print (" ")
            print ("Player one's turn")
            Playerturn(board, playerone)
            currentplayer = 2
            if WinCheck(board):
                wincondition = 1

        elif playmode == "c":
            print (" ")
            print (" ")
            print ("Cpu's turn")
            possiblemoves = ComputerMoveFinder(board)
            critical = ComputerCriticalMoveDetector(possiblemoves, board, playerone, playertwo)
            if critical[0]:
                play = random.choice(critical[0])
            elif critical[1]:
                play = random.choice(critical[1])
            else:
                play = random.choice(possiblemoves)
            board[play] = playertwo
            currentplayer = 1
            if WinCheck(board):
                wincondition = 2
        else:
            print (" ")
            print (" ")
            print ("Player two's turn")
            Playerturn(board, playertwo)
            currentplayer = 1
            if WinCheck(board):
                wincondition = 2
    print (" ")
    print (" ")
    print ("Final state of the game!")
    os.system('clear')
    PrintBoard(board)
    if wincondition == 0:
        print ("Draw game!")
    elif wincondition == 1:
        print ("Player one has won!")
    else:
        print ("Player two has won!")
        


def Playerturn(board, player):
    os.system('clear')
    PrintBoard(board)
    validmove = False
    while not validmove:
        choice = input("Please pick where you would like to place an " + player + " :(1-9)")
        validmove = BoardMoveCheck(choice, board)
        if validmove:
            board[int(choice)-1] = player
    return board


def BoardMoveCheck(number, board):
    if number not in ["1","2","3","4","5","6","7","8","9"]:
        print ("Please pick a number between 1 and 9")
        return False
    elif (board[int(number) - 1] == " "):
        return True
    else:
        print ("Invalid move, please try again")
        return False

    
        

stillplaying = True
while (stillplaying):
    NewGame()
    result = input("Would you like to play again? (y/n)")
    if not result == "y":
        stillplaying = False
