# date dan time (latihan)

import datetime as dt

hari_ini = dt.date.today()
print(f"Hari ini adalah : {hari_ini:%A} \ntanggal \t: {hari_ini}")

# input tanggal alahir
tanggal = int(input("masukan tanggal lahir anda \t: "))
bulan = int(input("masukan bulan lahir anda \t: "))
tahun = int(input("masukan tahun lahir anda \t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"tanggal lahir anda adalah : {tanggal_lahir} \nhari : {tanggal_lahir:%A}")

hari_lahir = hari_ini - tanggal_lahir
bulan_lahir = (hari_lahir.days % 365) // 30
tahun_lahir = hari_lahir.days // 365
print(f"Kamu lahir pada hari {tanggal_lahir:%A}, umur {tahun_lahir} tahun, {bulan_lahir} bulan")
