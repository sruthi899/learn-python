class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    def preorder(self,root):
        list = []
        if root:
            list.append(root.data)
            list += self.preorder(root.left)
            list += self.preorder(root.right)
        return list

    def inorder(self,root):
        list = []
        if root:
            list = self.inorder(root.left)
            list.append(root.data)
            list += self.inorder(root.right)
        return list

    def postorder(self,root):
        list = []
        if root:
            list = self.postorder(root.left)
            list += self.postorder(root.right)
            list.append(root.data)
        return list


root = node(27)
x = int(input("enter the no of data:"))
while x > 0:
    data = int(input("enter data:"))
    root.insert(data)
    x -= 1
root.printTree()
print(root.preorder(root))
print(root.inorder(root))
print(root.postorder(root))

