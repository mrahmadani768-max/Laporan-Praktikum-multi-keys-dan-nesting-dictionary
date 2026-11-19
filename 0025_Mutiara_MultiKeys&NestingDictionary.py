# # PROGRAM 11.1 MULTI KEYS & NESTING DICTIONARY 
# import datetime

# mahasiswa1 = {
#     'nama':'Mutiara Rahma Dani',
#     'nim':'2605060025',
#     'sks_lulus':130,
#     'beasiswa': False,
#     'lahir':datetime.datetime(2007, 6, 30) # tahun, tanggal, bulan
# }

# mahasiswa2 = {
#     'nama':'Lailatul Fajriyah',
#     'nim':'2605060026',
#     'sks_lulus': 130,
#     'beasiswa': True,
#     'lahir':datetime.datetime(2007, 1, 4) 
# }

# mahasiswa3 = {
#     'nama':'Indy Zahwanada Utomo',
#     'nim':'2605060027',
#     'sks_lulus':135,
#     'beasiswa': False,
#     'lahir':datetime.datetime(2008, 4, 1)
# }

# data_mahasiswa = {
#     'MAH001':mahasiswa1,
#     'MAH002':mahasiswa2,
#     'MAH003':mahasiswa3,
# }

# print("{'KEY :<6} {'Nama' :<6} {'SKS :<3'} {'Beasiswa' :<9} {'Lahir' :<10}")
# print("-"*50)

# for mahasiswa in data_mahasiswa:
#     KEY = mahasiswa

#     NAMA = data_mahasiswa[KEY]['nama']
#     NIM = data_mahasiswa[KEY]['nim']
#     SKS = data_mahasiswa[KEY]['sks_lulus']
#     BEASISWA = data_mahasiswa[KEY]['beasiswa']
#     LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

#     print(f"{KEY:<6} {NAMA:<17} {SKS:<3} {BEASISWA:<9} {LAHIR:<10}")

# # PROGRAM 11.2 LATIHAN DICTIONARY BAGIAN 1
# import datetime

# mahasiswa_template = {
#     'nama':'nama',
#     'nim':00000000,
#     'sks_lulus':0,
#     'lahir':datetime.datetime(1111,11,1)
# }

# data_mahasiswa = {}

# print(f"{'SELAMAT DATANG':^20}")
# print(f"{'DATA MAHASISWA':^20}")
# print("-"*20)

# mahasiswa = dict.fromkeys(mahasiswa_template.keys())
# print(mahasiswa)
# mahasiswa['nama'] = input("Nama Mahasiswa: ")
# mahasiswa['nim'] = input("NIM Mahasiswa: ")
# mahasiswa['sks_lulus'] = int(input("SKS Lulus: "))
# TAHUN_LAHIR = int(input("Tahun Lahir (yyyy): "))
# BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
# TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
# mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

# print(mahasiswa)

# # PROGRAM 11.3 LATIHAN DICTIONARY BAGIAN 3
# import datetime
# import os
# import string
# import random

# # template dict mahasiswa 
# mahasiswa_template = {
#     'nama':'nama',
#     'nim':'00000000',
#     'sks_lulus': 0,
#     'lahir':datetime.datetime(1111,1,11)
# }

# data_mahasiswa = {}

# while True :
#     # os.system("cls") # untuk windows
#     os.system("clear")
#     print(f"{'SELAMAT DATANG':^20}")
#     print(f"{'DATA MAHASISWA':^20}")
#     print('_'^20)

#     mahasiswa = dict.fromkeys(mahasiswa_template.keys())
#     mahasiswa['nama'] = input("Nama Mahasiswa: ")
#     mahasiswa['nim'] = input("NIM Mahasiswa: ")
#     mahasiswa['sks_lulus'] = int(input("sks_lulus: "))
#     TAHUM_LAHIR = int(input("Tahun lahir (yyyy): "))
#     BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
#     TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
#     mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

