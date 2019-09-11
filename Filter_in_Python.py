'''
Check if the string is of length = 2. '''
def isOfLengthFour(string1):
    if len(string1) == 2:
        return True 
    else:
        return False
def main():
    listOfStr = ['hi', 'this' , 'is', 'a', 'very', 'simple', 'string' , 'for', 'us']

    print("Original List is : ", listOfStr)

    print("Filtering list using filter method. ")
    filtered_List = list(filter(isOfLengthFour, listOfStr))
    print("Filtered list is : ", filtered_List)

    #Filtering list using lambda and filter combine 
    filtered_List1 = list(filter(lambda x: len(x)==2, listOfStr))
    print("Filtered list using lambda is : ", filtered_List1)

    #Filtering characters from a string using filter() 

    strObj = 'Hi this is a sample string, a very sample string'

    filteredChars = ''.join(filter(lambda x: x not in['a','s'], strObj))

    print('Filtered Characters  : ', filteredChars)
    print('*** Filter an array in Python using filter() ***')
    array1 = [1,3,4,5,21,33,45,66,77,88,99,5,3,32,55,66,77,22,3,4,5]
    array2 = [5,3,66]
    filteredArray = list(filter(lambda x : x not in array2, array1))
    print('Filtered Array  : ', filteredArray)
if __name__ == '__main__':
    main()
