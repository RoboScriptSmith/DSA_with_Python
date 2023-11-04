class Node:
     def __init__(self,item=None,next=None):
          self.item=item
          self.next=next

class CLL:
     def __init__(self,last=None):
          self.last=last

     def is_empty(self):
          return self.last==None  

     def insert_at_start(self,data):
        if self.last is None:
            n=Node(data)
            self.last=n
            self.last.next=self.last
            
        n=Node(data,self.last.next)
        self.last.next=n
      




###################################################################################3      
     
     def print_list(self):
        temp = self.last.next
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

     def __iter__(self):
        return CLLIterator(self.last)


class CLLIterator:
    def __init__(self, last):
        self.current = last

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
list1 = CLL()
########################################################################################################3


list1.insert_at_start(10)
list1.insert_at_start(20)
list1.insert_at_start(30)
list1.insert_at_start(40)
# list1.print_list()

##########################################################################################
for x in list1:
    print(x, end=' ')
print()

           