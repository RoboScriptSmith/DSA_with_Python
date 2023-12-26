class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.next = next
        self.item = item
        self.prev = prev


class Duque:
    def __init__(self, start=None):
        self.count = 0
        self.start = start

    def is_empty(self):
        return self.start== None

    def insert_front(self, data):
        self.count += 1
        n = Node(None, data, self.start)
        if self.is_empty():
            self.start = n

        else:
            self.start.prev = n
            self.start=n

    def insert_rear(self, data):
        self.count += 1
        temp = self.start
        if temp is not None:
            while temp.next != None:
                temp = temp.next
            n = Node(temp, data, None)
            temp.next = n
        else:
            n = Node(None, data)
            self.start = n

    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            self.count -= 1
            data = self.start.item

            self.start = self.start.next
            return data

    def delete_rear(self):
        if self.start is None:
            raise IndexError("deque is empty")
        elif self.start.next is None:
            self.count -= 1
            data = self.start.item
            self.start = None
            return data
        else:
            self.count -= 1
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            data = temp.next.item
            temp.next = None
            return data

    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.start.item

    def get_rear(self):
        if self.start is None:
            raise IndexError("deque is empty")
        elif self.start.next is None:
            return self.start.item
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            return temp.next.item

    def size(self):
        return self.count

obj=Duque()
obj.insert_front(20)
obj.insert_front(10)
obj.insert_rear(30)
obj.insert_rear(40)
print("get_front:",obj.get_front())
print("get_rear:",obj.get_rear())
print("size of deque:",obj.size())
print("delete_front:",obj.delete_front())
print("delete_front:",obj.delete_front())
print("delete_rear:",obj.delete_rear())
print("delete_rear:",obj.delete_rear())
print("size of deque:",obj.size())
