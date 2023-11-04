class Node:
     def __init__(self,prev=None,item=None,next=None):
          self.prev=prev
          self.item=item
          self.next=next

class DLL:
     def __init__(self,start=None):
          self.start=start

     def is_empty(self):
          return self.start == None
     def insert_at_start(self,data):
          n=Node(None,data,self.start)
          if  not self.is_empty():
               self.start.prev=n
          self.start=n 
     def insert_at_last(self,data):
          temp=self.start
          if temp is not None:
               while temp.next!=None:
                    temp=temp.next
               n=Node(temp,data,None)
               temp.next=n
          else:
               self.start=n
                         
     def search(self,data):
          temp=self.start
          while temp.next is not None:
               if temp.item==data:
                    return temp
               temp=temp.next
          return None
     def insert_after(self,temp,data):
          
          if temp is not None:
             n=Node(temp,data,temp.next)
             if temp.next is not None:
               temp.next.prev=n          
             temp.next=n
              
     def delete_first(self):
          if self.start is not None:
               self.start=self.start.next    
               
     def delete_last(self):
          if self.start is None:
               pass
          elif self.start.next is None:
               self.start=None
          else:
               temp=self.start
               while temp.next.next is not None:
                   temp=temp.next
               temp.next=None
     def delete_item(self,data):
          temp=self.start
          while temp is not None:
               if temp.item==data:
                    if temp.next is not None:
                         temp.next.prev=temp.prev
                    if temp.prev is not None:
                         temp.prev.next=temp.next
                    else:
                         self.start=temp.next     
               temp=temp.next          
#####################################################################
     def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next


     def __iter__(self):
          return DLLIterator(self.start)
class DLLIterator:
    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
   
#########################################################################################

mylist=DLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(40)
mylist.insert_at_last(50)
mylist.insert_at_last(60)
mylist.insert_at_last(70)
mylist.insert_at_last(80)
mylist.insert_after(mylist.search(20),25)

####################################################################################
for x in mylist:
    print(x,end=' ')
print()
#####################################################################################
mylist.delete_first()
mylist.delete_last()
mylist.delete_item(50)
############################################################
for x in mylist:
    print(x,end=' ')
print()