import pymysql
import os
from fungsi_filter import *

connection = pymysql.connect(
    host="localhost",
    user="root@",
    password="",
    database="persentase_kelulusan"
)
nim = input("Masukan NIM: ")

def Menampilkan_data(nim):
    cursor = connection.cursor()
    sql = "SELECT * FROM mahasiswa WHERE NIM = %s"
    cursor.execute(sql, nim)
    data = cursor.fetchone()
    return data



def Membuat_folder(nim):
    parent_path = os.path.abspath("hasil_filter")
    new_folder = os.path.join(parent_path, nim)
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
        print("Folder Created")
        Memproses_data(nim)
    else:
        print("Folder Already Exists")


def Memproses_data(nim):
    folder_path = Menampilkan_data(nim)[4]
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if (Mengecek_File_Data_Transkrip(folder_path+files[0])):
        print("File Sudah Ada")
    else:
        nama_file_xlsx = nim+'_s1.xlsx'
        Membuat_File_Sortir_Data(folder_path+"/"+files[0], nama_file_xlsx, nim)

Membuat_folder(nim)