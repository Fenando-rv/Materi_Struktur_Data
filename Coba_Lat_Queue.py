# Pendefinisian kelas Queue
class Queue:
    def __init__(self):
        self.front = -1
        self.rear = -1
        self.data = [0] * 5  # Maksimum 5 elemen dalam queue

    # Fungsi untuk mengecek apakah queue penuh
    def is_full(self):
        return self.rear == 4

    # Fungsi untuk mengecek apakah queue kosong
    def is_empty(self):
        return self.front == -1 or self.front > self.rear

    # Fungsi untuk menambahkan data ke dalam queue
    def enqueue(self, dta):
        if self.is_full():
            print("Maaf, queue penuh")
        else:
            if self.front == -1:  # Jika queue kosong
                self.front = 0
            self.rear += 1
            self.data[self.rear] = dta

    # Fungsi untuk mengambil data dari queue
    def dequeue(self):
        if self.is_empty():
            print("Data telah kosong!")
        else:
            print("Data yang terambil:", self.data[self.front])
            self.front += 1
            if self.front > self.rear:  # Reset kondisi jika queue kosong
                self.front = self.rear = -1

    # Fungsi untuk mencetak isi queue
    def print_queue(self):
        print("\nData yang terdapat dalam queue:")
        print("--------------------------------")
        if not self.is_empty():
            for i in range(self.front, self.rear + 1):
                print(self.data[i], end="   ")
        print("\n")

    # Fungsi untuk membersihkan queue
    def clear(self):
        self.front = self.rear = -1
        print("\nSekarang queue kosong")


# Fungsi utama
def main():
    queuebaru = Queue()

    while True:
        print("\t PROGRAM QUEUE")
        print("\t===============")
        print("Menu : ")
        print("1. Dequeue")
        print("2. Enqueue")
        print("3. Cetak")
        print("4. Bersihkan queue")
        print("5. Exit")

        menu = input("Menu pilihan Anda : ")

        if menu == '1':
            queuebaru.dequeue()
        elif menu == '2':
            dta = float(input("\nTambah Data\n-----------\nData yang akan disimpan di queue : "))
            queuebaru.enqueue(dta)
        elif menu == '3':
            queuebaru.print_queue()
        elif menu == '4':
            queuebaru.clear()
        elif menu == '5':
            break
        else:
            print("Menu tidak valid")


if __name__ == "__main__":
    main()
