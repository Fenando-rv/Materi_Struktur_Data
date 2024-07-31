def selection_sort(data):
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
                
        # Tukar elemen terkecil yang ditemukan dengan elemen pertama
        data[i], data[min_idx] = data[min_idx], data[i]

# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90]
print("Array sebelum diurutkan:")
print(data)

selection_sort(data)

print("Array setelah diurutkan menggunakan Selection Sort:")
print(data)
