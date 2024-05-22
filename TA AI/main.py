
from fungsi_filter import *
import streamlit as st

st.markdown(
    f"""
    <style>
    header {{
        text-align: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)
# st.write("Hello, World!")
st.header("Filter :rainbow[Nilai] Mahasiswa", divider="rainbow")

# Read the PDF file and convert it into a DataFrame
# tables = tabula.read_pdf("contoh kasus/khs71220892.pdf", pages="all")


# # di rapikan dalam excel
# excelData = pd.DataFrame(tables[0].head(10)['Unnamed: 0']) #menyimpan kolom kode matkulx``

# nim = input("Masukan NIM: ")
# # print(nim+'_Semester1.xlsx')
# nama_file = nim+'_Semester1.xlsx'

# if (Mengecek_File_Data_Transkrip(nama_file)):
#     print("File Sudah Ada")
# else:
#     Membuat_File_Sortir_Data('contoh kasus/khs71220892.pdf', nama_file)