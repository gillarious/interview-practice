def is_anagram(a, b):
    letters_a = {}
    letters_b = {}
    if len(a) != len(b):
        return False
    for i in a:
        if i not in letters_a:
            letters_a[i] = 1
        else:
            letters_a[i] += 1
    for i in b:
        if i not in letters_b:
            letters_b[i] = 1
        else:
            letters_b[i] += 1
    for key, val in letters_a.items():
        if key not in letters_b:
            return False
        elif val != letters_b[key]:
            return False
    return True

print(is_anagram("hi", "ih"))
print(is_anagram("lol", "ooo"))
print(is_anagram("aab", "bba"))