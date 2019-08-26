import math
no = input()
list1 = list(no)
length = len(list1)
sum1 = 0
for i in list1:
    sum1 = sum1 + pow(int(i), length)
print(sum1)
if sum1 == int(no):
    print("Yes it is an armstrong number")
else:
    print("No")