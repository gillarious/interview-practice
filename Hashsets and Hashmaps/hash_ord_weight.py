def hash(astring, table_size):
    sum = 0
    for pos in range(len(astring)):
        sum += ord(astring[pos]) * (pos + 1)
    return sum % table_size

print(hash("cat", 11))