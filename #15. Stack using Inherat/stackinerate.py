import singly_list as si


class stack(si.SLL):
    def __init__(self):
        super().__init__()
        self.item_count = 0

    def push(self, data):
        self.item_count += 1
        self.insert_at_start(data)

    def pop(self):
        if not self.is_empty():
            self.item_count -= 1
            return self.delete_first()

        else:
            raise IndexError("Stack is empty")

    def peek(self):
        return self.start.item

    def size(self):
        return self.item_count


list4 = stack()
list4.push(10)
list4.push(20)
list4.push(30)
list4.push(40)
list4.push(50)
list4.push(60)

print("Top of the stack: ", list4.peek())
print("Delete the element: ", list4.pop())
print("Delete the element: ", list4.pop())
print("Top of the stack: ", list4.peek())

print("Size of the element: ", list4.size())
