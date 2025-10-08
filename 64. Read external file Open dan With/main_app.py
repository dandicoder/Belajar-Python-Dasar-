# membaca file

print("="*3, "MEMBACA FILE", "="*3)

file = open("data.txt", mode="r")

print(f"status read : {file.readable()}") 
print(f"status write : {file.writable()}") 

# print(file.read()) 

# print(file.readline(), end="") # membaca satu satu dari atas
# print(file.readline())

print(file.readlines())

print(f"apakah file sudah keluar : {file.closed}")
file.close()
print(f"apakah file sudah keluar : {file.closed}")


print("="*3, "MEMBACA FILE MENGGUNAKAN PYTHON", "="*3)
with open("data.txt", mode="r") as file:
    content = file.readline()
    print(content)
    print(f"apakah file sudah keluar : {file.closed}")

print(f"apakah file sudah keluar : {file.closed}")