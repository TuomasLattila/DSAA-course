def sums(items):
    sums_list = [0]
    sums_list.append(items[0])
    for i in range(1, len(items)):
        last_length = 0
        for j in range(len(sums_list)):
            if i != len(items)-1:
                sums_list.append(sums_list[j])
                sums_list.append(sums_list[j]+items[i])
                last_length +=1
            else:
                sums_list.append(sums_list[j]+items[i])
        sums_list = sums_list[last_length:]
    value_list = set()
    for i in range(len(sums_list)):
        value_list.add(sums_list[i])
    value_list.remove(0) #remove 0
    #print(value_list)
    return len(value_list)

if __name__ == "__main__":
    print(sums([1, 2, 3]))                  # 6
    print(sums([2, 2, 3]))                  # 5
    print(sums([43, 6, 48, 23, 37, 37, 8, 30, 4, 34, 2, 29, 9, 16, 33, 3, 39, 42, 11, 8, 7, 33, 28, 43, 49]))
    print(sums([1, 3, 5, 1, 3, 5]))         # 18
    print(sums([1, 15, 5, 23, 100, 55, 2])) # 121
    #print(sums([9, 38, 13, 28, 32, 26, 44, 34, 4, 27, 20, 17, 13, 16, 31, 8, 21, 43, 19, 42, 35, 47, 1, 30, 31, 24, 32, 26, 39, 35, 2, 32, 43, 1, 13, 37, 1, 10, 20, 24]))