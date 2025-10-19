from .Operasi import create_first_Data

# Nama Database
DB_NAME = "Data.txt"

# Template Database
TEMPLATE_DB = {
    "pk" : "XXXXXX",
    "date" : "YYYY-MM-DD",
    "penulis" : 255*" ",
    "judul" : 255*" ",
    "tahun" : "YYYY",
}

def Database():
    try:
        with open(DB_NAME, "r") as file :
            file.read()
    except :
        print("Database Masih Kosong!!!\n")
        create_first_Data()