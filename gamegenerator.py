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

def randomMove(legalMoves):
    move = -1
    while(move not in legalMoves):
        move = random.randint(0,8)
    return int(move)

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
    print(physicalBoard[6]+"|"+physicalBoard[7]+"|"+physicalBoard[8])



numGames=int(input("How many games would you like to generate?"))
history=[]
for x in range(numGames):
    #initialize empty board
    board = [0,0,0, 0,0,0 ,0,0,0]
    history_onegame=[]
    #begin counting pieces played
    piecesPlayed = 0
    gameOver = False


    while(piecesPlayed<9 and gameOver == False):

        legalMoves = findLegalMoves(board)

        choice = randomMove(legalMoves)

        if(piecesPlayed%2==0):
            board[choice]=1
        else:
            board[choice]=-1
        history_onegame.append(choice)
        piecesPlayed = piecesPlayed + 1
        win = checkWin(board)
        if (win == 1):

            gameOver = True
            history_onegame.insert(0,win)
            history.append(history_onegame)
        elif(win == -1):

            gameOver = True
            history_onegame.insert(0,win)
            history.append(history_onegame)
        elif(piecesPlayed == 9):

            gameOver = True
            history_onegame.insert(0,win)
            history.append(history_onegame)
            
print(history)
f = open("history.txt","w")
for x in history:

    f.write(str(x)+'\n')
f.close()
