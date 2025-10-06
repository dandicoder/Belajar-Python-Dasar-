import datetime

data_waktu = datetime.datetime.now()
print(data_waktu)
tahun = data_waktu.year
hari_ini = data_waktu.strftime("%A")
print(f"hari ini {hari_ini} tahun {tahun}")


from collections import Counter

LIST = ["a", "b", "a", "bd", "b", "f"]
data_count = Counter(LIST)
print(f"data counter : {data_count}")
print(f"jumlah a : {data_count['a']}")

import io

file = io.open("file_text.txt", "r")
print(file.read())