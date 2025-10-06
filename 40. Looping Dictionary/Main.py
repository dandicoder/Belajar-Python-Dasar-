data_dict = {
    "nama" : "Dandi",
    "npm" : "200210019",
    "jurusan" : "Teknik Informatika"
}

for key in data_dict.keys():
    print(key)

for values in data_dict.values():
    print(values)


for key, value in data_dict.items():
    print(f"{key} adalah {value}")