class Node:
     def __init__(self,prev=None,item=None,next=None):
          self.prev=prev
          self.item=item
          self.next=next

class CDLL:
     def __init__(self,start=None):
          self.start=start

     def is_empty(self):
          return self.start==None     

     def insert_at_start(self,data):
          if self.is_empty():
               n=Node(None,data,None)
               n.next=n
               n.prev=n      
               self.start=n
          else:
               n=Node(self.start.prev,data,self.start)
               self.start.prev.next=n
               self.start.prev=n
               self.start=n
     
     def insert_at_last(self,data):
           if self.is_empty():
               n=Node(None,data,None)
               n.next=n
               n.prev=n      
               self.start=n

           else:
               n=Node(self.start.prev,data,self.start)
               self.start.prev.next=n
               self.start.prev=n    


     def search(self,data):
          temp=self.start
          while temp!=temp.prev:
               if temp.item==data:
                    return temp
               temp=temp.next  
          if temp.item==data:
               return temp

     def insert_after(self,temp,data):
          if self.is_empty():
               n=Node(None,data,None)
               n.next=n
               n.prev=n      
               self.start=n

          else:
                n=Node(temp,data,temp.next)
                temp.next.prev=n
                temp.next=n

     def print_list(self):
          if not self.is_empty():
               temp=self.start
               while temp!=self.start.prev:
                    print(temp.item, end=' ')
                    temp=temp.next
               print(temp.item,end=' ')

     def delete_at_first(self):
          self.start.prev.next=self.start.next
          self.start.next.prev=self.start.prev
          self.start=self.start.next           

     def delete_at_last(self):
          self.start.prev=self.start.prev.prev
          self.start.prev.prev=self.start
      

     def delete_after(self,temp):
          temp.prev.next=temp.next
          temp.next.prev=temp.prev
     def __iter_(self):
          return CDLLIterator(self.start)

# class CDLLIterator:
#      def __init__(self,start):
#           self.current=start
#      def __iter__(self):
#           return self
#      def __next__(self):
#           if not self.current:
#                raise StopIteration
#           data=self.current.item
#           self.current=self.current.next
#           return data               


list2=CDLL()
list2.insert_at_start(10)
list2.insert_at_start(5)
list2.insert_at_last(20)
list2.insert_at_last(30)
list2.insert_at_last(40)
list2.insert_at_last(50)
list2.insert_after(list2.search(40),45)

list2.print_list()
print()

list2.delete_at_first()
list2.delete_at_last()
list2.delete_after(list2.search(30))
list2.print_list()


# for x in list2:
#      print(x,end=' ')