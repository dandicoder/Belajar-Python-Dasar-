d = "Selamat Siang, Apa kabar kamu?"
print(d, type(d))

# 1. cara membuat string

'''

1. dengan menggunakan single quote ' '
2. dengan menggunakan double quote " "

'''

print("\n=======================")

d = "Hello, bubub?"
print(d, type(d))

d = "Selamat Hari Jum'at, Apa kabar kamu?"
print(d, type(d))

# menggunakan tanda /

d = 'jum\'at'
print(d, type(d))

# backlash 
print("C:\\User\\Dandi\\Desktop\\Python")

# backspace
print("Dandi \bDandi")

# tab
print("Dandi \tDandi")

# newline
print("Baris pertama \nbaris kedua") # LF => line feed
print("Baris pertama \rbaris kedua")    # CR => carriage return 
print("Baris pertama \r\nbaris kedua") # CRLF => line feed dan carriage return

#  STRING LITERAL DAN RAW

# hati-hati
print("C:\new") # akan error

# menggunakan raw string
print(r"C:\new")

# multiline string
print("""
    ini adalah baris pertama
    ini adalah baris kedua
    ini adalah baris ketiga
""")

# multiline string dan raw
print(r"""
    ini adalah baris pertama
    ini adalah baris kedua
    ini adalah baris ketiga
""")
