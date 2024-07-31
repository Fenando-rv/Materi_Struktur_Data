class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue(60)
queue.enqueue(20)
queue.enqueue(50)
queue.enqueue(30)
queue.enqueue(40)

print("Seluruh elemen dalam queue:", queue.items)  # Output: [2, 3]
print("Elemen pertama:", queue.peek())  # Output: 1

queue.dequeue()
print("Elemen pertama setelah dequeue:", queue.peek())  # Output: 2

print("Jumlah elemen dalam queue:", queue.size())  # Output: 2

print("Seluruh elemen dalam queue:", queue.items)  # Output: [2, 3]
