def pangkat(x, n):
    if n == 0:
        return 1
    else:
        return x * pangkat(x, n - 1)
# Contoh penggunaan
bilangan = 2
pangkatnya = 5
hasil_pangkat = pangkat(bilangan, pangkatnya)
print(bilangan, "pangkat", pangkatnya, "adalah", hasil_pangkat)
