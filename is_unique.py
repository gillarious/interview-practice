def is_unique(string):
    s = set(())
    
    for i in string:
        if i in s:
            return False
        s.add(i)

    return True


print(is_unique("lol"))
print(is_unique("lmao"))