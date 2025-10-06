import datetime as dt
import os
import string
import random

temp_mahasiswa = {
        "nama" : "",
        "npm" : "",
        "sks" : "",
        "tanggal_lahir" : dt.datetime(1111, 1, 1)
    }   

mahasiswa = {} # dictionary kosong

while True :
    os.system("clear")

    data_mhs = dict.fromkeys(temp_mahasiswa.keys()) # duplikat template
    # input 
    data_mhs["nama"] = input("MASUKAN NAMA KAU ANJING : ")
    data_mhs["npm"] = input("MASUKAN NPM KAU ANJING : ")
    data_mhs["sks"] = input("MASUKAN SKS KAU ANJING : ")
    tahun = int(input("MASUKAN TAHUN LAHIR : "))
    bulan = int(input("MASUKANK BULAN LAHIR : "))
    tanggal = int(input("MASUAN TANGGAL LAHIR : "))
    data_mhs["tanggal_lahir"] = dt.datetime(tahun,bulan,tanggal)


    ID = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    mahasiswa.update({ID : data_mhs})
    print("\n")

    print(f"{'DATA MAHASISWA':^70}")
    print(f"{'UNIK TAHUN 2025':^70}")
    print("-"*70)

    print(f"{"ID":<6} | {"NAMA":<10} | {"NPM":<9} | {"SKS":<20} | {"TANGGAL LAHIR":<25}")
    print(70*"-")     

    for mhs in mahasiswa :
        ID = mhs
        NAMA = mahasiswa[ID]["nama"]
        NPM = mahasiswa[ID]["npm"]
        SKS = mahasiswa[ID]["sks"]
        TANGGAL_LAHIR = mahasiswa[ID]["tanggal_lahir"].strftime("%x")
    
        print(f"{ID:<6} | {NAMA:<10} | {NPM:<9} | {SKS:<20} | {TANGGAL_LAHIR:<25}")

    print("\n")
    is_done = input("ULANGI LAGI ? y/n : ")

    if is_done == "n" or is_done != "y" :
        break