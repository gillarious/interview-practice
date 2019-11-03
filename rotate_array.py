def rotate_array(A, K):
    if len(A) == 0:
        return A
    for _ in range(K):
        temp = A[-1]
        for i in range(len(A)-1, 0, -1):
            A[i] = A[i-1]
        A[0] = temp
    return A

test = [0, 1, 2, 3, 4, 5, 6]

#rotate once
print(rotate_array(test, 1))

#rotate four times
print(rotate_array(test, 4))