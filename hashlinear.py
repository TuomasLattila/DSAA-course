class HashLinear:
    def __init__(self, size):
        self.size = size
        self.hasTable = []
        for i in range(size):
            self.hasTable.append(None)

    def calcSlotIndex(self, data):
        sum = 0
        for i in range(len(data)):
            sum += ord(data[i])
        return sum % self.size

    def insert(self, data):
        if self.hasTable[self.calcSlotIndex(data)] == data:
            return
        if self.hasTable[self.calcSlotIndex(data)] == None:
            self.hasTable[self.calcSlotIndex(data)] = data
        else:
            index = self.calcSlotIndex(data) + 1 
            for i in range(self.size):
                if index == self.size:
                    index = 0
                if self.hasTable[index] == None:
                    self.hasTable[index] = data
                    break
                index += 1

    def delete(self, data):
        for i in range(self.size):
            if self.hasTable[i] == data:
                self.hasTable[i] = None

    def print(self):
        for i in range(self.size):
            if self.hasTable[i] != None:
                print(self.hasTable[i], end=" ")
        print(end="\n")

if __name__ == "__main__":
    table = HashLinear(8)
    table.insert("BM40A1500")
    table.insert("fOo")
    table.insert("123")
    table.insert("Bar1")
    table.insert("10aaaa1")
    table.insert("BM40A1500")
    table.print()   # 10aaaa1 BM40A1500 fOo 123 Bar1
    table.delete("fOo")
    table.delete("Some arbitary string which is not in the table")
    table.delete("123")
    table.print()   # 10aaaa1 BM40A1500 Bar1