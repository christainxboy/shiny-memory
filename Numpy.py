#David Hernandez
#05/07/2023
#CS 162 HW Week 3

#Here an Array without Numpy
Matrix = [[5,6,7], [8,9,10],[11,12,13]]

print(Matrix)

print("This is everything in the array")
print(Matrix[2][2])

for row in Matrix:
    for Stuff in row:
        pass
        print(Stuff)

import numpy as np

Arraydave = np.array([[5,6,7], [8,9,10],[11,12,13]])
print(" ")
print(Arraydave)
print(Arraydave.shape)
print(" ")

for row in Arraydave:
    for iteam in row:
        print(Stuff)
    #NOw this will print the items in row 1 column 1

print(" ")

print(("This is the iteam in row one collum one: ") + str(Arraydave[1][1]))

#Sum and then print the sum of Axis 1, and Collum 2

SumDave = np.sum([[5,6,7], [8,9,10],[11,12,13]], axis = 0)
print(("This is the sum: ") + str(SumDave[2]))