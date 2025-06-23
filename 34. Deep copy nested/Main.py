data_1 = [1,2,3]
data_2 = [4,5]

data_2D = [data_1, data_2]
print(f"data 2D\t = {data_2D}")

data_copy = data_2D.copy()
print(f"data 2D\t\t = {data_2D}")
print(f"data 2D Copy\t = {data_copy}")

# adreess
print(f"data 2D\t\t = {hex(id(data_2D))}")
print(f"data 2D Copy\t = {hex(id(data_copy))}")

# melihat address didalam nested list
print(f"address data 2D ke {data_2D[0][0]}\t\t = {hex(id(data_2D[0][0]))}")
print(f"address data 2D Copy ke {data_copy[0][0]}\t = {hex(id(data_copy[0][0]))}")

# untuk mengcopy nested list menggunakan deepcopy

from copy import deepcopy

data_deepcopy = deepcopy(data_2D)
print(f"data 2D\t\t\t = {data_2D}")
print(f"data 2D deepcopy\t = {data_deepcopy}")

data_deepcopy[1][1] = 9
print(f"data 2D\t\t\t = {data_2D}")
print(f"data 2D deepcopy\t = {data_deepcopy}")

# melihat address didalam nested list
print(f"address data 2D ke {data_2D[0]}\t\t = {hex(id(data_2D[0]))}")
print(f"address data 2D deepcopy ke {data_deepcopy[0]}\t = {hex(id(data_deepcopy[0]))}")
