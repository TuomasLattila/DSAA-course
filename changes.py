def changes(A):
    result = 0
    compareNum = A[0]
    count = 1
    for i in range(1, len(A)):
        if A[i] == compareNum:
            count += 1
        else:
            compareNum = A[i]
            string = str((count/2))[0:1]
            result += int(string)
            count = 1
    string = str((count/2))[0:1]
    result += int(string)
    return result


if __name__ == "__main__":
    print(changes([1, 1, 2, 2, 2]))     # 2
    print(changes([1, 2, 3, 4, 5]))     # 0
    print(changes([1, 1, 1, 1, 1]))     # 2