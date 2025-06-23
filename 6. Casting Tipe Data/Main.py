# casting adalah konversi tipe data atau merubah tipe data ke tipe data lain

data_int = 9
print("data : ", data_int, " bertipe : ", type(data_int))

data_float = float(data_int)
print("data : ", data_float, " bertipe : ", type(data_float))

data_string = str(data_int)
print("data : ", data_string, " bertipe : ", type(data_string))

data_bool = bool(data_int)
print("data : ", data_bool, " bertipe : ", type(data_bool)) # akan false jika bernilai 0