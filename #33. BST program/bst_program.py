class Node:
    def __init__(self, item=None, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)

        elif data < root.item:
            root.left = self.rinsert(root.left, data)

        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root is None or root.item == data:
            return root

        elif data < root.item:
            return self.rsearch(root.left, data)

        elif data > root.item:
            return self.rsearch(root.right, data)

    def inorder(self):
        result = []
        self.rinorder(self.root, result)
        return result

    def rinorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

    def preorder(self):
        result = []
        self.rpreorder(self.root, result)
        return result

    def rpreorder(self, root, result):
        if root:
            result.append(root.item)
            self.rpreorder(root.left, result)
            self.rpreorder(root.right, result)

    def postnorder(self):
        result = []
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)


             
obj=BST()
print("Insert element in BST")
obj.insert(50)
obj.insert(30)
obj.insert(70)
obj.insert(10)
obj.insert(90)
obj.insert(60)
obj.insert(80)
print("Insertion is END")

print("search 40 element")
print(obj.search(40))

print("Inorder traversing ")
print(obj.inorder())
print("postorder traversing ")
print(obj.postnorder())
print("preorder traversing ")
print(obj.preorder())