"""
Tic Tac Toe Player
"""

import copy
import math


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        for col in row:
            if col == X:
                x_count += 1
            elif col == O:
                o_count += 1
    return X if x_count == o_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    frontier = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                frontier.append((i,j))
    return frontier


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")
    else:
        New_Board = copy.deepcopy(board) 
        New_Board[action[0]][action[1]] = player(board)
    return New_Board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Review Horizontal Winner
    for i in range(len(board)):
        x_contador = 0
        o_contador = 0
        for j in range(len(board[i])):
            if board[i][j]=="X":
                x_contador += 1
            elif board[i][j]=="O":
                o_contador += 1
            if x_contador==3:
                return "X" 
            elif o_contador==3:
                return "O" 
    # Review Vertical Winner
    for j in range(len(board)):
        x_contador = 0
        o_contador = 0
        for i in range(len(board[j])):
            if board[i][j] == "X":
                x_contador += 1
            elif board[i][j] == "O":
                o_contador += 1
            if x_contador == 3:
                return "X"  
            elif o_contador == 3:
                return "O"  
    # Review Diagonal Winner
    if board[0][0] == board[1][1] and board[2][2]==board[0][0]:
        return board[1][1] 
    elif board[1][1] == board[0][2] and board[1][1] == board[2][0]:
        return board[1][1]  
    else: return None
    

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True 
    elif len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    bestAction=0

    if player(board) == "X":  
        v = -math.inf
        for action in actions(board):
            if v < min_value(result(board,action)):
                v = min_value(result(board,action))
                bestaction = action
        return bestaction
    else:   
        v=math.inf
        for action in actions(board):
            if v > max_value(result(board, action)):
                v = max_value(result(board, action))
                bestAction = action
        return bestAction

def max_value(board):
    v = -100
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board,action)))
    return v


def min_value(board):
    v = 100
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board,action)))
    return v
s=initial_state()