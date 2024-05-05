class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self.__insertHelp(self.root, key)

    def __insertHelp(self, node, key):
        if node == None:
            node = Node(key)
        elif node.key == key:
            return node
        elif key < node.key:
            node.left = self.__insertHelp(node.left, key)
        elif key > node.key:
            node.right = self.__insertHelp(node.right, key)
        return node
    
    def search(self, key):
        return self.__searchHelp(self.root, key)

    def __searchHelp(self, node, key):
        if node == None:
            return False
        elif node.key == key:
            return True
        elif key < node.key:
            return self.__searchHelp(node.left, key)
        elif key > node.key:
            return self.__searchHelp(node.right, key)
        
    def remove(self, key):
        self.root = self.__removeHelp(self.root, key)

    def __removeHelp(self, node, key):
        if node == None:
            return node
        elif key < node.key:
            node.left = self.__removeHelp(node.left, key)
        elif key > node.key:
            node.right = self.__removeHelp(node.right, key)
        else:
            if node.left == None:
                return node.right
            elif node.right == None:
                return node.left
            else:
                node.key = self.__getmax(node.left)
                node.left = self.__removeMax(node.left)
        return node

    def __getmax(self, node):
        if node.right == None:
            return node.key
        return self.__getmax(node.right)
    
    def __removeMax(self, node):
        if node.right == None:
            return node.left
        node.right = self.__removeMax(node.right)
        return node

    def preorder(self):
        self.__preorderHelp(self.root)
        print(end="\n")

    def __preorderHelp(self, node):
        if node == None:
            return
        print(node.key, end=" ")
        self.__preorderHelp(node.left)
        self.__preorderHelp(node.right)

    def postorder(self):
        self.__postorderHelp(self.root)
        print(end="\n")

    def __postorderHelp(self, node):
        if node == None:
            return
        self.__postorderHelp(node.left)
        self.__postorderHelp(node.right)
        print(node.key, end=" ")

    def inorder(self):
        self.__inorderHelp(self.root)
        print(end="\n")

    def __inorderHelp(self, node):
        if node == None:
            return
        self.__inorderHelp(node.left)
        print(node.key, end=" ")
        self.__inorderHelp(node.right)

    def breadthfirst(self):
        list = []
        if self.root == None:
            return
        list.append(self.root)
        while(len(list) > 0):
            print(list[0].key, end=" ")
            node = list.pop(0)
            if node.left != None:
                list.append(node.left)
            if node.right != None:
                list.append(node.right)
        print(end="\n")

if __name__ == "__main__":
    Tree = BST()
    keys = [5, 9, 1, 3, 7, 7, 4, 6, 2]

    for key in keys:
        Tree.insert(key)
   
    Tree.postorder()        # 2 4 3 1 6 7 9 5 
    Tree.inorder()          # 1 2 3 4 5 6 7 9  
    Tree.breadthfirst()     # 5 1 9 3 7 2 4 6