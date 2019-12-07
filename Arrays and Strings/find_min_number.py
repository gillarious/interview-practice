#o(n) solution
def find_min2(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min


test = [21,35,7,99,2]

print(find_min2(test))