import  os

def header():
    '''header'''
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{'='*40:^40}")

def input_data():
    panjang = int(input("Masukan Panjang : "))
    lebar = int(input("Masukan Lebar : "))
    return panjang, lebar

def menghitung_luas(panjang, lebar):
    return panjang*lebar

def menghitung_keliling(panjang, lebar):
    return 2*(panjang+lebar)

def display(title, value):
    return print(f"Hasil Perhitungan {title} = {value}")

while True:
    
    os.system("clear")
    header()
    PANJANG, LEBAR = input_data()

    opsi = input("hitung (keliling/luas) ? ")

    if opsi == "luas" :
        LUAS = menghitung_luas(PANJANG, LEBAR)
        display("Luas", LUAS)
    else :
        KELILING = menghitung_keliling(PANJANG, LEBAR)
        display("Keliling", KELILING)
  
    isContinue = input("apakah lanjut (y/n) ? ")
    
    if isContinue == "n":
        break