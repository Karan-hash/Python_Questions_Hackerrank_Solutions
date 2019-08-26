# https://www.hackerrank.com/challenges/hex-color-code/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# https://www.hackerrank.com/challenges/hex-color-code/forum
import re, sys
[print(j) for i in sys.stdin for j in re.findall('[\s:](#[a-f0-9]{6}|#[a-f0-9]{3})', i, re.I)]

''' Explanation of the code 
It's a regex: [\s:] will match either a space of a colon. That way it filters out the ones right at 
the beginning of the line

[a-f0-9]{6} will match hexes that start with hashtag followed by six hex digis (0-9a-f)
[a-f0-9]{3} Same as above with 3
re.I is to ignore the case. ''' 
# Another method - 
num=int(input())
for i in range(num):
    m=re.findall("(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})(?=[;,)])",input())
    for i in m:
        print(i)