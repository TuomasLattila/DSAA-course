class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.tail = Node(None, None)
        self.head = Node(None, self.tail)
        self.curr = None
        self.len = 0

    def append(self, it):
        if self.head.next == self.tail:
            self.head.next = Node(it, self.tail)
            self.len = 1
        else:
            self.tail.next = Node(self.tail.data, self.tail.next)
            self.tail.data = it
            self.tail = self.tail.next
            self.len += 1
        
    def insert(self, it, index):
        if index <= self.len and index >= 0:
            self.curr = self.head.next
            for i in range(self.len + 1):
                if i == index:
                    self.curr.next = Node(self.curr.data, self.curr.next)
                    self.curr.data = it
                    self.len += 1
                    if self.curr == self.tail:
                        self.tail = self.curr.next
                    break
                self.curr = self.curr.next

    def delete(self, index):
        if index <= self.len - 1 and index >= 0:
            self.curr = self.head.next
            for i in range(self.len):
                if i == index:
                    result = self.curr.data
                    self.curr.data = self.curr.next.data
                    self.curr.next = self.curr.next.next
                    self.len -= 1
                    if self.curr == self.tail:
                        self.tail = self.curr.next
                    return result
                self.curr = self.curr.next

    def print(self):
        self.curr = self.head.next
        for i in range(self.len):
            if i == self.len-1:
                print(self.curr.data)
            else:
                print(self.curr.data, "->", end = " ")
            self.curr = self.curr.next

    def index(self, it):
        self.curr = self.head.next
        for i in range(self.len):
            if self.curr.data == it:
                return i
            self.curr = self.curr.next
        return -1
    
    def swap(self, i, j):
        if self.len > i >= 0 and self.len > j >= 0:
            self.curr = self.head.next
            if j < i:
                i,j = j,i
            for x in range(self.len):
                if x == i:
                    data1 = self.curr
                if x == j:
                    self.curr.data, data1.data = data1.data, self.curr.data
                    break
                self.curr = self.curr.next

    def isort(self):
        dataList = []
        self.curr = self.head.next
        for i in range(self.len):
            dataList.append(self.curr.data)
            self.curr = self.curr.next
        
        for i in range(1,len(dataList)):
            j = i-1
            while j >= 0 and dataList[j] > dataList[j+1]:
                dataList[j], dataList[j+1] = dataList[j+1], dataList[j]
                j = j-1

        self.curr = self.head.next
        for i in range(self.len):
            self.curr.data = dataList[i]
            self.curr = self.curr.next

if __name__ == "__main__":
    L = LinkedList()
    for num in (3, 5, 2, 7, 8, 10, 6):
        L.append(num)
    L.print()   # 3 -> 5 -> 2 -> 7 -> 8 -> 10 -> 6
    L.isort()
    L.print()   # 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> 10