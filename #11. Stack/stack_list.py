class stack:
     def __init__(self,item=None):
          self.item=[]


     def is_empty(self):
          return self.item==None

     def push(self,data):
          self.item.append(data)

     def pop(self):
          if not self.is_empty():
               return self.item.pop()
          else:
               return None     

     def peek(self):
          if self.is_empty():
               return None
          else:
               return self.item[-1]     

     def size(self):
          if self.is_empty():
               return len(self.item)  
          else:
               return len(self.item)                              
      

list3=stack()
list3.push(10)
list3.push(20)
list3.push(30)
list3.push(40)
list3.push(50)
list3.push(60)

print(list3.peek())
print(list3.pop())
print(list3.pop())
print(list3.peek())

print(list3.size())