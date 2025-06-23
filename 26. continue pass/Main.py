# continue , pas dan break

# pass ==> berfungsi sebagai dummy

angka = 0

while angka < 5:
    angka += 1
    print(f"angka {angka}") # aksi 1

    if angka == 3:
        # pass   
        continue # melanjutkan aksi 1
        print("kenalkan aku tiga") # aksi 2

    print("nicee")


print("success")