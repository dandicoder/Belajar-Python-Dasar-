# fungsi biasa

def f_pangkat(angka,n) :
    return angka**n

hasil = f_pangkat(5,2)
print(f"hasil dari pangkat : {hasil}")

# memakai lambda
hasil = lambda angka, n: angka**n
print(f"hasil dari lambda pangkat : {hasil(5,2)}")

# sorting
data_list = ["naruto", "kakasi", "sakura"]
data_list.sort()
print(f"data list di sorting : {data_list}")



# sorting memakai nama panjang
data_list = ["dandi", "cr", "messi"]
def panjang_nama(nama):
    return len(nama)

data_list.sort(key=panjang_nama)
print(f"data list di sorting panjang nama : {data_list}")

data_list = ["dandi", "cr", "messi"]
data_list.sort(key=lambda p_nama:len(p_nama))
print(f"data list di sorting panjang nama lambda : {data_list}")

# filter data
angka_list = [1,2,3,4,5,6,7,8,9,10]

def filter_angka(angka):
    return angka < 5

angka_list_baru = list(filter(filter_angka, angka_list))
print(f"filter angka : {angka_list_baru}")

l_angka_list_baru = list(filter(lambda angka: angka<3, angka_list))
print(f"filter angka lambda : {l_angka_list_baru}")

# 

angka_list = [1,2,3,4,5,6,7,8,9,10]

data_genap = list(filter(lambda n:(n%2==0), angka_list ))
print(data_genap)

data_ganjil = list(filter(lambda n:(n%2!=0), angka_list ))
print(data_ganjil)

data_kelipatan3 = list(filter(lambda n:(n%3==0), angka_list ))
print(data_kelipatan3)

# dengan currying menjadi

def pangkat(n) :
    return lambda angka: angka**n

hasil = pangkat(2)
print(f"hasil pangkat 2, {hasil(10)}")

print(f"hasil pangkat bebas : {pangkat(2)(3)}")