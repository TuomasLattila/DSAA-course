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

if __name__ == "__main__":
    L = LinkedList()
    L.append(1)
    L.append(3)
    L.print()           # 1 -> 3
    L.insert(10, 1)
    L.insert(15, 0)
    L.print()           # 15 -> 1 -> 10 -> 3
    L.delete(0)
    L.print()           # 1 -> 10 -> 3