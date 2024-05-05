def jumps(n, a, b):
    values = [0]*(n+1)
    values[0] = 1
    for i in range(1, n+1):
        if i-a >= 0:
            values[i] += values[i-a]
        if i-b >= 0:
            values[i] += values[i-b]
    return values[n]

if __name__ == "__main__":
    print(jumps(4, 1, 2)) # 5
    print(jumps(8, 2, 3)) # 4
    print(jumps(11, 6, 7)) # 0
    print(jumps(30, 3, 5)) # 58
    print(jumps(100, 4, 5)) # 1167937
    print(jumps(10000, 4, 5))