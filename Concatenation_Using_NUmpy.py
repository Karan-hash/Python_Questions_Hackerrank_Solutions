# https://www.hackerrank.com/challenges/np-concatenate/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import numpy

array_1 = numpy.array([1,2,3])
array_2 = numpy.array([4,5,6])
array_3 = numpy.array([7,8,9])

print(numpy.concatenate((array_1, array_2, array_3)))
# Output
# [1 2 3 4 5 6 7 8 9]

# If we have more than 1 dimension we will specify the axix for solving the problem 
array_4 = numpy.array([[1,2,3], [0,0,0]])
array_5 = numpy.array([[0,0,0], [7,8,9]])

print(numpy.concatenate((array_4, array_5), axis = 1)) #Along the first dimension