class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def addElement(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = newNode

    def deleteElement(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def insertAfter(self, prevNode, data):
        if prevNode is None:
            print("Node sebelumnya tidak ada.")
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    def searchElement(self, key):
        current = self.head
        position = 1
        while current is not None:
            if current.data == key:
                return f"Elemen {key} ditemukan di posisi {position}"
            current = current.next
            position += 1
        return f"Elemen {key} tidak ditemukan dalam linked list"

if __name__ == "__main__":
    linkedList = LinkedList()

    linkedList.addElement(1)
    linkedList.addElement(2)
    linkedList.addElement(3)

    print("Linked list awal: ", end="")
    linkedList.printList()

    # Menambahkan elemen baru
    linkedList.addElement(4)
    print("Setelah menambahkan elemen 4: ", end="")
    linkedList.printList()

    # Menghapus elemen
    linkedList.deleteElement(2)
    print("Setelah menghapus elemen 2: ", end="")
    linkedList.printList()

    # Menyisipkan elemen
    linkedList.insertAfter(linkedList.head.next, 5)
    print("Setelah menyisipkan elemen 5 setelah 1: ", end="")
    linkedList.printList()

    # Mencari elemen
    key = 3
    print(linkedList.searchElement(key))
    


