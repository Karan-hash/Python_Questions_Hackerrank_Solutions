# https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=next-challenge&h_v=zen
'''
line 1: straightforward.

There are a couple things to notice.

The first is that each line has a set number of repetitions of '.|.', which are centered, and the rest is filled by '-'.

The second is that the flag is symmetrical, so if you have the top, you have the bottom by reversing it. You only need to work on n // 2 (n is odd and you need the integer div because the remaining line is the "WELCOME" line).

line 2: I generate 2\*i + 1 '.|.', center it, and fill the rest with '-'. That's basically the top part of the output.

line 3: put things together. '\n'.join() should be straightforward. Then, the sequence of strings to join is the pattern described above, the middle 'WELCOME' line, and the pattern reversed.
'''
n, m = map(int, input().split())
# pattern = [('.|.'*(2*i + 1)).center(m,'-') for i in range(n//2)]
# print(pattern)
pattern = []
# This for loop is same as above line of pattern
for i in range(n//2):
    ty = ('.|.'*(2*i + 1)).center(m,'-')
    pattern.append(ty)

print(pattern)
print('\n'.join(pattern + ['WELCOME'.center(m,'-')] + pattern[::-1]))



#Another method 
for i in range(1,n,2):
    print("{}".format('.|.'*i).center(m,'-'))
print("WELCOME".center(m,'-'))
for i in range(n-2,-1,-2):
    print("{}".format('.|.'*i).center(m,'-'))