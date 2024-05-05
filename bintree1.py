class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.insertHelp(self.root, key)

    def insertHelp(self, node, key):
        if node == None:
            node = Node(key)
        elif node.key == key:
            return node
        elif key < node.key:
            node.left = self.insertHelp(node.left, key)
        elif key > node.key:
            node.right = self.insertHelp(node.right, key)
        return node
    
    def search(self, key):
        return self.searchHelp(self.root, key)

    def searchHelp(self, node, key):
        if node == None:
            return False
        elif node.key == key:
            return True
        elif key < node.key:
            return self.searchHelp(node.left, key)
        elif key > node.key:
            return self.searchHelp(node.right, key)
        
    def remove(self, key):
        self.root = self.removeHelp(self.root, key)

    def removeHelp(self, node, key):
        if node == None:
            return node
        elif key < node.key:
            node.left = self.removeHelp(node.left, key)
        elif key > node.key:
            node.right = self.removeHelp(node.right, key)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                node.key = self.getmax(node.left)
                node.left = self.removeMax(node.left)
        return node

    def getmax(self, node):
        if node.right == None:
            return node.key
        return self.getmax(node.right)
    
    def removeMax(self, node):
        if node.right == None:
            return node.left
        node.right = self.removeMax(node.right)
        return node

    def preorder(self):
        self.preorderHelp(self.root)
        print(end="\n")

    def preorderHelp(self, node):
        if node == None:
            return
        print(node.key, end=" ")
        self.preorderHelp(node.left)
        self.preorderHelp(node.right)
        

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)

    Tree.preorder()         # 5 1 3 2 4 9 7 6
 
    print(Tree.search(6))   # True
    print(Tree.search(8))   # False
    
    Tree.remove(1)
    Tree.preorder()         # 5 3 2 4 9 7 6
    Tree.remove(9)
    Tree.preorder()         # 5 3 2 4 7 6 
    Tree.remove(3)
    Tree.preorder()         # 5 2 4 7 6