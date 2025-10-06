# *args 

def fungsi(nama, umur, tb): # fungsi biasa
    print(f"{nama} umur {umur} tinggi badan {tb}")

fungsi("dandi", 25, 154)

def fungsi(data_list) : # menggunakan tuple
    data = data_list.copy()
    nama = data[0]
    umur = data[1]
    tb = data[2]
    print(f"{nama} umur {umur} tinggi badan {tb}")

fungsi(["dandi", 25, 154])

def fungsi(*biodata) : # args menggunakan *
    nama = biodata[0]
    umur = biodata[1]
    tb = biodata[2]
    print(f"{nama} umur {umur} tinggi badan {tb}")

fungsi("dandi saja", 25, 154)