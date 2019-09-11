from itertools import combinations_with_replacement 
print(list(combinations_with_replacement('12345',2)))

A = [1,1,1,2,3,4,42,3,2,2]
print(list(combinations_with_replacement(A,2)))

#Another method 
import itertools
str1, k = input().strip().split()

print(*list(map(''.join, itertools.combinations_with_replacement(sorted(str1), int(k)))), sep='\n')
