## Teknik menduplikasi list

a = ["naruto", "sasuke", "sakura"]
print(f"a = {a}")

b = a # pass by reference
print(f"b = {b}")

# kita akan merubah member dari a

# merubah keduanya
a[1] = "sai"
b.sort()
print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list
print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")

# menduplikasi list dengan copy
c = a.copy() # membuat duplikasi dengan address berbeda
print(f"c = {c}")

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")