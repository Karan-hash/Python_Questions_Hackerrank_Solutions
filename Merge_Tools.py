# https://www.hackerrank.com/challenges/merge-the-tools/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
str1 = input()
n = int(input())
list1 = []
#for i in range()
#print(list(str1))
list2 = list(str1)
for i in range(0, len(list2), n):
    list1.append(list2[i:i+n])
print(list1)
for i in list1:
    str1 = ""
    for j in range(len(i)):
        if i[j] not in str1:
            str1 +=i[j]
    print(str1)

#Another method - 
str2 = "ABCDEFGHIJKLMNOPQRST"
for part in zip(*[iter(str2)]*n):
    d = dict()
    print(''.join([ d.setdefault(c,c) for c in part if c not in d]))
    '''
    setdefault method returns the key value available in the dictionary and if given key is not available then it will provided default value 
    and adds it to the dictionary. '''
'''
Hi nagacharan. I will try to explain it:

1. iter(s) returns an iterator for S.

2. [iter(s)]*n makes a list of n times the same iterator for s.
Example: [[iter(s)]*3] = ([iter(s), iter(s), iter(s)])
'''

#Another method - 
S = input()
K =int(input())
temp = []
len_temp = 0
for item in S:
    len_temp += 1
    if item not in temp:
        temp.append(item)
    if len_temp == K:
        print (''.join(temp))
        temp = []
        len_temp = 0
#Another method - 
for i in range(0, len(string), k):
    s = ""
    for j in string[i : i + k]:
        if j not in s:
            s += j          
    print(s)