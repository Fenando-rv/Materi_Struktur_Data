class PriorityQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item, priority):
        self.items.append((item, priority))
        self.items.sort(key=lambda x: x[1])  # Urutkan berdasarkan prioritas

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[0]

    def peek(self):
        if not self.is_empty():
            return self.items[0][0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

priority_queue = PriorityQueue()

priority_queue.enqueue("Task 1", 2)
priority_queue.enqueue("Task 2", 1)
priority_queue.enqueue("Task 3", 3)

print("Elemen pertama pada Priority Queue:", priority_queue.peek())  # Output: Task 2

priority_queue.dequeue()
print("Elemen pertama setelah dequeue:", priority_queue.peek())  # Output: Task 1

print("Seluruh elemen dalam Priority Queue:", priority_queue.items)  # Output: [('Task 1', 2), ('Task 3', 3)]
