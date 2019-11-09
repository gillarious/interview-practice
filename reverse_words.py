def reverse_words(string):
    if string:
        words = string.split(" ")
        return " ".join(words[::-1])
    return string
    
test = "Hello World And Stacey"

print(test)
print(reverse_words(test))