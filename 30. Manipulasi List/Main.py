## Operasi List


# index dari list 0 (-3), 1 (-2), 2 (-1)
data = ["naruto", "sasuke", "sakura"]

# mengambil data
data_2 = data[1]
print(data_2)

data_terakhir = data[-1]
print(data_terakhir)

# menampilkan info panjang data list
panjang = len(data)
print(panjang)

## Manipulasi data list
# 1. Menambahkan Item pada List
# 2. Menghapus Item pada List
# 3. Mengganti Item pada List
# 4. Menampilkan Item pada List
# 5. Menampilkan Semua Item pada List

print("=== Menambahkan Item pada List ===")

# menambahkan item pada list sesuai posisi
data.insert(1, "kakashi")
print(data)

# menambahkan item pada list di akhir
data.append("sai")
print(data)

#  menggabungkan list dengan list
data_guy = ["guy", "rock lee", "neji"]
data.extend(data_guy)
print(data)

# merubah data
data[1] = "jiraya"
print(data)

# menghapus data
data.remove("sasuke")
# data.remove("Sasuke") akan error tidak sesuai dengan string data
print(data)

# menghapus data paling akhir
data_hilang = data.pop()
print(data)

print(data_hilang)