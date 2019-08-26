# http://www.thelearningpoint.net/computer-science/learning-python-programming-and-data-structures/learning-python-programming-and-data-structures--tutorial-13--regular-expression-matching

'''Mobile Number validation criteria:

The first digit should contain number between 7 to 9.
The rest 9 digit can contain any number between 0 to 9.
The mobile number can have 11 digits also by including 0 at the starting.
The mobile number can be of 12 digits also by including 91 at the starting.
''' 
import re 
def isvalid(s1):
     # 1) Begins with 0 or 91 
    # 2) Then contains 7 or 8 or 9. 
    # 3) Then contains 9 digits 
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}$") # I Have put dollar so that length should not be greater than 10
    return Pattern.match(s)
for i in range(0, int(input())):
    s1 = input()
    if(isvalid(s1)):
        print("Valid Number")
    else:
        print("Invalid Number")
# Another solution for line no - 15 = re.compile(r'^[7-9][0-9]{9}$')
# Another solution for line no - 15 = re.match(r"^[789]{1}\d{9}$", line)

''' 
import re

for _ in range(int(input())):
    line = input()
    if re.match(r"^[789]{1}\d{9}$", line):
        print("YES")
    else:
        print("NO")
'''
#Another method 
n = int(input())
for i in range(n):
    try:
        ph = input()
        k = int(ph)

        if (len(k)==10 and (ph[0]=="9" or ph[0]=="8" or ph[0] == "7")):
            print("YES")
        else:
            print("NO")
    except:
        print("NO")

#Another method 
test = int(input())
for i in range(test):
    string  = input()
    if(len(string)==10 and string[0] in ['9', '8', '7'] and string.isnumeric()):
        print("YES")
    else:
        print("NO")