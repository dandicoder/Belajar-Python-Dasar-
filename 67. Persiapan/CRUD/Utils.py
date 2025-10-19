import random
import string

def random_string(panjang:int) -> str:
    string_random = "".join(random.choice(string.ascii_letters) for i in range(panjang))
    return string_random

def form_input():
    penulis = input("Masukan Nama Penulis : ")
    judul = input("Masukan Nama Judul : ")
    while(True):
        try:
            tahun = int(input("Masukan Nama Tahun : "))
            if len(str(tahun)) == 4 :
                break
            else:
                print("Masukan Tahun Dengan Benar (YYYY) !")
        except:
            print("Masukan Tahun Dengan Benar (YYYY) !")

    return penulis, judul, tahun