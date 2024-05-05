def queen(n, m):
    board = [None]*(n)
    yList = []
    memory = {}
            
    def search(y, n, location, yList, m):
        if m == 0:
            return 1
        QCount = 0
        for x in range(n):
            if ((n-1)-x, y) in memory: #test if memory has the correct value
                QCount += memory[((n-1)-x, y)]
            else:
                for i in range(y,n-(m-1)):
                    if can_be_placed(y, x, yList, location):
                        location[y] = x
                        yList.append(y)
                        QCount += search(i + 1, n, location, yList, m-1)
                        location[y] = None
                        yList.pop()
                if y == 0: #save the value in the memory for later use
                    sum = 0
                    for i in memory:
                        sum += memory[i]
                    memory[(x, y)] = QCount -sum
        return QCount
                        
    def can_be_placed(y, x, yList, locations):
        for i in reversed(yList):
            if locations[i] == x:
                return False
            else:
                distance = (y - i)
                if locations[i] == (distance + x):
                    return False
                if locations[i] == (x - distance):
                    return False
        return True
    return search(0, n, board, yList, m)

if __name__ == "__main__":
    print(queen(4, 4))  # 2
    print(queen(4, 2))  # 44
    print(queen(6, 4))  # 982
    print(queen(7, 2))  # 700
    print(queen(8, 8))  # 92
