import single as sl

my_obj=sl.SLL()


class stack:
     def __init__(self):
          self.item_count=0
     def is_empty(self):
          return my_obj.is_empty()

     def push(self,data):
               my_obj.insert_at_start(data)
               self.item_count+=1
     def pop(self):
          if self.is_empty():
               raise IndexError("Stack is empty")     
          else:
               
               self.item_count-=1
               return my_obj.delete_first()

     def peek(self):
          return my_obj.start.item

     def size(self):
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



