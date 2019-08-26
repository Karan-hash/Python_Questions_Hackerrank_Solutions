str1 = input()
def capitalize_first_last_letters(str1):
    str1 = result = str1.title() #Capitalize first letter of each word
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " " # Capitalize last letter of word
    return result[:-1]
print(capitalize_first_last_letters(str1))
