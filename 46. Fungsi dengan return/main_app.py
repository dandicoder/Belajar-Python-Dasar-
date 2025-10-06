# fungsi dengan kembalian

def kuadrat(input_angka):
    hasil = input_angka**2
    return hasil

h_kuadrat = kuadrat(3)
a = 10 + h_kuadrat
print(h_kuadrat)
print(a)


def operasi_matika(angka1, angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2
    return angka1, angka2, tambah, kurang, kali, bagi

angka1, angka2, tambah, kurang, kali, bagi = operasi_matika(5,2)

print(f"{angka1} + {angka2} =  {tambah}")
print(f"{angka1} - {angka2} = {kurang}")
print(f"{angka1} x {angka2} = {kali}")
print(f"{angka1} : {angka2} = {bagi}")