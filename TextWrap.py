# https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/

s = input()
width = int(input())
for i in range(0, len(s), width):
    print(s[i:width+i])

# Another method 
import textwrap

def wrap(string, max_width):
    wraps = textwrap.fill(string,max_width)

    return wraps

if __name__ == '__main__':
    string, max_width = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 5
    result = wrap(string, max_width)
    print(result)

#Another method 
#print("\n".join([string[i:max_width+i] for i in range(0, len(string), max_width)]))