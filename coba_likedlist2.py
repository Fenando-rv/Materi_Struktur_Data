#inisialisasi linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

#Menambah dan Menyisipkan
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
                
#menampilkan  
    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


# Membuat objek LinkedList
myLinkedList = LinkedList()

# Menambahkan node-node 50, 35, 15, 25
myLinkedList.add_at_beginning(25)
myLinkedList.add_at_beginning(15)
myLinkedList.add_at_beginning(35)
myLinkedList.add_at_beginning(50)


# Mencetak linked list
print("Linked List:")
myLinkedList.traverse()



# Mencetak linked list setelah penambahan
print("Linked List setelah penambahan:")
myLinkedList.traverse()