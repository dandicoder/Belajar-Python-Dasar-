def ucap_salam(nama):
    print(f"selamat datang {nama}")

ucap_salam("dandi")


# fungsi tambah

def tambah(angka1, angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka1} = {hasil}")

tambah(2,5)
tambah(2,100)

# fungsi argumen list

def say_hi(list_peserta):
    daftar_peserta = list_peserta.copy()

    for peserta in daftar_peserta :
        print(f"peserta {peserta}")

anggota_boyband= ["gorgon", "dinosaurus", "ayip"]
say_hi(anggota_boyband)