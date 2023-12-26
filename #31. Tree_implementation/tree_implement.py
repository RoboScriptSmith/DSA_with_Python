class Node:
    def __init__(self, prev=None, left=None, item=None, right=None):
        self.left = left
        self.prev = prev
        self.item = item
        self.right = right


class Tree:
    def __init__(self, root=None):
        self.root = root

    def is_empty(self):
        return self.root == None

    def Insertation(self, data):
        if self.is_empty():
            print(data)
            n = Node(None, None, data, None)
            self.root = n

        else:
            print("1.insert from left press: 1")
            print("2.insert from right press: 2")
            print("3.back press: 3")

            val = int(input())
            temp = self.root
            n = Node(temp, None, data, None)
            if (val == 1):
                print(data)
                temp.left = n
                temp = n
            elif (val == 2):
                print(data)
                temp.right = n
                temp = n
            elif (val == 3):
                temp = temp.left
        33333


obj = Tree()
obj.Insertation(20)
obj.Insertation(30)
obj.Insertation(40)
obj.Insertation(50)
