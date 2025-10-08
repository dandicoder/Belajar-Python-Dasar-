# exception akan terjadi saat program mengalami error saat runtime

# contoh sederhana menangkap exception

# angka_input = int(input("masukan angka ? : "))
# hasil = 0
# try:
#     hasil = 10/angka_input
# except:
#     print("jan masun angko nol")

# print(hasil)

# contoh 1

# hasil = None
# while True:
#     input_angka = int(input("Masukan Angka : "))
#     try:
#         hasil = 10/input_angka
#         isDone = input("Lagi ? (y/n) : ")
#         print(hasil)
#         if isDone == "n" :
#             break
    
#     except:
#         print("jan masun angko nol")

# print(hasil)

# contoh 2
while True :
    try:
        with open("data.txt", mode="r") as file:
            print(file.read())
        break
    except:
        print("file tidak ditemukan")
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("File Baru")
        break
        