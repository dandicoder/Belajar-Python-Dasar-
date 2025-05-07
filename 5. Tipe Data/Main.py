data_integer = 1
print(type(data_integer))

data_float = 1.1
print(type(data_float))

data_string = "ini adalah string"
print(type(data_string))

data_bool = True
print(type(data_bool))


# tipe data khusus
data_complex = complex(5,6)
print(type(data_complex))


print("=====================================")
# tipe data dari bahasa c
from ctypes import c_double, c_int, c_float, c_char, c_bool, c_byte, c_wchar, c_long, c_longlong
data_c_double = c_double(10)
print(type(data_c_double))

data_c_int = c_int(10)
print(type(data_c_int))

data_c_float = c_float(10)
print(type(data_c_float))

data_c_char = c_char(10)
print(type(data_c_char))

data_c_bool = c_bool(10)
print(type(data_c_bool))

data_c_byte = c_byte(10)
print(type(data_c_byte))


data_c_long = c_long(10)
print(type(data_c_long))

data_c_longlong = c_longlong(10)
print(type(data_c_longlong))