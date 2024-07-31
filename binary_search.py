def binary_search(data, target):
  low = 0
  high = len(data) - 1

  while low <= high:
    mid = (low + high) // 2
    if data[mid] == target:
      return mid
    elif data[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

# Contoh penggunaan
data = [1, 5, 8, 12, 16, 20, 24, 28]
print("Isi dari array = ", data)
data.append(30)
print(data)

data.insert(5,18)
print(data)
data.remove(5)
print(data)

target = int(input("Masukkan Nilai yang di cari = "))
index = binary_search(data, target)

if index != -1:
  print("Target ditemukan pada indeks:", index)
else:
  print("Target tidak ditemukan dalam daftar")
