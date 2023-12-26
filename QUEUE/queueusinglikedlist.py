class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class QUEUE:
    def __init__(self, start=None):
        self.start = None
        self.item_count = 0

    def is_empty(self):
        return self.start == None

    def enqueue(self, data):
        n = Node(data, self.start)
        self.start = n
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("queue is empty")

        elif self.start.next is None:
            data = self.start.item
            self.start = None
            self.item_count -= 1
            return data
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            data = temp.next.item
            temp.next = None
            self.item_count -= 1
            return data

    def get_front(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            temp = self.start.next
            while temp.next is not None:
                temp = temp.next
            data = temp.item
            return data

    def get_rear(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            return self.start.item

    def size(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            return self.item_count


my_obj = QUEUE()
my_obj.enqueue(10)
my_obj.enqueue(20)
my_obj.enqueue(30)
my_obj.enqueue(40)
my_obj.enqueue(50)


print("size of the queue is: ", my_obj.size())
print("front of the queue is: ", my_obj.get_front())
print("Rear of the queue is: ", my_obj.get_rear())
print("Delete the elemet is: ", my_obj.dequeue())
print("Delete the elemet is: ", my_obj.dequeue())
print("size of the queue is: ", my_obj.size())
print("front of the queue is: ", my_obj.get_front())
print("Rear of the queue is: ", my_obj.get_rear())
