from singly_list import*
obj = SLL()


class QUEUE:
    def __init__(self):
        self.item_count = 0

    def is_empty(self):
        return obj.is_empty()

    def enqueue(self, data):
        obj.insert_at_start(data)
        self.item_count += 1

    def dequeue(self):
        self.item_count -= 1
        return obj.delete_last()

    def get_front(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            temp = obj.start.next
            while temp.next is not None:
                temp = temp.next
            data = temp.item
            return data

    def get_rear(self):
        if self.is_empty():
            raise IndexError("queue is empty")
        else:
            return obj.start.item

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
