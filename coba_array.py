my_array = [10, 20, 30, 40, 50]

pertama = my_array[3]
terakhir = my_array[-1]

my_array.append(60)
my_array.insert(0, 5)
my_array.remove(30)

Total = sum(my_array)
N_Tertinggi = max(my_array)
N_Rendah = min(my_array)

print("Tampil array= ", my_array)
print("Indeks Pertama = ", pertama)
print("Indeks terakhir = ", terakhir)

print("Total nilai = ", Total)
print("nilai Tertinggi= ", N_Tertinggi)
print("nilai TerRendah= ", N_Rendah)
