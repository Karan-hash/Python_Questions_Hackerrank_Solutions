import os
def solve(s):
    str1 = s.split()
    result = (" ".join(word.capitalize() for word in str1))
    return result
if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = solve(s)
    print(result)

#Another method 
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

#Another method 
import string
str1 = "Karan Kaushal"
print(string.capwords(input(), ' '))