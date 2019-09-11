from itertools import product
print(list(product([1,2,3], repeat = 2)))

print(list(product([1,2,3], [3,4])))

A = [[1,2,3],[3,4,5]]
print(list(product(*A)))

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))

#Inputting two lists and finding values 
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
print(*list(product(l1,l2)))