# menggunakan write

# akan menimpa/ overwrite
with open("data-1.txt", mode="w", encoding="UTF-8") as file:
    file.write("Data 1")

with open("data-1.txt", mode="w", encoding="UTF-8") as file:
    file.write("Data 2")

with open("data-1.txt", mode="w", encoding="UTF-8") as file:
    file.write("overwrite")

# menggunakan append
with open("data-2.txt", mode="w", encoding="UTF-8") as file:
    file.write("Data Tambah 1\n")

with open("data-2.txt", mode="a", encoding="UTF-8") as file:
    file.write("Data Tambah 2\n")

with open("data-2.txt", mode="a", encoding="UTF-8") as file:
    file.write("Data Tambah 3\n")

# menggunakan r+

with open("data-3.txt", mode="w", encoding="utf-8") as file:
    file.write("Membuat File 3\n")

with open("data-3.txt", mode="r+", encoding="utf-8") as file: # r+ harus ada file 
    file.write("Menggunakan R+ - 1\n")
    file.write("Menggunakan R+ - 2\n")
    file.write("Menggunakan R+ - 3\n")
    file.write("Menggunakan R+ - 4\n")

with open("data-3.txt", mode="r+", encoding="utf-8") as file:
    # print(file.read())
    file.write("Menggunakan R+ - 5\n")
    print(file.read())
