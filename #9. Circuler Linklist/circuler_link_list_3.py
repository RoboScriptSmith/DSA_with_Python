class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next


class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self): 
        return self.last == None

    def insert_at_start(self, data):
        if self.is_empty():
            n = Node(data)
            n.next = n
            self.last = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n

    def insert_at_last(self, data):
        if self.is_empty():
            n = Node(data)
            n.next = n
            self.last = n
        else:
            n = Node(data, self.last.next)
            self.last.next = n
            self.last = n

    def search(self, data):
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp

    def insert_after(self, temp, data):
        if temp is not None:
            if self.is_empty():
                n = Node(data)
                n.next = n
                self.last = n
            else:
                n = Node(data, temp.next)
                temp.next = n

    def delete_at_first(self):
        if self.last.next == self.last:
            self.last = None
        else:
            self.last.next = self.last.next.next

    def delete_at_last(self):
        if self.last.next == self.last:
            self.last = None
        else:
            temp = self.last.next
            while temp.next != self.last:
                temp = temp.next
            temp.next = temp.next.next
            self.last = temp

    def delete_after(self, data):
        if data is None:
          pass 
        elif  data.next==data:
            self.last = None  
        else:
            temp = self.last.next
            while temp.next != data:
                temp = temp.next
            temp.next = temp.next.next

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item, end=' ')


list2 = CLL()
list2.insert_at_start(10)
list2.insert_at_last(20)
list2.insert_at_last(30)
list2.insert_at_start(5)
list2.insert_at_start(1)
list2.insert_after(list2.search(20), 25)
list2.print_list()
print()
print(list2.search(20))

list2.delete_at_first()
list2.delete_at_first()
list2.delete_at_last()
list2.delete_at_last()
list2.delete_at_last()
list2.delete_after(list2.search(10))
list2.print_list()
print()
