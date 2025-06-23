#  format string

# contoh generic
## string 
nama = "Dandi"
format_str = f"Nama saya, {nama}"
print(format_str)

## boolean
boolean = False
format_str = f"ini boolean : {boolean}"
print(format_str)

## angka
# bilangan bulat
angka = 23
format_str = f"angka : {angka:d}" # d = pembulatan
print(format_str)

# bilangan dengan ordo
angka = 200000000
format_str = f"bapo banyak : {angka:,}" # 
print(format_str)

# bilangan decimal
angka = 2005.63444
format_str = f"angka desimal : {angka:.2f}" # menampilkan 2 angka belakang koma
print(format_str)

# menampilkan leading sero
angka = 2005.6344
format_str = f"angka desimal : {angka:010.4f}"
print(format_str)

# menampilkan tanda + atau -
angka_plus = 10
angka_minus = -10.389

format_plus = f"plus : {angka_plus:+d}"
format_minus = f"minus : {angka_minus:+.2f}"
print(format_plus)
print(format_minus)

# persentase
persen = 0.034
format_str = f"persentase : {persen:.2%}"
print(format_str)


## melakukan operasi aritmatika didalam placeholder
harga = 50000
total = 3

format_str = f" {harga} x {total} : Rp. {harga * total}"
print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 255
bil_binary = f"bilangan binary : {bin(angka)}"
bil_octa = f"bilangan binary : {oct(angka)}"
bil_hexadecimal = f"bilangan binary : {hex(angka)}"

print(bil_binary)
print(bil_octa)
print(bil_hexadecimal)