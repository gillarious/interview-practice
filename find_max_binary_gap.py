def find_max_binary_gap(N):
    N = list('{0:08b}'.format(N))
    ones = 0
    for i in range(len(N)):
        if int(N[i]) == 1:
            ones += 1
    if ones < 2:
        return 0
    else:
        gaps = {}
        prev = 0
        for i in range(1, len(N)):
                if int(N[i]) == 0 and int(N[i-1]) == 1:
                    gaps[i] = 0
                    prev = i
                elif int(N[i]) == 1 and i > prev and prev > 0:
                    gaps[prev] = i
                    prev = 0
        max_gap = 0
        for key, val in gaps.items():
            ans = val - key
            if ans > max_gap:
                max_gap = ans
        return max_gap

print("5 in binary is " + '{0:08b}'.format(5))
print("Longest binary gap is " + str(find_max_binary_gap(5)))

print("32 in binary is " + '{0:08b}'.format(32))
print("Longest binary gap is " + str(find_max_binary_gap(32)))

print("1073741825 in binary is " + '{0:08b}'.format(1073741825))
print("Longest binary gap is " + str(find_max_binary_gap(1073741825)))