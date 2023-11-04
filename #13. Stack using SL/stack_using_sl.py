class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class stack:
    def __init__(self, start=None):
        self.start = start
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def push(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def pop(self):

        if self.is_empty():
            raise IndexError("stack is empty")

        else:
            data = self.start.item
            self.start = self.start.next
            self.item_count -= 1
            return data

    def peek(self):

        if self.is_empty():
            raise IndexError("stack is empty")

        else:
            return self.start.item

    def size(self):

        if self.is_empty():
            raise IndexError("stack is empty")

        else:
            return self.item_count


list4 = stack()
list4.push(10)
list4.push(20)
list4.push(30)
list4.push(40)
list4.push(50)
list4.push(60)

print("Top of the stack: ",list4.peek())
print("Delete the element: ",list4.pop())
print("Delete the element: ",list4.pop())
print("Top of the stack: ",list4.peek())

print("Size of the element: ",list4.size())
