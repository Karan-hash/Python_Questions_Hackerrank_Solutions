# https://www.hackerrank.com/challenges/maximize-it/forum
K, M = [int(x) for x in input().split()]
arrayN = []
for _ in range(K):
    arrayN.append([int(x) for x in input().split()][1:])
from itertools import *
possible_combination =list(product(*arrayN)) #Product is used to all possible combinations of list
# print(possible_combination)
def func(nums):
    return sum(x**2 for x in nums)%M
print(max(list(map(func, possible_combination))))

# https://www.geeksforgeeks.org/iterator-functions-python-set-2islice-starmap-tee/