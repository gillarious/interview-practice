def binary_search(alist, start, end, item):
    dist = end - start
    midpoint = dist // 2 + start
    if midpoint == len(alist):
        midpoint -= 1
    if alist[midpoint] == item:
            return True
    elif dist <= 0:
        return False
    else:
        if item < alist[midpoint]:
            return binary_search(alist, start, midpoint, item)
        else:
            return binary_search(alist, midpoint+2, end, item)

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search(test_list, 0, len(test_list), 3))
print(binary_search(test_list, 0, len(test_list), 13))
print(binary_search(test_list, 0, len(test_list), 19))
print(binary_search(test_list, 0, len(test_list), 39))
print(binary_search(test_list, 0, len(test_list), 42))
print(binary_search(test_list, 0, len(test_list), 0))