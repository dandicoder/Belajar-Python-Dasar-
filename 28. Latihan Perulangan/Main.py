# latihan pengulangan

sisi = 6

# menggunakan for
print(10*"=" + "Menggunakan For" + 10*"=")
count = 1
for i in range(sisi):
    print("*"*count)
    count += 1
print(10*"=" + "Akhir" + 10*"=" + "\n")

# menggunakan while
print(10*"=" + "Menggunakan While" + 10*"=")
count = 1
while True:
    print("*"*count)
    count += 1
    
    if count > sisi :
        break
         
print(10*"=" + "Akhir" + 10*"=" + "\n")
    
# ganjil
print(10*"=" + "Ganjil" + 10*"=")
count = 1
while True:
    if count%2 :
        print("*"*count)
        count += 1
    else:
        count += 1
        continue


    if count > sisi :
        break
         
print(10*"=" + "Akhir" + 10*"=" + "\n")

# piramid
print(10*"=" + "Piramid" + 10*"=")
count = 0
spasi = int(sisi/2)
while True:
    if count%2 :
        print(" "*spasi, "+" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue


    if count > sisi :
        break
         
print(10*"=" + "Akhir" + 10*"=" + "\n")

# piramid
print(10*"=" + "Piramid" + 10*"=")
count = 0
spasi = int(sisi/2)
while True:
    if count%2 :
        print(" "*spasi, "+" * count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue


    if count > sisi :
        break

count = 1
spasi = int((sisi/2) - 2)
while True:
    if sisi%2:
        print(" " * spasi, "+" * sisi)
        spasi += 1
        sisi -= 1
    else :
        sisi -= 1
        continue

    if sisi < count :
        break
         
print(10*"=" + "Akhir" + 10*"=" + "\n")