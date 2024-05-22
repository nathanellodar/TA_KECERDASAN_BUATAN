import json

# Load the JSON file
with open('percobaanDataiList.json') as f:
    data = json.load(f)

# Access the data for semester 7
semester_7_data = data['syarat']['jumlah sks']['jenis matkul']['pilihan']['matkul_pilihan']['MatkulPilihan_BebasProdi']

# Print the data
# print(semester_7_data)
for key, value in semester_7_data.items():
    print(f"kode Matkul: {key}\nsks: {value}\n")