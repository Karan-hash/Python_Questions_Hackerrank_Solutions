# https://scotch.io/bar-talk/5-hottest-vs-code-themes-to-use-in-2019
n = int(input())
list1 = list(map(int, input().strip().split()))
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(sorted(list2)[-2])   
''' Another method ''' 
list1 = [2,3,6,6,5]
max1 = max(list1)
l1 = filter(lambda x: x!=max1, l1) # We are filtering values
print(l1)