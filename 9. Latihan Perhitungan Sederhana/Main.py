'''
=============================================================================================
|    DARI KE   |  CELCIUS   |  REAMUR      |  FAHRENHEIT          |       KELVIN          |
=============================================================================================
|    CELCIUS     |     -      |   5/4 * C    |  (9/5 * C) + 32      |  C + 273              |
|    REAMUR      |  4/5 * R   |     -        |  (9/4 * R) + 32      | (5/4 * R) + 273       |
| FAHRENHEIT     |  5/9(F-32) |  4/9(F-32)   |          -           | (5/9 * (F-32)) + 273  |
|    KELVIN      |  K - 273   |  4/5(K-273)  | (9/5 * (K-273)) + 32 |           -           |
=============================================================================================
'''


print("\nPROGRAM KONVERSI TEMPERATUR")

# celcius
celcius = float(input("Masukan suhu dalam bentuk celcius : "))
print("Suhu adalah : ", celcius, " Celcius")

# reamur
reamur = (4 / 5) * celcius
print("Suhu adalah : ", reamur, " reamur")

# fahrenheit
fahrenheit = ((9 / 5) * celcius) + 32
print("Suhu adalah : ", fahrenheit, " fahrenheit")

# kelvin
kelvin = celcius + 273
print("Suhu adalah : ", kelvin, " kelvin")


print("\n=================FAHRENHEIT=================")
fahrenheit = float(input("Masukan suhu dalam bentuk fahrenheit : "))
print("Suhu adalah : ", fahrenheit, " fahrenheit")

# celcius
celcius = (5 / 9) * (fahrenheit - 32)
print("Suhu adalah : ", celcius, " celcius")

# reamur
reamur = (4 / 9) * (fahrenheit - 32)
print("Suhu adalah : ", reamur, " reamur")

# kelvin
kelvin = ((5 / 9) * (fahrenheit - 32)) + 273
print("Suhu adalah : ", kelvin, " kelvin")


print("\n===================KELVIN===================")
kelvin = float(input("Masukan suhu dalam bentuk kelvin : "))
print("Suhu adalah : ", kelvin, " kelvin")

# celcius
celcius = kelvin - 273
print("Suhu adalah : ", celcius, " celcius")

# reamur
reamur = (4 / 5) * (kelvin - 273)
print("Suhu adalah : ", reamur, " reamur")

# fahrenheit
fahrenheit = ((9 / 5) * (kelvin - 273)) + 32
print("Suhu adalah : ", fahrenheit, " fahrenheit")

print("\nTERIMAKASIH")