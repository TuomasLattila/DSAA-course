class listClass:
    maxNumLeft = []
    minNumRight = []

def split(T):
    result = 0
    compareNumbers = []
    newMaxNumLeft = T[0]
    newMinNumRight = T[len(T)- 1]
    minNumsRight = []

    for i in range(len(T)-1):
        if T[len(T)- 1 - i] < newMinNumRight:
            newMinNumRight = T[len(T)- 1 - i]
        minNumsRight.append(newMinNumRight)
        
    for i in range(len(T)-1):
        if T[i] > newMaxNumLeft:
            newMaxNumLeft = T[i]
        lists = listClass()
        lists.maxNumLeft = newMaxNumLeft
        lists.minNumRight = minNumsRight[len(T)-2 - i]
        compareNumbers.append(lists)
        
    for i in range(len(compareNumbers)):
        if compareNumbers[i].maxNumLeft < compareNumbers[i].minNumRight:
            result += 1
    return result

if __name__ == "__main__":
    print(split([1,2,3,4,5]))       # 4
    print(split([5,4,3,2,1]))       # 0
    print(split([2,1,2,5,7,6,9]))   # 3
    print(split([1,2,3,1]))         # 0