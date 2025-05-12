# Operasi Komperasi

# Setiap hasil dari komperasi komperasi adalah boolean

# >, <, =>, =<, ==, !=, is, is not

# is sebagai komperasi object identity

x = 5
y = 5

print("nilai x = ", x, ", id = ", hex(id(x)))
print("nilai y = ", y, ", id = ", hex(id(y)))

hasil = x is not y

print("hasil x is y = ", hasil)