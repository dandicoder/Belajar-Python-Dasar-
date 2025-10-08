# Membuat exception

from numbers import Number


def tambah(a, b):
    if not isinstance(a, Number) or not isinstance(b, Number):
        raise "masukan angka "
    return a+b

print(tambah(3,4))

angka =0
try:
    hasil = 10/0
    print(hasil)
except ZeroDivisionError as err_message: # Exeptiont
    print(err_message)
