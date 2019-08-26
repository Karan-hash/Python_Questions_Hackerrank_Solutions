from math import *
def isPrime(n):
    if n<=1:
        return False
    else:
        for i in range(2, int(sqrt(n))+1):
            if n%i==0:
                return False
    return True
n = int(input())

if isPrime(n):
    print("True")
else:
    print("False")