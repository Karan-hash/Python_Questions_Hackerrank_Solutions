# We can change the string value by following methods - 
# Method 1 - One solution is to convert the string to a list and then change the value.
string = "abracadabra"
l = list(string)
l[5] = 'k'
s1 = ''.join(l)
print(s1)
# Method 2 - String Slicing
string = string[:5] +"k"+string[6:]
print(string)