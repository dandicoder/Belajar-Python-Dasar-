# kalkulator sederhana
print("\n========== KALKULATOR SEDERHANA ===========")

angka_1 = float(input("Masukan angka pertama : "))
operator = input("Masukan operator (+, -, *, /) : ")
angka_2 = float(input("Masukan angka kedua : "))

if operator == "+":
    hasil = angka_1 + angka_2
    print(angka_1, "+", angka_2, "=", hasil)
elif operator == "-":
    hasil = angka_1 - angka_2
    print(angka_1, "-", angka_2, "=", hasil)
elif operator == "*" or operator == "x" or operator == "X":
    hasil = angka_1 * angka_2
    print(angka_1, "*", angka_2, "=", hasil)
elif operator == "/":
    hasil = angka_1 / angka_2
    print(angka_1, "/", angka_2, "=", hasil)
else:
    print("Operator tidak valid")