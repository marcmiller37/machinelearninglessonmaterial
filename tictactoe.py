import os
import random
import copy

#X's are 1, O's are -1, empty is 0
#check if 3 in a row has been made
def checkWin(board):
    win = 0
    winningLines = [[0, 1, 2],[3, 4, 5],[6, 7, 8],[0, 3, 6],[1, 4, 7],[2, 5, 8],[0, 4, 8],[2, 4, 6]]
    for x in winningLines:
        if( board[x[0]]==1 and  board[x[1]]==1 and  board[x[2]]==1):
            win = 1
        elif(board[x[0]]==-1 and  board[x[1]]==-1 and  board[x[2]]==-1):
            win = -1
    return win
#find which parts of the array are available
def findLegalMoves(board):
    legalMoves=[]
    for i in range(len(board)):
        if board[i] == 0:
            legalMoves.append(i)
    return legalMoves

#why didn't I use a dictionary
def createBoard(board):
    physicalBoard=[]
    for x in board:
        if x == -1:
            physicalBoard.append('O')
        elif x == 1:
            physicalBoard.append('X')
        elif x == 0:
            physicalBoard.append(" ")

    return physicalBoard
#display board
def printBoard(board):
    physicalBoard = createBoard(board)

    print(physicalBoard[0]+"|"+physicalBoard[1]+"|"+physicalBoard[2])
    print("-+-+-")
    print(physicalBoard[3]+"|"+physicalBoard[4]+"|"+physicalBoard[5])
    print("-+-+-")
    print(physicalBoard[6]+"|"+physicalBoard[7]+"|"+physicalBoard[8]+"\n")
def printHelpBoard():
    print("\nChoose a place to put your piece using the following guide:")
    print("0"+"|"+"1"+"|"+"2")
    print("-+-+-")
    print("3"+"|"+"4"+"|"+"5")
    print("-+-+-")
    print("6"+"|"+"7"+"|"+"8\n")



#initialize empty board
board = [0,0,0, 0,0,0 ,0,0,0]
#begin counting pieces played
piecesPlayed = 0
gameOver = False



while(piecesPlayed<9 and gameOver == False):
    #display empty board
    printBoard(board)
    #find legal moves
    legalMoves = findLegalMoves(board)

    #State which player moves
    if(piecesPlayed%2==0):
        print("Player X's Turn")

    else:
        print("Player O's Turn")

    printHelpBoard()
    choice = -1
    while (choice<0 or choice>9):
        choice = int(input("What is your choice?"))
        if choice not in legalMoves:
            print("Please choose a legal move.")
        elif( choice <0 or choice >9):
            print("Please choose a move in the game.")
    if(piecesPlayed%2==0):
        board[choice]=1
    else:
        board[choice]=-1

    piecesPlayed = piecesPlayed + 1
    win = checkWin(board)
    if (win == 1):
        print("Player X Wins")
        gameOver = True
        printBoard(board)
    elif(win == -1):
        print("Player O Wins")
        gameOver = True
        printBoard(board)
    elif(piecesPlayed == 9):
        print("Game is a draw.")
        gameOver = True
        printBoard(board)
