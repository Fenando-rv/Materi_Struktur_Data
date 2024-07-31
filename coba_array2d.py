array_2d = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
baris = len(array_2d)
kolom = len(array_2d[0]) if array_2d else 0
Tampil = array_2d[2][1]
Total = sum(sum(row) for row in array_2d)
Tertinggi = max(max(row) for row in array_2d)

print("Baris=", baris)
print("Kolom=", kolom)
print("Tampil = ", Tampil)
print("Total = ", Total)
print("Tertinggi = ", Tertinggi)