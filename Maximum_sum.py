from itertools import product
n, k = map(int, input().split())
N = (list(map(int, input().split()))[1:] for _ in range(n))
results = map(lambda x: sum(i**2 for i in x)%k, product(*N))
print(max(results))
'''
*N goes through all the values of N. So we can write "*N" instead of "N[0],N[1],...,N[K-1]"

N is different because it is N and not the values of N. In this case we want "N[0],N[1],...,N[K-1]" 
instead of N.
'''
# Alternative for lambda and map above = resul = (sum(no**2 for no in nos ) % k for nos in product(*N))
# print(max(resul))
