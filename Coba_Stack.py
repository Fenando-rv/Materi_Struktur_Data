class Stack:
    def __init__(self) :
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]

    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items

#inputan
stack = Stack()
stack.push(50)
stack.push(70)
stack.push(60)
stack.push(80)
stack.push(90)

print("Semua Elemen Stack:", stack.display())

print("Elemen teratas:", stack.peek())  # Output: 3

stack.pop()
print("Elemen teratas setelah pop:", stack.peek()) # Output: 2
print("Semua Elemen Stack:", stack.display())




