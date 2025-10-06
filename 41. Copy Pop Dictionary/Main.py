# copy dictionery

data_dict = {
    "nama" : "Dandi",
    "npm" : "200210019",
    "jurusan" : "Teknik Informatika"
}

mahasiswa = data_dict.copy()

print(f"data dict = {data_dict}")
print(f"data mahasiswa = {mahasiswa}")

mahasiswa.update({"jurusan": "pwk"})
print(f"data dict = {data_dict}")
print(f"data mahasiswa = {mahasiswa}")

data_jurusan = mahasiswa.pop("jurusan") # mengambil data sesuai key
print(f"jurusan = {data_jurusan}")
print(f"data mahasiswa = {mahasiswa}")

data_jurusan = mahasiswa.popitem() 
print(f"jurusan = {data_jurusan}")
print(f"data mahasiswa = {mahasiswa}")