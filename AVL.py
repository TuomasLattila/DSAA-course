class AVLNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        self.balance = 0

class AVL:
    def __init__(self):
        self.root = None
        self.is_balanced = True

    def insert(self, data):
        self.root = self.balanced_insert(self.root, data)

    def balanced_insert(self, root, data):
        if root == None:
            root = AVLNode(data)
            self.is_balanced = False
        elif data < root.data:
            root.left = self.balanced_insert(root.left, data)
            #Check if not balanced
            if self.is_balanced == False:
                if root.balance >= 0:
                    self.is_balanced = root.balance == 1
                    root.balance -= 1
                else:
                    if root.left.balance == -1:
                        root = self.right_rotation(root)
                    else:
                        root = self.left_right_rotation(root)
                    self.is_balanced = True
        elif data > root.data:
            root.right = self.balanced_insert(root.right, data)
            #Check if not balanced
            if self.is_balanced == False:
                if root.balance <= 0:
                    self.is_balanced = root.balance == -1
                    root.balance += 1
                else:
                    if root.right.balance == 1:
                        root = self.left_rotation(root)
                    else:
                        root = self.right_left_rotation(root)
                    self.is_balanced = True
        return root
    
    def right_rotation(self, root):
        child = root.left
        root.left = child.right
        child.right = root
        child.balance = root.balance = 0
        return child

    def left_right_rotation(self, root):
        child = root.left
        grandchild = child.right
        child.right = grandchild.left
        grandchild.left = child
        root.left = grandchild.right
        grandchild.right = root
        child.balance = root.balance = 0
        if grandchild.balance == -1:
            root.balance = 1
        elif grandchild.balance == 1:
            child.balance = -1
        grandchild.balance = 0
        return grandchild
    
    def left_rotation(self, root):
        child = root.right
        root.right = child.left
        child.left = root
        child.balance = root.balance = 0
        return child

    def right_left_rotation(self, root):
        child = root.right
        grandchild = child.left
        child.left = grandchild.right
        grandchild.right = child
        root.right = grandchild.left
        grandchild.left = root
        child.balance = root.balance = 0
        if grandchild.balance == -1:
            child.balance = 1
        elif grandchild.balance == 1:
            root.balance = -1
        grandchild.balance = 0
        return grandchild
    
    def preorder(self):
        self.preorder_print(self.root)
        print(end="\n")

    def preorder_print(self, root):
        print(str(root.data) + ";" + str(root.balance), end=" ")
        if root.left != None:
            self.preorder_print(root.left)
        if root.right != None:
            self.preorder_print(root.right)
        return

if __name__ == "__main__":
    Tree = AVL()
    for key in [9, 10, 11, 3, 2, 6, 4, 7, 5, 1]:
        Tree.insert(key)
    Tree.preorder()     # 9;-1 4;0 2;0 1;0 3;0 6;0 5;0 7;0 10;1 11;0