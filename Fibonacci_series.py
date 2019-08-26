def fibonac(n):
    if n<=1:
        return n 
    else:
        return (fibonac(n-1) + fibonac(n-2))
n = int(input()) 
list1 = [None]*n
if n<=0:
    print("Please enter a positive integer")
else:
    for i in range(n):
        list1[i] = fibonac(i)
print(*list1)