#  Variabel adalah tempat penyimpan data
#  Variabel di Python menggunakan huruf kecil semua
#  Variabel di Python menggunakan underscore untuk pemisah kata
#  Variabel di Python menggunakan angka untuk pemisah kata
# di python tidak menggunakan deklarasi (int a = 12) melainkan (a = 12)


a = 10 # assignment (penugasan) atau variabel yang akan menyimpan nilai ke memori
x = 5
panjang = 1000

print("nilai a : ", a)
print("nilai x : ", x)
print("nilai panjang : ", panjang)

# penamaan 
nilai_y = 15 # dengan menggunakan underscore
juta10 = 10000000 # dengan menggunakan angka
nilaiZ = 17.5 # dengan menggunakan angka

print("nilai y : ", nilai_y)
print("nilai juta10 : ", juta10)
print("nilai Z : ", nilaiZ)

# assigment indirect
b = a
print("nilai b : ", b)

a = 50
print("nilai a : ", a)
print("nilai b : ", b)