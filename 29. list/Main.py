# LIST

# cara membuat list
# 1. dengan menggunakan list()
# 2. dengan menggunakan []

# kumpulan list number
data_number = [1,2,3,4,5]
print(data_number, type(data_number))

# kumpulan list string
data_string = ["satu", "dua", "tiga", "empat", "lima"]
print(data_string, type(data_string))

# kumpulan list boolean
data_bool = [True, False, True, False, True]
print(data_bool, type(data_bool))

# kumpulan list mixed
data_mixed = [1, "dua", True, "empat", 5]
print(data_mixed, type(data_mixed))

# list di dalam list
data_nested = ["satu", ["dua", "tiga"], "empat", ["lima", "enam"]]
print(data_nested, type(data_nested))

## alternatif membuat list string
data = list(("satu", "dua", "tiga", "empat", "lima"))
print(data, type(data))

# menggunakan range
data = list(range(5))
print(data, type(data))

data = list(range(1, 5))
print(data, type(data))

data = list(range(1, 10, 2)) # range(start, stop, step)
print(data, type(data))

# menggunakan for
data = [i for i in range(5) if i != 2]
print(data, type(data))

# genap
data = [i for i in range(1, 10) if i % 2 == 0]
print(data, type(data))
# ganjil
data = [i for i in range(1, 10) if i % 2 == 1]
print(data, type(data))