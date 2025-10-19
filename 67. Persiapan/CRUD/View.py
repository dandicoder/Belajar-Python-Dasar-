from . import Operasi
from .Utils import form_input

# Delete Data
def delete_console():
    read_console()

    while(True):
        no_buku = int(input("Masukan Nomor Buku yang di Delete ? : "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            data_break = data_buku.split(",")
            pk = data_break[0]
            date = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            print("\n"+"="*100)
            print("Data yang akan di hapus!\n")
            print(f"1. Penulis\t : {penulis:.40}")
            print(f"2. Judul\t : {judul:.40}")
            print(f"3. Tahun\t : {tahun:4}")
            is_done = input("Apakah Anda Yakin ? (y/n) :")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_buku)
                break
        else:
            print("nomor tidak valid, masukan nan botuoool!!!")

# Menedit data
def update_console():
    read_console()

    while(True):
        no_buku = int(input("Masukan Nomor Buku ? : "))
        data_buku = Operasi.read(index=no_buku)
        if data_buku:
            break
        else:
            print("nomor tidak valid, masukan nan botuoool!!!")

    data_break = data_buku.split(",")
    pk = data_break[0]
    date = data_break[1]
    penulis = data_break[2][:-1]
    judul = data_break[3][:-1]
    tahun = data_break[4][:-1]

    while(True):
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah?")
        print(f"1. Penulis\t : {penulis:.40}")
        print(f"2. Judul\t : {judul:.40}")
        print(f"3. Tahun\t : {tahun:4}")

        user_option = input("Pilih Nomor [1,2,3] : ")

        match user_option:
            case "1" : penulis = input("Masukan Nama Penulis : ")
            case "2" : judul = input("Masukan Nama Judul : ") 
            case "3" : 
                while(True):
                    try:
                        tahun = int(input("Masukan Nama Tahun : "))
                        if len(str(tahun)) == 4 :
                            break
                        else:
                            print("Masukan Tahun Dengan Benar (YYYY) !")
                    except:
                        print("Masukan Tahun Dengan Benar (YYYY) !")
            case _: print("index tidak cuocookk")

        is_done = input("Apakah Sudah Selesai ? (y/n) :")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_buku,pk,date,penulis,judul,tahun)
    
# Menambah Data
def create_console():
    print(f"\n\n"+ "="*100)
    print("Silahkan Menambahkan Data Buku Baru\n")

    penulis, judul, tahun = form_input()

    Operasi.create(penulis, judul, tahun)
    
    print(f"\nBerikut Data Baru Anda!!!\n")

    read_console()

# Membaca Data
def read_console():
    data_file = Operasi.read()

    index = "NO"
    judul = "JUDUL"
    penulis = "PENULIS"
    judul = "JUDUL"
    tahun = "TAHUN"

    # header
    print("\n" + "="*100)

    print(f"{index:^4} | {penulis:^40} | {judul:^40} | {tahun:^5}")
    print("-"*100)

    # data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]

        print(f"{index + 1:4} | {penulis:.40} | {judul:.40} | {tahun:5}", end="")

    # footer
    print("="*100 + "\n")