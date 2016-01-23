"""
Python 3 code to generate a 4x4 board by Max Li
Copyleft (L) 2016
"""

class Board:
    global board, treasures
    '''board[i][j] is a zero-indexed, 2d list where if at row i and column j there is a treasure,
    board[i][j] = 'T', if there isn't, board[i][j] represents the number of adjacent treasures where
    an adjacent grid position row i1 and column j1 have |i-i1| <= 1 and |j-j1| <= 1 and i != i1
    and j != j1'''
    board = [[0 for i in range(4)] for j in range(4)]
    treasures = set()
    def __init__(self):
        from random import randrange
        while len(treasures) < 9:
            treasures.add(randrange(16))
        for pos in treasures:
            board[pos//4][pos%4] = 'T'
        moves=[[1,1],[1,0],[0,1],[-1,1],[-1,0],[-1,-1],[1,-1],[0,-1]]
        for pos in range(16):
            if board[pos//4][pos%4] != 'T':
                for move in moves:
                    if (0 <= pos//4+move[0] < 4 and 0 <= pos%4+move[1] < 4 and
                        board[pos//4+move[0]][pos%4+move[1]] == 'T'):
                        board[pos//4][pos%4] += 1
                
    def debug(self):
        for row in board:
            print(" ".join(map(str, row)))
            

#TESTING CODE
#
#a = Board()
#a.debug()
