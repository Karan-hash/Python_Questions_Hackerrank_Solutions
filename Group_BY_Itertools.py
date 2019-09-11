'''     
Here things is a list of tuples where the first item in each tuple is the group 
the second item belongs to.

The groupby() function takes two arguments: (1) the data to group and (2) the 
function to group up with. 

Here, lambda x: x[0] tells groupby() to use the first item in each tuple as the grouping key.

In the above for statement, groupby returns three (key, group iterator) 
pairs - once for each unique key. You can use the returned iterator to iterate 
over each individual item in that group.
** Syntax of groupby is - 
groups = []
unique_keys = []
for k, g in groupby(data, keyfunc):
    groups.append(list(g))
    unique_keys.append(k)
k is the current grouping key, and g is an iterator that you can use to iterate 
over the group defined by that grouping key. In other words, the groupby iterator 
itself returns iterators.  ''' 
# Example is 
from itertools import groupby
things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"), ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    for thing in group:
        print("A %s is a %s."%(thing[1], key))
    print(" ")

# Here's a slightly different example with the same data, using a list comprehension:
for key, group in groupby(things, lambda x: x[0]):
    listofthings =" and ".join([thing[1] for thing in group])
    print(key + "s: " + listofthings + ".")

#Hackerrank Question  
'''Basically I'm unpacking the list comprehension and printing each element of it.

The list is built of elements of (len(list(c)), int(k)). len(list(c)) is simply 
the number of occurences of a character c returned by the groupby function. k is 
just the key value, the character itself. '''
str1 = input()
print(*[(len(list(c)), int(k)) for k, c in groupby(str1)])

#Another method 
for k, g  in groupby(str1):
    print("({}, {})".format(len(list(g)), k), end = " ")