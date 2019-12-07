# check if palindrome recursively
def palindrome_checker(string):
    s = string.lower().replace(" ", "")
    
    if len(s) < 2:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return palindrome_checker(s[1:-1])

# check if palindrome with one line 
def is_palindrome(word):
    return word == word[::-1]

print(palindrome_checker("rad A r"))
print(is_palindrome("radar"))

print(palindrome_checker("rad A r R"))
print(is_palindrome("radarr"))