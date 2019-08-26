''' We can Solve this problem by using a property: ** That a median on the hypotenuse divides the 
right angled triangle in two isoceles triangle.** * Means AM=BM=CM * So, ∡MBC = ∡MCB '''
from math import *
n1 = int(input())
n2 = int(input())
print(str(int(round(degrees(atan2(n1,n2)))))+ '°')

#Another method 
a = int(input())
b = int(input())
c = sqrt(a**2 + b**2)
an = acos(b/c)
de = degrees(an)
print(round(de), chr(176), sep='')