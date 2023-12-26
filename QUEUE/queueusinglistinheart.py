class QUEUE(list):
    

    def is_empty(self):
        return len(self) == 0

    def enqueue(self, data):
        self.append(data)
       

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        else:
            return super().pop(0)
       

    def get_front(self):
        return self[0]

    def get_rear(self):
        return self[-1]

    def size(self):
     return len(self)


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



