#inisialisasi linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, prev_data, new_data):
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        print("Node dengan nilai", prev_data, "tidak ditemukan dalam linked list.")

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


#Objek Baru
MyLinkedList = LinkedList()

#Menambahkan Node baru
MyLinkedList.add_at_beginning(15)
MyLinkedList.add_at_beginning(20)
MyLinkedList.add_at_beginning(30)
MyLinkedList.add_at_beginning(45)
#Menampilkan
print("Isi node = ")
MyLinkedList.traverse()

#menyisipkan
MyLinkedList.insert_after(20, 25)
#Menampilkan
print("Isi node setelah di sisipkan = ")
MyLinkedList.traverse()

