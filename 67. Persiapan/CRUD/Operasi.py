from . import Database
from .Utils import random_string, form_input
import time
import os

def delete(no_buku):
    try:
        with open(Database.DB_NAME, "r") as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0 :
                    break
                elif counter == no_buku - 1:
                    pass
                else: 
                    with open("Data_temp.txt", "a", encoding="utf-8") as file_temp:
                        file_temp.write(content)
                counter += 1
    except:
        print("Kesalahan saat ambil Data!")

    os.replace("Data_temp.txt",Database.DB_NAME)
    print("Data Berhasil Dihapus")
        
def update(no_buku,pk,date,penulis,judul,tahun):
    data = Database.TEMPLATE_DB.copy()

    data["pk"] = pk
    data["date"] = date
    data["penulis"] = penulis+Database.TEMPLATE_DB["penulis"][len(penulis):]
    data["judul"] = judul+Database.TEMPLATE_DB["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]}, {data["date"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
    
    data_length = len(data_str)
   
    try:
        with open(Database.DB_NAME, "r+", encoding="utf-8") as file :
            file.seek(data_length*(no_buku-1))
            file.write(data_str)
    except:
        print("Error dalam edit data!!!")

def create(penulis, judul, tahun):
    
    data = Database.TEMPLATE_DB.copy()

    data["pk"] = random_string(6)
    data["date"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis+Database.TEMPLATE_DB["penulis"][len(penulis):]
    data["judul"] = judul+Database.TEMPLATE_DB["judul"][len(judul):]
    data["tahun"] = tahun

    data_str = f'{data["pk"]}, {data["date"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'

    try:
        with open(Database.DB_NAME, "a", encoding="utf-8") as file :
            file.write(data_str)
    except :
        print("Terjadi Kesalahan!")

def create_first_Data():
    penulis, judul, tahun = form_input()

    data = Database.TEMPLATE_DB.copy()
    data["pk"] = random_string(6)
    data["date"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
    data["penulis"] = penulis+Database.TEMPLATE_DB["penulis"][len(penulis):]
    data["judul"] = judul+Database.TEMPLATE_DB["judul"][len(judul):]
    data["tahun"] = tahun
    
    data_str = f'{data["pk"]}, {data["date"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME, "w", encoding="utf-8") as file :
            file.write(data_str)
    except :
        print("Terjadi Kesalahan!")

def read(**kwargs):   
    try:
        with open(Database.DB_NAME, "r") as file :
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs :
                index_buku = kwargs["index"]-1
                if index_buku < 0 or index_buku + 1 > jumlah_buku:
                    return False
                else:
                    return content[index_buku]
            else:  
                return content
    except:
        print("Gagal Membaca Database!")
        create_first_Data() 