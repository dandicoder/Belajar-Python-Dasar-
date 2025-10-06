# Variabel Global dan Local Scope
# Variabel global dapat di akses oleh if dan for kecuali funngsi



def fungsi(nama):
    print(f"nama saya adalah {nama}")

nama = "naruto" # <- global
fungsi(nama)


# def fungsi2():
#     akatsuki = "itachi" <- local scope

# print(akatsuki) tidak bisa diakses di luar 

# cara mengakses di dalam fungsi
nama_mhs = ["dandi", "dudung", "otong"]

def fungsi3():
    global nama_mhs # mendefinisikan global
    nama_mhs[0] = "suparman"
    print(f"{nama_mhs}")

fungsi3()

nama_mhs = ["dandi", "dudung", "otong"]
angka = 0
def fungsi4(nama_ganti):
    global nama_mhs
    global angka
   
    for angka in range(len(nama_mhs)):
        print(f"No. {angka} nama {nama_mhs[angka]}")

        if nama_mhs[angka] == "dandi" :
            nama_mhs[angka] = nama_ganti
        
        print(f"No. {angka} nama {nama_mhs[angka]}")
        angka += 1

fungsi4("jeje")

angka_lama = 2
def angka_ubah(angka_baru):
    global angka_lama
    angka_lama = angka_baru
    print(angka_lama)

print(angka_ubah(10))