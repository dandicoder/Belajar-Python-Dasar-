# __main__ adalah top level environment code

# __name__ = __main__ akan terjadi ada di program utama

# __name__ pada file program utama
print(f"nilai __name__ pada file main_app.py : {__name__}")

# __name__ pada file program eksternal
import fungsi

# contoh penggunaan __main__

# deklarasi
def tambah(a:int, b:int) -> int :
    return a+b

# fungsi utama
if __name__ == "__main__" :
    angka1 = 4
    angka2 = 2
    hasil = tambah(angka1, angka2)
    print(f"hasil {angka1} + {angka2} = {hasil}")

# import package
import package # -> cara manggil $ python -m package