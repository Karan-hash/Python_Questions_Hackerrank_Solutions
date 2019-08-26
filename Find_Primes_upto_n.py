from math import *
def isPrime(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True
def find_Primes(n):
    list3 = []
    for i in range(2, n+1):
        if (isPrime(i)==1):
            list3.append(i)
    return list3
n = int(input())
list1 = find_Primes(n)
print(*list1)