#     KEY = ''.join((random.choice(string.ascil_uppercase) for i in range(6)))
#     data_mahasiswa.update({KEY.mahasiswa})

#     # dari program sebelumnya, hilangkan beasiswa 
#     print(f"\n{'KEY':<6} {'Nama':<17} {'NIM':<8} {'SKS lulus':<10} {'Tanggal lahir':<10}")
#     print('_'*60)

#     for mahasiswa in data_mahasiswa:
#         KEY = mahasiswa

#         NAMA = data_mahasiswa[KEY]['nama']
#         NIM = data_mahasiswa[KEY]['nim']
#         SKS = data_mahasiswa[KEY]['sks_lulus']
#         LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

#         print(f"{KEY:<6} {NAMA:<17} {NIM:<8} {SKS:^10} {LAHIR:^10}")

#     print("\n")
#     is_done = input("Mau tambah lagi kak (y/n)?")
#     if is_done == "n":
#         break

# print("\nAkhir dari program, terima kasih")

# --- TUGAS PRAKTIKUM ---

import datetime
import string
import random

# Template dictionary buku 
buku_template = {
    'judul_buku':'judul',
    'penulis':'penulis',
    'tahun_terbit':0,
    'tanggal_terakhir_pinjam': datetime.datetime(1111, 1, 1),
    'status':'TERSEDIA'
}

data_buku = {}

while True:
    print(f"{'SELAMAT DATANG':^30}")
    print(f"{'SISTEM PERPUSTAKAAN':^30}")
    print("-"*30)

    # Membuat divtionary baru berdasarkan template
    buku = dict.fromkeys(buku_template.keys())

    buku['judul_buku'] = input("Judul buku")
    buku['penulis'] = input("Penulis: ")
    buku['tahun_terbit'] = int(input("Tahun Terbit: "))

    TANGGAL = input("Tanggal Terakhir Pinjam (DD-MM-YYYY): ")
    buku['tanggal_terakhir_pinjam'] = datetime.datetime.strptime(TANGGAL, "%d-%m-%Y")

    # Memasukkan status buku 
    while True:
        STATUS = input("Status (TERSEDIA/TIDAK): '").upper()
        if STATUS == "TERSEDIA" or STATUS == "TIDAK":
            buku['status'] = STATUS
            break
        else:
            print("Status harus TERSEDIA atau TIDAK!")

        # Membuat key secara acak 
    KEY = ''.join(
        random.choice(string.ascii_uppercase) for i in range(6)
        )

     # Multi-key menggunakan tuple 
    MULTI_KEY = (KEY, buku['tahun_terbit'])

        # Memasukkan data ke dalam nesting dictionary
    data_buku.update({MULTI_KEY: buku})

    # Menampilkan seluruh data buku 
    print("\n")
    print(f"{'DATA BUKU PERPUSTAKAAN':^75}")
    print("-"*75)
    print(f"{'KEY':<10} {'Judul Buku':<20} {'Penulis':<15}" f"{'Tahun':<8} {'Tanggal Pinjam':<12} {'Status':<0}")
    print("-"*75)

    for MULTI_KEY in data_buku:
        KEY = MULTI_KEY[0]

        JUDUL = data_buku[MULTI_KEY]['judul_buku']
        PENULIS = data_buku[MULTI_KEY]['penulis']
        TAHUN = data_buku[MULTI_KEY]['tahun_terbit']
        TANGGAL = data_buku[MULTI_KEY]['tanggal_terakhir_pinjam'].strftime("%d-%m-%Y")
        STATUS = data_buku[MULTI_KEY]['status']

        print(f"{KEY:<10} {JUDUL:<10} {PENULIS:<15}" f"{TAHUN:<8} {TANGGAL:<12} {STATUS:<10}")

    print("\n")
    is_done = input("Mau menambah buku lagi (y/n)").lower()
    if is_done == "n":
        break

print("\nAkhir dari program, terima kasih")