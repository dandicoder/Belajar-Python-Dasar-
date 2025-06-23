# Operasi Logika dan Boolean

# not, or, and, xor


# NOT
a = True
c = not a
print("data a = ", a , ", NOT ===>" , c)

# OR (Akan true jika salah satunya true)
print("\n============= OR =============")
a = False
b = False
c = a or b
print(a, "OR", b, " = ", c)
a = True
b = False
c = a or b
print(a, "OR", b, " = ", c)
a = False
b = True
c = a or b
print(a, "OR", b, " = ", c)
a = True
b = True
c = a or b
print(a, "OR", b, " = ", c)

# AND (akan False jika salah satunya false)
print("\n============= AND =============")
a = False
b = False
c = a and b
print(a, "AND", b, " = ", c)
a = True
b = False
c = a and b
print(a, "AND", b, " = ", c)
a = False
b = True
c = a and b
print(a, "AND", b, " = ", c)
a = True
b = True
c = a and b
print(a, "AND", b, " = ", c)

# XOR (Akan true/false jika salah satunya false, sisanya true/false )
print("\n============= XOR =============")
a = False
b = False
c = a ^ b
print(a, "XOR", b, " = ", c)
a = True
b = False
c = a ^ b
print(a, "XOR", b, " = ", c)
a = False
b = True
c = a ^ b
print(a, "XOR", b, " = ", c)
a = True
b = True
c = a ^ b
print(a, "XOR", b, " = ", c)