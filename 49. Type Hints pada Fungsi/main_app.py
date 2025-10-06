# fungsi menggunakan tipe hints
# berfungsi untuk menentukan type argumen dan return


# def studi_kasus(argument):
#     pangkat = argument**2
#     print(pangkat)

# studi_kasus(15)
# studi_kasus("ucup")
# studi_kasus(True)

def pangkat_sepuluh(argument:int) -> int :
    pangkat = 10**argument
    return pangkat

hasil = pangkat_sepuluh(2)
print(hasil)

def display(argument:str) -> str :
    print(f"hello {argument}")

display("dandi")

# so type hints berfungsi memberitahukan argumen fungsi itu tipenya apa