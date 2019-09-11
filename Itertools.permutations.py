from itertools import permutations
# https://www.hackerrank.com/challenges/itertools-permutations/forum
print(permutations(['1', '2', '3'])) # This will print string object 

print(list(permutations(['1', '2', '3'])))

#Print permutation of size 2 
print(list(permutations(['1', '2', '3'], 2)))

# Print permutation of size 3 
print(list(permutations('abc',3)))

# Another method 
s, k = input().strip().split() 
[print(*p, sep = "")for p in list(permutations(sorted(s), int(k)))]

#Another method for print 
print(*[''.join(i) for i in permutations(sorted(s), int(k))], sep='\n')

#Another method for printing  
[print(''.join(i)) for i in permutations(sorted(s), int(k))]

#Without list 
for c in permutations(sorted(s), int(k)):
    print(''.join(c))
# Another Solution 
print('\n'.join([''.join(i) for i in list(permutations(sorted(s), int(k)))]))

#Another method  
for i in list(permutations(sorted(s), int(k))):
    print(*i, sep = "")
# Another method 
permuation_per_list = sorted(list(permutations(sorted(s), int(k))))
for i in range(len(permuation_per_list)):
    for j in range(len(permuation_per_list[i])):
        print(permuation_per_list[i][j], end='')
    print(end="\n")