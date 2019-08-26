my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life']
list1 = []
chunk_size = 4
for i in range(0, len(my_list), chunk_size):
    list1.append(my_list[i:i+chunk_size])
print(list1)
#Another method we can use yield method to access list elements
my_list = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 
  
# Yield successive n-sized 
# chunks from l. 
def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# How many elements each 
# list should have 
n = 5
  
x = list(divide_chunks(my_list, n)) 
print (x) 