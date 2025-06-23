data_angka = [3,5,4,3,2,1,0,6,9]

# menggunakan for
print(10*"="+ " FOR LOOP " + 10*"=")
for angka in data_angka:
    print(f"angka : {angka}")

print("\n")

peserta = ["naruto", "sasuke", "sakura", "kakasi"]

for nama in peserta :
    print(f"nama : {nama}")
print(30*"="+ "\n")

# menggunakan while
print(10*"="+ " WHILE LOOP " + 10*"=")

peserta = ["naruto", "sasuke", "sakura", "kakasi"]

panjang = len(peserta)
i = 0

while i < panjang :
    print(f"nama : {peserta[i]}")
    i += 1

print(30*"="+ "\n")

# menggunakan list comprehension
print(10*"="+ " COMPREHENSION " + 10*"=")
data_list = ["naruto", "sasuke", "sakura", "kakasi"]

[print(f"nama : {i}") for i in data_list]

data_kuadrat = [i**2 for i in data_angka]
print("\n")

print(f"data angka\t : {data_angka}")
print(f"data kuadrat\t : {data_kuadrat}\n")

print(30*"="+ "\n")



# menggunakan list enumerate
print(10*"="+ " ENUMERATE " + 10*"=")
data_list = ["naruto", "sasuke",3,6,4, "sakura", "kakasi"]

for index, data in enumerate(data_list):
    print(f"indek ke : {index} dengan data : {data}")

print(30*"="+ "\n")