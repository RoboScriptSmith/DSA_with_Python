class stack(list):
    def is_empty(self):
        return len(self)==0

    def push(self, data):
        self.append(data)

    def pop(self):
        if not self.is_empty():
            return super().pop()
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not self.is_empty():
            return self[-1]
        else:
            raise IndexError("stack is empty")

    def size(self):
        if not self.is_empty():
            return len(self)
        else:
            raise IndexError("stack is empty")
    def insert(self,index,data):
     raise AttributeError("No attribute 'insert' in stack" )

list4 = stack()
list4.push(10)
list4.push(20)
list4.push(30)
list4.push(40)
list4.push(50)
list4.push(60)

print(list4.peek())
print(list4.pop())
print(list4.pop())
print(list4.peek())

print(list4.size())
