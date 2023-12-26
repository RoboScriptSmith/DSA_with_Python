class Duque:
    def __init__(self):
        self.item = []
        self.count = 0

    def is_empty(self):
        return self.item == None

    def insert_front(self, data):
        self.count += 1
        self.item.insert(0,data)

    def insert_rear(self, data):
        self.count += 1
        self.item.append(data)

    def delete_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            self.count -= 1
            return self.item.pop(0)

    def delete_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            self.count -= 1
            return self.item.pop(-1)

    def get_rear(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.item[-1]

    def get_front(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.item[0]

    def size(self):
        if self.is_empty():
            raise IndexError("deque is empty")
        else:
            return self.count

obj=Duque()
obj.insert_front(20)
obj.insert_front(10)
obj.insert_rear(30)
obj.insert_rear(40)
print("get for front:",obj.get_front())
print("get for rear:",obj.get_rear())
print("size of deque:",obj.size())
print("deque for front:",obj.delete_front())
print("deque for front:",obj.delete_front())
print("deque for rear:",obj.delete_rear())
print("deque for rear:",obj.delete_rear())
