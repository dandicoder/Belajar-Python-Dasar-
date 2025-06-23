# OPERASI LIST

data_angka = [0, 3, 3, 9, 4, 3, 5, 5 , 4, 8 , 10]

print(f"data angka = {data_angka}")
print(f"jumlah angka = {len(data_angka)}")
print(f"angka terbesar = {max(data_angka)}")
print(f"angka terkecil = {min(data_angka)}")
print(f"jumlah angka semua = {sum(data_angka)}")

# count angka
angka_3 = data_angka.count(3)
angka_5 = data_angka.count(5)
print(f"jumlah angka 3 = {angka_3}")
print(f"jumlah angka 5 = {angka_5}")

# ambil posisi index pada data list
data = ["naruto", "sasuke", "sakura"]

index_naruto = data.index("naruto")
print(f"index naruto = {index_naruto}")

index_sakura = data.index("sakura")
print(f"index sakura = {index_sakura}")

# mengurutkan list (sort)
data_angka.sort()
print(f"data angka = {data_angka}")

# membalikan list
# data_angka.sort(reverse=True)
# print(f"data angka = {data_angka}")

data_angka.reverse()
print(f"data angka = {data_angka}")