#Let's say
# https://stackoverflow.com/questions/13252333/python-check-if-all-elements-of-a-list-are-the-same-type
list1 = [1,2,3,4,5,6]
list2 = [1,2,'-',4,5,'a']
def check_values(list1):
    return all(isinstance(x, int) for x in list1)
print(check_values(list1))
print(check_values(list2)) 
#Another method 
# Using any(), no need to traverse whole list. Just break as soon as object which is not int or long is found:
def check_values1(list1):
    return any(not isinstance(y,int) for y in list1)
print(check_values1(list2))