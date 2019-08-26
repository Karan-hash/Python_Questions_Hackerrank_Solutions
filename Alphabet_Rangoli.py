import string
alphabets = string.ascii_lowercase #All alphabets are stored in the lowercase in the alphabets
n = int(input())
List1 = []
for i in range(n):
    s = "-".join(alphabets[i:n])
    #print(s)
    List1.append(s[::-1] + s[1:])
#print(List1)
width = (4*n - 3)
for i in range(n-1, 0, -1):
    print(List1[i].center(width, "-"))

for i in range(n):
    print(List1[i].center(width, "-"))

""" Another solution
import string
alpha = string.ascii_lowercase

n = int(input())
L = []
for i in range(n):
    s = "-".join(alpha[i:n])
    L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
print('\n'.join(L[:0:-1]+L))
"""
''' Another solution
def print_rangoli(size):
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    for i in list(range(size))[::-1] + list(range(1, size)):
        print('-'.join(alpha[size-1:i:-1] + alpha[i:size]).center(width, '-'))
'''
''' Another solution
import string

alpha = string.ascii_lowercase

num = int(input())

def srange(N):
    return list(range(N))+list(range(N-2,-1,-1))

for i in srange(num):
    print('-'.join([alpha[num-j-1] for j in srange(i+1)]).center(4*(num-1)+1,'-'))
'''