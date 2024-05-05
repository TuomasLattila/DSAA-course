class HashBucket:
    def __init__(self, size, buckets):
        self.size = size
        self.buckets = buckets
        self.hashTable = [None] * buckets
        for i in range(len(self.hashTable)):
            bucket = [None] * int(size/buckets)
            self.hashTable[i] = bucket
        self.overflow = [None] * size

    def calcSlotIndex(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.buckets

    def insert(self, data):
        for i in range(len(self.hashTable[self.calcSlotIndex(data)])):
            if self.hashTable[self.calcSlotIndex(data)][i] == data:
                return
            if self.hashTable[self.calcSlotIndex(data)][i] == None:
                self.hashTable[self.calcSlotIndex(data)][i] = data
                return
        for i in range(len(self.overflow)):
            if self.overflow[i] == None:
                self.overflow[i] = data
                break

    def delete(self, data):
        for i in range(len(self.hashTable[self.calcSlotIndex(data)])):
            if self.hashTable[self.calcSlotIndex(data)][i] == data:
                self.hashTable[self.calcSlotIndex(data)][i] = None
                break

        for i in range(len(self.overflow)):
            if self.overflow[i] == data:
                self.overflow.pop(i)
                self.overflow.append(None)
                return
    
    def print(self):
        for i in range(len(self.hashTable)):
            for j in range(len(self.hashTable[i])):
                if self.hashTable[i][j] != None:
                    print(self.hashTable[i][j], end=" ")
        
        for i in range(len(self.overflow)):
            if self.overflow[i] != None:
                print(self.overflow[i], end=" ")
        print(end="\n")

if __name__ == "__main__":
    table = HashBucket(8, 4)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # fOo BM40A1500 123 Bar1 10aaaa1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # BM40A1500 Bar1 10aaaa1