def reverse_words(string):
    return " ".join(string.split(" ")[::-1])
    
test1 = "Hello World And Stacey"
test2 = ""
test3 = "l     mao"

print(test1)
print(reverse_words(test1))

print(test2)
print(reverse_words(test2))

print(test3)
print(reverse_words(test3))