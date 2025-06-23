# Operasi yang dapat menyingkatkan
#  operasi ditambah dengan assignment

a = 10


a += 5 # a = a + 5
print("nilai a += 5 : ", a)

a -= 5 # a = a - 5
print("nilai a -= 5 : ", a)

a *= 5 # a = a * 5
print("nilai a *= 5 : ", a)

a /= 5 # a = a / 5
print("nilai a /= 5 : ", a)

a //= 5 # a = a // 5 floor division
print("nilai a //= 5 : ", a)

a **= 5 # a = a ** 5 eksponen/pangkat
print("nilai a **= 5 : ", a)

a %= 5 # a = a % 5 modulus
print("nilai a %= 5 : ", a)

#  operator bitwise
print("\n========== OPERATOR BITWISE ===========")

b = True

print("\n================> OR")
b |= True # OR
print("nilai b |= c : ", b)
b |= False # OR
print("nilai b |= c : ", b)
b |= False # OR
print("nilai b |= c : ", b)
b |= False # OR
print("nilai b |= c : ", b)

print("\n================> AND")
b &= True # AND
print("nilai b &= c : ", b)
b &= False # AND
print("nilai b &= c : ", b)
b &= False # AND
print("nilai b &= c : ", b)
b &= False # AND
print("nilai b &= c : ", b)

print("\n================> XOR")
b ^= True # XOR
print("nilai b ^= c : ", b)
b ^= True # XOR true ^ true = false
print("nilai b ^= c : ", b)
b ^= False # XOR
print("nilai b ^= c : ", b)
b ^= False # XOR
print("nilai b ^= c : ", b)

print("\n================> NOT")
b = True
b = not b
print("nilai b = not b : ", b)

b = False
b = not b
print("nilai b = not b : ", b)

print("\n================> SHIFT")
d = 0b0100

d >>= 2 # shift right
print("nilai d >>= 2 : ", format(d, "04b"))
 
d <<= 2 # shift left
print("nilai d <<= 2 : ", format(d, "04b"))
