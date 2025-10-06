# kwargs 

def fungsi(nama, umur, tb): # fungsi biasa
    print(f"{nama} umur {umur} tinggi badan {tb}")

fungsi("dandi", 25, 154)

def math(*args, **kwargs) -> int:
    output=0
    if kwargs["optional"] == "tambah" :
        for angka in args :
            output += angka
    elif kwargs["optional"] == "kali" :
        output = 1
        for angka in args :
            output *= angka
    else :
        print("tidak ada operasi")

    return output

hasil = math(2,2,3, optional = "tambah" ) # optional = "tambah" penggunaan kwargs
print(f"hasil penjumlahan {hasil}")

hasil = math(2,2,3, optional = "kali" )
print(f"hasil perkalian {hasil}")