# operator bitwise, operasi biner, binary
# or (|), and (&), xor (^), not (~)

a = 5
b = 9

# 1. bitwise OR (|)
print("\n",40*"=")
c = a | b
print("nilai :", a, ", binary : ", format(a, "08b"))
print("nilai :", b, ", binary : ", format(b, "08b"))
print(20*"=", " OR")
print("nilai :", c, ", binary : ", format(c, "08b"))

# 2. bitwise AND (&)
print("\n",40*"=")
c = a & b
print("nilai :", a, ", binary : ", format(a, "08b"))
print("nilai :", b, ", binary : ", format(b, "08b"))
print(20*"=", " AND")
print("nilai :", c, ", binary : ", format(c, "08b"))

# 2. bitwise XOR (^)
print("\n",40*"=")
c = a ^ b
print("nilai :", a, ", binary : ", format(a, "08b"))
print("nilai :", b, ", binary : ", format(b, "08b"))
print(20*"=", " XOR")
print("nilai :", c, ", binary : ", format(c, "08b"))

# 2. bitwise NOT (~)
print("\n",40*"=")
c = ~ a
print("nilai :", a, ", binary : ", format(a, "08b"))
print(20*"=", " NOT")
print("nilai :", c, ", binary : ", format(c, "08b"))

# shifting 
# shift right (>>)
print("\n",40*"=")
c = a >> 2
print("nilai :", a, ", binary : ", format(a, "08b"))
print(20*"=", "SHIFT RIGHT 2")
print("nilai :", c, ", binary : ", format(c, "08b"))

# shift left (<<)
print("\n",40*"=")
c = a << 2
print("nilai :", a, ", binary : ", format(a, "08b"))
print(20*"=", "SHIFT LEFT 2")
print("nilai :", c, ", binary : ", format(c, "08b"))