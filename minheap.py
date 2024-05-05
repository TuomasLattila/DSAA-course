class MinHeap:
    def __init__(self, list):
        self.list = list
        x = 1
        start = 1
        length = 1
        while True:
            if start +(2*x) >= len(list):
                break
            start += (2*x)
            x = 2*x
            length += 1
        for i in range(length):
            for j in range(start-1,-1,-1):
                self.heapify(list, j)
        

    def heapify(self, list, root):
        left = (2*root+1)
        right = (2*root+2)
        smallestChild = root
        if left < len(list) and list[left] < list[smallestChild]:
            smallestChild = left
        if right < len(list) and list[right] < list[smallestChild]:
            smallestChild = right

        if list[smallestChild] != list[root]:
            list[smallestChild], list[root] = list[root], list[smallestChild]
        
    def pop(self):
        self.list[0], self.list[len(self.list)-1] = self.list[len(self.list)-1], self.list[0]
        deleted = self.list.pop()
        list = self.list
        if len(list) == 0:
            return deleted
        x = 1
        start = 1
        length = 1
        while True:
            if start +(2*x) >= len(list):
                break
            start += (2*x)
            x = 2*x
            length += 1
        for i in range(length):
            for j in range(start-1,-1,-1):
                self.heapify(list, j)
        return deleted

    def push(self, key):
        self.list.append(key)
        list = self.list
        x = 1
        start = 1
        length = 1
        while True:
            if start +(2*x) >= len(list):
                break
            start += (2*x)
            x = 2*x
            length += 1
        for i in range(length):
            for j in range(start-1,-1,-1):
                self.heapify(list, j)

    def print(self):
        for i in range(len(self.list)):
            print(self.list[i], end=" ")
        print(end="\n")

if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3 
    print(heap.pop())   # 1
    heap.print()
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9