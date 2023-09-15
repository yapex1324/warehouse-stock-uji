daftar_barang = [
    {
        'nama_barang' : 'sepatu',
        'stock' : 100,
        'kategori' : 'apd',
        'harga' : 20000
    },
    {
        'nama_barang' : 'helm',
        'stock' : 20,
        'kategori' : 'apd',
        'harga' : 15000
    },
    {
        'nama_barang' : 'solder',
        'stock' : 20,
        'kategori' : 'elektronik',
        'harga' : 35000
    }
]

def print_kosongan():
    print(f"\n{'nama_barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10}")

def print_barang():
    print(f"\n{'nama barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10}")
    for i in range(len(daftar_barang)):
        nama_barang = daftar_barang[i]['nama_barang']
        stock = daftar_barang[i]['stock']
        kategori = daftar_barang[i]['kategori']
        harga = daftar_barang[i]['harga']
        
        print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")

welcome_home = '''
Selamat Datang di Cek Stok Gudang

List Menu : 
1. Menampilkan daftar barang
2. Menambah barang
3. Mengubah data barang
4. Menghapus stok barang
5. Exit Program 

'''

##############      read done
welcome_read = '''
Silahkan pilih sub menu read data
1. Cek Seluruh daftar barang yang ada
2. Cari barang yang ada
3. Sortir barang berdasarkan kategori
4. kembali ke menu utama
'''
# while True:
#     print(welcome_read)
#     pilihan = int(input("silahkan pilih sub menu read data : "))

#     if pilihan == 1:
#         if len(daftar_barang) == 0:
#             print(f"tidak ada daftar barang")

#         else: 
#             print(f"\n{'nama barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10}")
#             for i in range(len(daftar_barang)):
#                 nama_barang = daftar_barang[i]['nama_barang']
#                 stock = daftar_barang[i]['stock']
#                 kategori = daftar_barang[i]['kategori']
#                 harga = daftar_barang[i]['harga']
                
#                 print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")

#     elif pilihan == 2:
#         if len(daftar_barang) == 0:
#             print(f"tidak ada daftar barang")
#         else:
#             barang_yang_dicari = input("masukkan nama barang yang ingin dicari : ")

#             for i in range(len(daftar_barang)):
#                 nama_barang = daftar_barang[i]['nama_barang']
#                 stock = daftar_barang[i]['stock']
#                 kategori = daftar_barang[i]['kategori']
#                 harga = daftar_barang[i]['harga']
#                 if nama_barang == barang_yang_dicari:
#                     print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")
#                     break
#             else:
#                 print(f"barang tidak ditemukan")
    
#     elif pilihan == 3:
#         barang_yang_disortir = input("masukkan nama kategori yang ingin dicari : ")
#         barang_yang_disortir_list = []
#         for i in range(len(daftar_barang)):
#             nama_barang = daftar_barang[i]['nama_barang']
#             stock = daftar_barang[i]['stock']
#             kategori = daftar_barang[i]['kategori']
#             harga = daftar_barang[i]['harga']
#             if kategori == barang_yang_disortir:
#                 barang_yang_disortir_list.append([nama_barang, stock, kategori, harga])
        
#         if barang_yang_disortir_list:
#             for barang in barang_yang_disortir_list:
#                 print(f"{barang[0]:<13} | {barang[1]:<8} | {barang[2]:<10} | {barang[3]:<10}")
#         else:
#             print(f"kategori barang tidak ditemukan")
    
#     elif pilihan == 4:
#         break

#     else:
#         continue 

#################### create sudah done
welcome_create = '''
++++++++++Tambah data barang++++++++++
1. tambah data barang
2. kembali ke menu utama
'''
# while True:
#     print(welcome_create)
#     pilihan = int(input("silahkan pilih sub menu create data 1 - 2 : "))
#     if pilihan == 1:
#         nama_barang_tambah = input("masukkan barang yang ingin ditambahkan : ")

#         for i in range(len(daftar_barang)):
#                 nama_barang = daftar_barang[i]['nama_barang']
#                 stock = daftar_barang[i]['stock']
#                 kategori = daftar_barang[i]['kategori']
#                 harga = daftar_barang[i]['harga']
#                 if nama_barang == nama_barang_tambah:
#                     print(f"barang yang ditambahkan sudah ada")
#                     break
#         else:
#             stock = int(input("silahkan masukkan jumlah stock barang : "))
#             kategori = input("silahkan masukkan kategori barang : ")
#             harga = int(input("silahkan masukkan harga barang : "))
#             while True:
#                 is_done = input("yakin mau disimpan (y/n)? ")
#                 if is_done == "n":
#                     break
#                 elif is_done == 'y':
#                     daftar_barang.append(
#                         {
#                             'nama_barang' : nama_barang_tambah,
#                             'stock' : stock,
#                             'kategori' : kategori,
#                             'harga' : harga
#                         }
#                     )
#                     print(f"data telah disimpan")
#                     break
#                 else:
#                     continue  
#     elif pilihan == 2:
#          break
#     else:
#          continue 



####################        update data done
welcome_update = '''
++++++++++Ubah data barang++++++++++
1. ubah data barang
2. kembali ke menu utama
'''

# barang_yang_diupdate = input("masukkan nama barang yang ingin diubah : ")
# a = 0
# for i in range(len(daftar_barang)):
#     nama_barang = daftar_barang[i]['nama_barang']
#     stock = daftar_barang[i]['stock']
#     kategori = daftar_barang[i]['kategori']
#     harga = daftar_barang[i]['harga']
#     if nama_barang == barang_yang_diupdate:
#         print_kosongan()
#         print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")
#         while True:
#             if a == 1:
#                 a = 0
#                 break
#             pilihan = input("tekan Y jika ingin lanjut UPDATE atau N jika ingin CANCEL (y/n)? ")
#             if pilihan == 'y':
#                 kolom_yang_ingin_diganti = input("masukkan kolom yang ingin diganti : ")
#                 hasil = input(f"masukkan data {kolom_yang_ingin_diganti} yang baru : ")
#                 while True:
#                     is_done = input("yakin mau disimpan (y/n)? ")
#                     if is_done == "n":
#                         print(f"data tidak jadi disimpan")
#                         a = 1
#                         break
#                     elif is_done == 'y':
#                         daftar_barang[i][kolom_yang_ingin_diganti] = hasil
#                         a = 1
#                         print(f"data telah diupdate")
#                         break
#                     else:
#                         continue
#             elif pilihan == 'n':
#                 break
#             else:
#                 continue
#         break
# else:
#     print(f"barang tidak ditemukan")


welcome_delete = '''
++++++++++Ubah data barang++++++++++
1. hapus data barang
2. kembali ke menu utama
'''

while True:
    print(welcome_delete)
    pilihan_delete = input("silahkan pilih sub menu delete : ")
    if pilihan_delete == '1':
        barang_yang_dihapus = input("masukkan nama barang yang ingin dihapus : ")
        for i in range(len(daftar_barang)):
            nama_barang = daftar_barang[i]['nama_barang']
            stock = daftar_barang[i]['stock']
            kategori = daftar_barang[i]['kategori']
            harga = daftar_barang[i]['harga']
            if nama_barang == barang_yang_dihapus:
                while True:
                    yn_hapus = input("yakin data mau dihapus ? (y/n)")
                    if yn_hapus == 'y':
                        print(f"data sudah dihapus")
                        break
                    elif yn_hapus == 'n':
                        break
                    else:
                        continue
        else:
            print(f"barang tidak ditemukan")
    elif pilihan_delete == '2':
        break
    else:
        continue