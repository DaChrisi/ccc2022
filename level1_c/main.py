import numpy
import math

file = open("level1_c/level1_5.in")
amount = int(file.readline())
counter=0
for i in range(0,amount):
    board = str(file.readline())
    for j in range(0, len(board)):
        if board[j] == 'C':
            counter = counter +1
            


print(counter)