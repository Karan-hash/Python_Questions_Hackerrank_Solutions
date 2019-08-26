# Example - Validating_Parsing_Email_Address 
# https://www.programcreek.com/python/example/84216/email.utils
# https://docs.python.org/3/library/email.utils.html
import email.utils
#print(email.utils.parseaddr('DOSHI <DOSHI@hackerrank.com>'))
#print(email.utils.formataddr(('DOSHI','DOSHI@hackerrank.com')))


#Using regex we can check valid email address 
import re
n = int(input())
pattern = r"^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$"
for i in range(n):
    x,y = input().split(" ")
    if re.match(pattern,y):
        print(x,y)

#Another method - 
n = int(input())
for _ in range(n):
    x, y = input().split()
    m = re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$',y)
    if m:
        print(x,y)

#Another method 
import email.utils
import re


username = "[A-Za-z](\w|_|-|\.)"
domain = '[A-Za-z]'
extension = '[A-Za-z]{1,3}'

N= input()

for i in range(int(N)):
    user, mail = email.utils.parseaddr(input())
    reg_ex = username +'+' +'@'+ domain +'+' + '\.'+ extension+"$"
    if bool(re.match(reg_ex,mail)):
        print(email.utils.formataddr((user, mail)))