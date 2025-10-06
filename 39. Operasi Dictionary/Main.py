# operasi untuk dictionary

data_dict = {
    "nama" : "Dandi",
    "npm" : "200210019",
    "jurusan" : "Teknik Informatika"
}

lendict = len(data_dict)
print(lendict)


# mengecek key dictionary
key = "npm"
checkkey = key in data_dict
print(f"apakah data {key} ada di data dictionery : {checkkey}")

# mengakses value (read) dari key denga get
print(data_dict["jurusan"])
print(data_dict.get("jurusan"))
print(data_dict.get("juusan", "tulisan typo a")) # cek key dengan message

# mengupdate data dict
data_dict["nama"] = "ayip"
print(data_dict)

data_dict.update({"npm" : "200210020"})
print(data_dict)

data_dict.update({"semester" : "9"}) # menambahkan otomatis jika data tidak ada
print(data_dict)

# menghapus data
del data_dict["semester"]
print(data_dict)
