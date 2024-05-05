def pairs(s):
    count = 0
    distances = []
    sum = 0
    y = 0
    x = 2
    for i in range(len(s)):
        if s[i] == "1":
            if count != 0:
                distances.append(count)
            count = 1
        else:
            if count != 0:
                count += 1

    listLength = len(distances)
    length = len(distances)
    for i in range(len(distances)):
        y += 1
        sum += distances[i] * length
        length = (listLength-y)*x
        x += 1
    return sum


if __name__ == "__main__":
    print(pairs("100101"))          # 10
    print(pairs("101"))             # 2
    print(pairs("100100111001"))    # 71