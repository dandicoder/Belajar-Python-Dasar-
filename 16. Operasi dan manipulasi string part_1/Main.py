# operasi manipulasi string

# menyambung string (concatenate)
nama_pertama = "ndat"
nama_tengah = "aka"
nama_terakhir = "dan"

nama_lengkap = nama_pertama + " " + nama_tengah + " " + nama_terakhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari " + nama_lengkap + " = " + str(panjang))

# operator untuk string

# mengecek apakah ada komponen char atau string di string
D = "D"
status = D in nama_lengkap
print(D + " ada di " + " '"+ nama_lengkap + "' " + " = " + str(status))

D = "D"
status = D not in nama_lengkap
print(D + " tidak ada di " + " '"+ nama_lengkap + "' " + " = " + str(status))

d = "d"
status = d in nama_lengkap
print(d + " ada di " + " '"+ nama_lengkap + "' " + " = " + str(status))

# mengulang string
print("wk"*10)
print(5*"wk")

# indexing
print("index ke-0 dari" + " '"+ nama_lengkap + "' " + " : " + nama_lengkap[0] )
print("index 0 sampai 4" + " '"+ nama_lengkap + "' " + " : " + nama_lengkap[0:5] ) # index 0 sampai (:) sebelum lima (4)
print("index ke-[0, 2, 4, 6, 8, 10]" + " '"+ nama_lengkap + "' " + " : " + nama_lengkap[0:11:2] ) # increment 2

# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))


ascii_code = ord("i")
print("ASCII CODE dari i adalah : " + str(ascii_code))

data = 7
print("char untuk ASCII CODE dari " + str(data) + " adalah : " + chr(data))
dandi = 6897110100105

# operator dalam method
data = "skyline - love lesson no 1"
jumlah = data.count("o")
print("jumlah o dalam " + data + " = " + str(jumlah))