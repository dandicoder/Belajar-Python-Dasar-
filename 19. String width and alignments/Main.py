# string width dan alignment

# Data
data_nama = "dandi"
data_umur = 25
data_tinggi = 156
data_nomor_sepatu = 38

# string standar
print(5*"="+"DATA STRING STANDAR"+5*"=")
data = f"nama : {data_nama}, umur : {data_umur}, tinggi : {data_tinggi}, no sepatu : {data_nomor_sepatu}"
print(data)

# string multiline menggunakan \n
print("\n"+5*"="+"DATA STRING MULTILINE"+5*"=")
data = f"nama : {data_nama}, \numur : {data_umur}, \ntinggi : {data_tinggi}, \nno sepatu : {data_nomor_sepatu}"
print(data)

# string multiline menggunakan kutip triplets
print("\n"+5*"="+"DATA STRING MULTILINE"+5*"=")
data = f"""
nama        : {data_nama}
umur        : {data_umur}
tinggi      : {data_tinggi}
no sepatu   : {data_nomor_sepatu}
"""
print(data)

# mengatur lebar
print("\n"+5*"="+"MENGATUR LEBAR"+5*"=")
data = f"""
nama        : {data_nama:>6}
umur        : {data_umur:>6}
tinggi      : {data_tinggi:>6}
no sepatu   : {data_nomor_sepatu:>6}
"""
print(data)