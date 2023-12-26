class QUEUE:
    def __init__(self, item=None):
        self.item = []
        self.item_count = 0

    def is_empty(self):
        return self.item == None

    def enqueue(self, data):
        self.item.append(data)
        self.item_count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        else:
            self.item_count -= 1
            return self.item.pop(0)

    def get_front(self):
        return self.item[0]

    def get_rear(self):
        return self.item[-1]

    def size(self):
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
