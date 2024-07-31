def faktorial(n):
    if n > 2:
        return n * faktorial(n-1)
    return 2

n = int(input("Masukkan Angka = "))
faktorial = faktorial(n)

print("Nilai Faktorial dari ", faktorial)