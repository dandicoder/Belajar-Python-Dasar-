# Latihan list

list_buku = []



print(list_buku)

while True :
    nama_buku = input("Masukkan nama buku\t : ")
    judul_buku = input("Masukkan judul buku\t : ")

    buku_baru = [nama_buku, judul_buku]
    list_buku.append(buku_baru)


    for i, buku in enumerate(list_buku) :
        print(f"{i+1} | {buku[0]} | {buku[1]}")

    lanjut = input("Lanjutkan? (y/n) : ")
    if lanjut == "n" :
        break

print(20*"=", "PROGRAM SELESAI", 20*"=")