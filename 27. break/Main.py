# BREAK

data_integer = int(input("Masukan angka 1 - 10 : "))
angka = 0

while True :
    angka += 1
    print(f"count : {angka}")

    if angka == data_integer :
        print(f"cukup sampai di angka {data_integer}")
        break # mengakhiri program


print("selesai")