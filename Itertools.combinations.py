from itertools import combinations
print(list(combinations('12345', 2)))

A = [1,1,3,3,3,6]
print(list(combinations(A, 4)))

# Another method 
str1, k = input().strip().split()

for l in range(1, int(k)+1):
    for j in combinations(sorted(str1), l):
        print(''.join(j))

# Another method 
print(*[''.join(j) for i in range(1, int(k)+1) for j in combinations(sorted(str1), i)], sep='\n')

#Another method 
for i in range(1, int(k)+1):
    print(*list(map(''.join, combinations(sorted(str1), i))), sep='\n')