# copy dictionery

mahasiswa1 = {
    "nama" : "Dandi",
    "npm" : "200210019",
    "jurusan" : "Teknik Informatika"
}

mahasiswa2 = {
    "nama" : "Ayip",
    "npm" : "200210020",
    "jurusan" : "Teknik Informatika"
}

mahasiswa3 = {
    "nama" : "Cyko",
    "npm" : "200210021",
    "jurusan" : "Teknik Informatika"
}

mahasiswa4 = {
    "nama" : "Ryanda",
    "npm" : "200210022",
    "jurusan" : "Teknik Informatika"
}


dataMhs = {
    "mhs1" : mahasiswa1,
    "mhs2" : mahasiswa2,
    "mhs3" : mahasiswa3,
    "mhs4" : mahasiswa4,
}

print(f"{"No":<2} | {"Nama":<10} | {"Npm":<9} | {"jurusan":<20} |")
print(52*"-")     
no = 0
for mhs in dataMhs :
    key = mhs
    no += 1
    nama = dataMhs[mhs]["nama"]
    npm = dataMhs[mhs]["npm"]
    jurusan = dataMhs[mhs]["jurusan"]

    print(f"{no:<2} | {nama:<10} | {npm:<9} | {jurusan:<20} |")