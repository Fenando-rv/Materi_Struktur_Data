# Pendefinisian kelas Stack
class Stack:
    def __init__(self):
        self.top = -1
        self.data = [0] * 5  # Maksimum 5 elemen dalam stack

    # Fungsi untuk mengecek apakah stack penuh
    def is_full(self):
        return self.top == 4

    # Fungsi untuk mengecek apakah stack kosong
    def is_empty(self):
        return self.top == -1

    # Fungsi untuk menambahkan data ke dalam stack
    def push(self, dta):
        if self.is_full():
            print("Maaf, stack penuh")
        else:
            self.top += 1
            self.data[self.top] = dta

    # Fungsi untuk mengambil data dari stack
    def pop(self):
        if self.is_empty():
            print("Data telah kosong!")
        else:
            print("Data yang terambil:", self.data[self.top])
            self.top -= 1

    # Fungsi untuk mencetak isi stack
    def print_stack(self):
        print("\nData yang terdapat dalam stack:")
        print("--------------------------------")
        for i in range(self.top + 1):
            print(self.data[i], end="   ")
        print("\n")

    # Fungsi untuk membersihkan stack
    def clear(self):
        self.top = -1
        print("\nSekarang stack kosong")


# Fungsi utama
def main():
    stackbaru = Stack()

    while True:
        print("\t PROGRAM STACK")
        print("\t===============")
        print("Menu : ")
        print("1. Pop stack")
        print("2. Push stack")
        print("3. Cetak")
        print("4. Bersihkan stack")
        print("5. Exit")

        menu = input("Menu pilihan Anda : ")

        if menu == '1':
            stackbaru.pop()
        elif menu == '2':
            dta = float(input("\nTambah Data\n-----------\nData yang akan disimpan di stack : "))
            stackbaru.push(dta)
        elif menu == '3':
            stackbaru.print_stack()
        elif menu == '4':
            stackbaru.clear()
        elif menu == '5':
            break
        else:
            print("Menu tidak valid")


if __name__ == "__main__":
    main()
