#  Masukan Angka

# 1. -------- 0 +++++++ 5 -------- 8 +++++++ 11 --------
# 2. +++++++ 0 -------- 5 +++++++ 8 -------- 11 +++++++

# SOAL NO 1

print("\n",10*"=", " Soal No 1", 10*"=")

masukanAngka = float(input("Masukan Angka, \nLebih dari 0 dan kurang dari 5 \natau lebih dari 8 dan kurang dari 11\n: "))

lebihDari0 = masukanAngka > 0 
print("Lebih dari 0 = ", lebihDari0)

kurangDari5 = masukanAngka < 5
print("Kurang dari 5 = ", kurangDari5)

lebihDari8 = masukanAngka > 8
print("Lebih dari 8 = ", lebihDari8)

kurangDari11 = masukanAngka < 11
print("Kurang dari 11 = ", kurangDari11) 

isCorrect = lebihDari0 and kurangDari5 or lebihDari8 and kurangDari11

print("angka yang anda masukan = ", isCorrect)


# SOAL NO 2

print("\n",10*"=", " Soal No 2", 10*"=")

masukanAngka = float(input("Masukan Angka, \nkurang dari 0 atau lebih dari 5 \ndan kurang dari 8 atau lebih dari 11\n: "))

kurangDari0 = masukanAngka < 0 
print("Lebih dari 0 = ", lebihDari0)

lebihDari5 = masukanAngka > 5
print("Kurang dari 5 = ", kurangDari5)

kurangDari8 = masukanAngka < 8
print("Lebih dari 8 = ", lebihDari8)

lebihDari11 = masukanAngka > 11
print("Kurang dari 11 = ", kurangDari11) 

isCorrect = kurangDari0 or lebihDari5 and kurangDari8 or lebihDari11

print("angka yang anda masukan = ", isCorrect)