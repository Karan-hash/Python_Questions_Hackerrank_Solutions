marksheet=[]
scorelist = []
n =int(input())
for i in range(n):
    name = input()
    score = float(input())
    marksheet +=[[name, score]]
    scorelist +=[score]
b = sorted(list(set(scorelist)))[1]
for name, no in sorted(marksheet):
    if no == b:
        print(name)

#Another method 
marksheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    marksheet.append([name, score])
b = sorted(list(set([no for name, no in marksheet] )))[1]
print('\n'.join([name for name , no in sorted(marksheet) if no == b]))    

# Another method is dict.fromkeys(parameter is list)
# b = sorted(list(dict.fromkeys(list_name)))[1]