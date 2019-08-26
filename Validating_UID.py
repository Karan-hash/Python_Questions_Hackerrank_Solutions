# https://www.hackerrank.com/challenges/validating-uid/problem?h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_r%5B%5D=next-challenge&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_v%5B%5D=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
def verify(str1):
    result = "Valid"
    if len(str1)!=10:
        result = "Invalid"
        return result
    count_upper = 0
    for ch in str1:
        if ch.isupper():
            count_upper +=1
        if count_upper>=2:
            break
    if count_upper<2:
        result = "Invalid"
        return result 
    if str1.isalnum():
        None 
    else:
        result = "Invalid"
        return result
    count_digit = 0
    for ch in str1:
        if ch.isnumeric():
            count_digit += 1
        if count_digit>=3:
            break 
    if count_digit<3:
        result = "Invalid"
        return result
    set1 = set(str1)
    if len(set1)!=10:
        result = "Invalid"
        return result
    return result
    

for _ in range(int(input())):
    str1 = input() 
    print(verify(str1))

#Another method 
import re
def valid_UID(s):
    if len(s)!=10:
        return 'Invalid'
    else:
        if not re.search(r'.*[A-Z].*[A-Z].*', s): #Contain atleast 2 uppercase letters
            return 'Invalid'
        if not re.search(r'.*\d.*\d.*\d.*',s): #Contain atleast 3 digits
            return 'Invalid'
        if not re.search(r'[a-zA-Z\d]{10}', s): #Contain digit, characters
            return 'Invalid'
        if re.search(r'(.).*\1',s): #Checking string contain only 1 character each
            return 'Invalid'
        return 'Valid'

for _ in range(int(input())):
    s = input()
    print(valid_UID(s)) 

#Another Solution 
import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')