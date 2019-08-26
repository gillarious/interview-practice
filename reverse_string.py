# how to reverse string iteratively
def reverse_string(string):
    string = list(string)
    reverse = []

    for i in range(len(string)):
        reverse.append(string.pop())

    return str("".join(reverse))

# how to reverse string using recursion
def reverse(s):
    return (s if len(s) == 0 else reverse(s[1:]) + s[0])


print(reverse_string("hi lmao"))
print(reverse("hi lmao"))