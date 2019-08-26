# https://www.hackerrank.com/challenges/string-validators/problem
str1 = input()
print (any(c.isalnum()  for c in str1))
print (any(c.isalpha() for c in str1))
print (any(c.isdigit() for c in str1))
print (any(c.islower() for c in str1))
print (any(c.isupper() for c in str1))

#Another method 
type1 = type(str1)
for method in [type1.isalnum, type1.isalpha, type1.isdigit, type1.islower, type1.isupper]:
    print(any(method(c) for c in str1) )

# String Validators another method
print(any(map(str.isalnum, str1)))
print(any(map(str.isalpha, str1)))
print(any(map(str.isdigit, str1)))
print(any(map(str.islower, str1)))
print(any(map(str.isupper, str1)))

# Another method using eval
func = [".isalnum()", ".isalpha()",".isdigit()",".islower()",".isupper()"]
for i in func:
    eval ("print( (any(char" + i + " for char in str1))")