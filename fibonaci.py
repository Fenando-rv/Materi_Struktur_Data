def fibonaci(n):
    if n <= 1:
        return n
    else:
        return fibonaci(n-1) + fibonaci(n-2)

# Ambil input dari pengguna untuk jumlah bilangan dalam deret Fibonacci
n = int(input("Masukkan jumlah bilangan dalam deret Fibonacci: "))

# Cetak deret Fibonacci menggunakan pendekatan rekursif
print("Deret Fibonacci:")
for i in range(n):
    print(fibonaci(i), end=" ")