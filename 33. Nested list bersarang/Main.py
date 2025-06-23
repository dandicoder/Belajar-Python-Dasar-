data_0 = [1,2]
data_1 = [3,4,5]

data_list_2d = [data_0, data_0, 9,3,4]
print(f"data list 2d = {data_list_2d}")

# contoh kasus
peserta_1 = ["naruto", 20, "laki-laki"]
peserta_2 = ["sasuke", 22, "laki-laki"]
peserta_3 = ["sakura", 19, "perempuan"]

data_peserta = [peserta_1, peserta_2, peserta_3]
print(f"data peserta = {data_peserta}\n")

for peserta in data_peserta :
    print(f"Nama\t : {peserta[0]}")
    print(f"Umur\t : {peserta[1]}")
    print(f"Gender\t : {peserta[2]}\n")

# dengan reference
list_copy = data_peserta.copy()
print(f"data copy\t : {list_copy}")
peserta_2[1] = "sai"
print(f"data copy\t : {list_copy}")
print(f"data copy\t : {data_peserta}")