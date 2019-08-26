# https://stackoverflow.com/questions/34494247/solving-palindromic-triangle-quest-puzzle-in-python
n = int(input())
for i in range(1, n+1):
    print(*list(range(1, i + 1)) + list(range(i-1,0,-1)), sep = None)

    #Another method 
    print(((10**i-1)//9)**2)

#Another method 
arr = []
for i in range(1, n+1):
    arr.append(i)
    print(arr+arr[-2: :-1])