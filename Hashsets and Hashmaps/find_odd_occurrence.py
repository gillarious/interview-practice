def find_odd_occurrence(A):
    occurrences = {}
    for i in A:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    for key, val in occurrences.items():
        if val % 2 == 1:
            return key

test = [9, 3, 9, 3, 9, 7, 9]
print(find_odd_occurrence(test))