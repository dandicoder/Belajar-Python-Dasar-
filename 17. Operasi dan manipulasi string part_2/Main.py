# operasi manipulasi string dalam method

## merubah case dari string 

# merubah ke upper case dan lower case
salam = "bro!"
print("normal : " + salam)
print("upper : " + salam.upper())
print("lower : " + salam.lower())

# contoh pengecekan 
salam = "sisssst"
apakah_lower = salam.islower()
print("apakah " + "'" + salam + "'" + " lower case : " + str(apakah_lower))

apakah_upper = salam.isupper()
print("apakah " + "'" + salam + "'" + " upper case : " + str(apakah_upper))

# isalpha()         <--- mengecek semuanya huruf
# isalnum()         <--- huruf dan angka
# isdeccimal()      <--- angka
# isspace()         <--- spaci, tab, newline (\n)
# istitle           <-- semua kata dimulai dari huruf besar

## ngecek komponen startswith() dan endswith()
cek_start = "Tia Monika".startswith("Monika") # akan false karena awalan kata "Tia"
print("start : " + str(cek_start)) 

cek_end = "Tia Monika".endswith("Monika") 
print("start : " + str(cek_end)) 

## penggabungan komponen join() dan split()
pisah = ["aku", "jadi", "duta", "shampo"]
join = " ".join(pisah)
print("join : " + join)

split = join.split(" ")
print("split : " + str(split))

# alokasi karakter rjust(), ljust(), center()
kanan = "dandicode".rjust(10)
print("'"+kanan+"'")

center = "DANDI".center(10, ":")
print("'"+center+"'")

# kebalikannya --> strip()
center = center.strip(":") # menghilangkan tanda :
print("'"+center+"'")
 