import datetime

daftar_barang = [
    {
        'nama_barang' : 'sepatu',
        'stock' : 100,
        'kategori' : 'apd',
        'harga' : 20000,
    },
    {
        'nama_barang' : 'helm',
        'stock' : 20,
        'kategori' : 'apd',
        'harga' : 15000,
    },
    {
        'nama_barang' : 'solder',
        'stock' : 20,
        'kategori' : 'elektronik',
        'harga' : 35000,
    }
]

def print_kosongan():
    print(f"\n{'nama_barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10}")

def print_barang(daftar_barang):
    print(f"\n{'nama barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10}")
    for i in range(len(daftar_barang)):
        nama_barang = daftar_barang[i]['nama_barang']
        stock = daftar_barang[i]['stock']
        kategori = daftar_barang[i]['kategori']
        harga = daftar_barang[i]['harga']
        
        print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")

def print_log():
    print(f"\n{'nama barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10} | {'status':<30} | {'tanggal':<10} | {'waktu':<10}")
    for i in range(len(list_log_kosong)):
        nama_barang = list_log_kosong[i]['nama_barang']
        stock = list_log_kosong[i]['stock']
        kategori = list_log_kosong[i]['kategori']
        harga = list_log_kosong[i]['harga']
        status = list_log_kosong[i]['status']
        tanggal = list_log_kosong[i]['tanggal']
        waktu = list_log_kosong[i]['waktu']
        
        print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10} | {status:<30} | {tanggal:<10} | {waktu:<10}")

def log_pengeluaran_barang():
    list_belanja = []
    while True:
        print(welcome_belanja)
        sub_menu_belanja = input("masukkan pilihan sub menu Pengeluaran Barang : ")
        if sub_menu_belanja == '1':
            barang_yang_dibeli = input("masukkan barang yang ingin dikeluarkan : ")
            for i in range(len(daftar_barang)):
                nama_barang = daftar_barang[i]['nama_barang']
                stock = daftar_barang[i]['stock']
                kategori = daftar_barang[i]['kategori']
                harga = daftar_barang[i]['harga']

                if nama_barang == barang_yang_dibeli:
                    masukkan_stock = int(input("masukkan jumlah yang ingin dikeluarkan : "))
                    if masukkan_stock <= 0:
                        print(f"masukkan jumlah yang valid")
                        break
                    elif int(masukkan_stock) < int(stock):
                        daftar_barang[i]['stock'] = int(daftar_barang[i]['stock']) - masukkan_stock
                        current_datetime = datetime.datetime.now()
                        formatted_date = current_datetime.strftime("%Y-%m-%d")
                        formatted_time = current_datetime.strftime("%H:%M:%S")
                        list_log_kosong.append(
                            {
                                'nama_barang' : barang_yang_dibeli,
                                'stock' : stock,
                                'kategori' : kategori,
                                'harga' : harga,
                                'status' : f"barang dikeluarkan {masukkan_stock} pc",
                                'tanggal' : formatted_date,
                                'waktu' : formatted_time
                            }
                        )
                        print(f"barang sudah dikeluarkan")
                        break
                    else:
                        print(f"jumlah yang dimasukkan tidak boleh melebihi stock")
                        break

            else:
                print(f"barang tidak ditemukan")
        elif sub_menu_belanja == '2':
            break
        else:
            continue

welcome_home = '''
Selamat Datang di Cek Stok Gudang

List Menu : 
1. Menampilkan daftar barang
2. Menambah barang
3. Mengubah data barang
4. Menghapus stok barang
5. Log data
6. Exit Program'''

##############      read done
welcome_read = '''
Silahkan pilih sub menu read data
1. Cek Seluruh daftar barang yang ada
2. Cari barang yang ada
3. Sortir barang berdasarkan kategori
4. kembali ke menu utama'''

welcome_create = '''
++++++++++Tambah data barang++++++++++
1. tambah data barang
2. kembali ke menu utama'''

welcome_update = '''
++++++++++Ubah data barang++++++++++
1. ubah data barang
2. kembali ke menu utama'''

welcome_delete = '''
++++++++++Ubah data barang++++++++++
1. hapus data barang
2. keluarkan barang
3. kembali ke menu utama'''

welcome_belanja = '''
==========Menu Pengeluaran Barang==========
1. Keluarkan barang
2. Kembali menu sebelumnya'''

list_log_kosong = []
while True:
    print(welcome_home)
    pilihan_menu = input("masukkan menu yang ingin di cek : ")

    if pilihan_menu == '1':

        while True:
            print(welcome_read)
            pilihan = int(input("silahkan pilih sub menu read data : "))

            if pilihan == 1:
                if len(daftar_barang) == 0:
                    print(f"tidak ada daftar barang")

                else: 
                    print_kosongan()
                    print_barang(daftar_barang)

            elif pilihan == 2:
                if len(daftar_barang) == 0:
                    print(f"tidak ada daftar barang")
                else:
                    barang_yang_dicari = input("masukkan nama barang yang ingin dicari : ")

                    for i in range(len(daftar_barang)):
                        nama_barang = daftar_barang[i]['nama_barang']
                        stock = daftar_barang[i]['stock']
                        kategori = daftar_barang[i]['kategori']
                        harga = daftar_barang[i]['harga']
                        if nama_barang == barang_yang_dicari:
                            print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")
                            break
                    else:
                        print(f"barang tidak ditemukan")
            
            elif pilihan == 3:
                barang_yang_disortir = input("masukkan nama kategori yang ingin dicari : ")
                barang_yang_disortir_list = []
                for i in range(len(daftar_barang)):
                    nama_barang = daftar_barang[i]['nama_barang']
                    stock = daftar_barang[i]['stock']
                    kategori = daftar_barang[i]['kategori']
                    harga = daftar_barang[i]['harga']
                    if kategori == barang_yang_disortir:
                        barang_yang_disortir_list.append([nama_barang, stock, kategori, harga])
                
                if barang_yang_disortir_list:
                    print_kosongan()
                    for barang in barang_yang_disortir_list:
                        print(f"{barang[0]:<13} | {barang[1]:<8} | {barang[2]:<10} | {barang[3]:<10}")
                else:
                    print(f"kategori barang tidak ditemukan")
            
            elif pilihan == 4:
                break

            else:
                continue 

    #################### create sudah done
    elif pilihan_menu == '2':
        while True:
            print(welcome_create)
            pilihan = input("silahkan pilih sub menu create data 1 - 2 : ")
            if pilihan == '1':
                nama_barang_tambah = input("masukkan barang yang ingin ditambahkan : ")

                for i in range(len(daftar_barang)):
                        nama_barang = daftar_barang[i]['nama_barang']
                        stock = daftar_barang[i]['stock']
                        kategori = daftar_barang[i]['kategori']
                        harga = daftar_barang[i]['harga']
                        if nama_barang == nama_barang_tambah:
                            print(f"barang yang ditambahkan sudah ada")
                            break
                else:
                    stock = input("silahkan masukkan jumlah stock barang : ")
                    if stock.isnumeric():
                        stock = int(stock)
                    else:
                        print(f"")
                        print(f"masukkan input berupa angka")
                        print(f"kembali ke menu utama")
                        break

                    kategori = input("silahkan masukkan kategori barang : ")

                    harga = input("silahkan masukkan harga barang : ")
                    if harga.isnumeric():
                        harga = int(harga)
                    else:
                        print(f"")
                        print(f"masukkan input berupa angka")
                        print(f"kembali ke menu utama")
                        break
                    
                    while True:
                        is_done = input("yakin mau disimpan (y/n)? ")
                        is_done = is_done.lower()
                        if is_done == "n":
                            print(f"data tidak jadi disimpan")
                            break
                        elif is_done == 'y':
                            daftar_barang.append(
                                {
                                    'nama_barang' : nama_barang_tambah,
                                    'stock' : stock,
                                    'kategori' : kategori,
                                    'harga' : harga
                                }
                            )
                            print(f"data telah disimpan")
                            current_datetime = datetime.datetime.now()
                            formatted_date = current_datetime.strftime("%Y-%m-%d")
                            formatted_time = current_datetime.strftime("%H:%M:%S")
                            list_log_kosong.append(
                                {
                                    'nama_barang' : nama_barang_tambah,
                                    'stock' : stock,
                                    'kategori' : kategori,
                                    'harga' : harga,
                                    'status' : 'barang ditambahkan',
                                    'tanggal' : formatted_date,
                                    'waktu' : formatted_time
                                }
                            )
                            break
                        else:
                            continue  
            elif pilihan == '2':
                break
            else:
                continue 



    ####################        update data done

    elif pilihan_menu == '3':
        while True:
            print(welcome_update)
            pilihan_update = input("masukkan pilihan sub menu update : ")
            if pilihan_update == '1':
                barang_yang_diupdate = input("masukkan nama barang yang ingin diubah : ")
                a = 0
                for i in range(len(daftar_barang)):
                    nama_barang = daftar_barang[i]['nama_barang']
                    stock = daftar_barang[i]['stock']
                    kategori = daftar_barang[i]['kategori']
                    harga = daftar_barang[i]['harga']
                    if nama_barang == barang_yang_diupdate:
                        print_kosongan()
                        print(f"{nama_barang:<13} | {stock:<8} | {kategori:<10} | {harga:<10}")
                        while True:
                            if a == 1:
                                a = 0
                                break
                            pilihan = input("tekan Y jika ingin lanjut UPDATE atau N jika ingin CANCEL (y/n)? ")
                            pilihan = pilihan.lower()
                            if pilihan == 'y':
                                kolom_yang_ingin_diganti = input("masukkan kolom yang ingin diganti : ")
                                hasil = input(f"masukkan data {kolom_yang_ingin_diganti} yang baru : ")
                                while True:
                                    is_done = input("yakin mau disimpan (y/n)? ")
                                    is_done = is_done.lower()
                                    if is_done == "n":
                                        print(f"data tidak jadi disimpan")
                                        a = 1
                                        break
                                    elif is_done == 'y':
                                        daftar_barang[i][kolom_yang_ingin_diganti] = hasil
                                        a = 1
                                        current_datetime = datetime.datetime.now()
                                        formatted_date = current_datetime.strftime("%Y-%m-%d")
                                        formatted_time = current_datetime.strftime("%H:%M:%S")
                                        list_log_kosong.append(
                                        {
                                            'nama_barang' : barang_yang_diupdate,
                                            'stock' : stock,
                                            'kategori' : kategori,
                                            'harga' : harga,
                                            'status' : f"kolom yang diupdate {kolom_yang_ingin_diganti}",
                                            'tanggal' : formatted_date,
                                            'waktu' : formatted_time
                                        }
                                        )
                                        print(f"data telah diupdate")
                                        break
                                    else:
                                        continue
                            elif pilihan == 'n':
                                break
                            else:
                                continue
                        break
                else:
                    print(f"barang tidak ditemukan")
            elif pilihan_update == '2':
                break
            else:
                continue



    elif pilihan_menu == '4':
        while True:
            print(welcome_delete)
            pilihan_delete = input("silahkan pilih sub menu delete : ")
            if pilihan_delete == '1':
                barang_yang_dihapus = input("masukkan nama barang yang ingin dihapus : ")
                for i in range(len(daftar_barang)):
                    a = 0
                    nama_barang = daftar_barang[i]['nama_barang']
                    stock = daftar_barang[i]['stock']
                    kategori = daftar_barang[i]['kategori']
                    harga = daftar_barang[i]['harga']
                    if nama_barang == barang_yang_dihapus:
                        while True:
                            yn_hapus = input("yakin data mau dihapus ? (y/n)")
                            if yn_hapus == 'y':
                                a = i
                                current_datetime = datetime.datetime.now()
                                formatted_date = current_datetime.strftime("%Y-%m-%d")
                                formatted_time = current_datetime.strftime("%H:%M:%S")
                                list_log_kosong.append(
                                    {
                                        'nama_barang' : barang_yang_dihapus,
                                        'stock' : stock,
                                        'kategori' : kategori,
                                        'harga' : harga,
                                        'status' : 'barang dihapus',
                                        'tanggal' : formatted_date,
                                        'waktu' : formatted_time
                                    }
                                )
                                del daftar_barang[i]
                                print(f"data sudah dihapus")
                                break
                            elif yn_hapus == 'n':
                                break
                            else:
                                continue
                        break
                else:
                    print(f"barang tidak ditemukan")
            elif pilihan_delete == '2':
                log_pengeluaran_barang()
            elif pilihan_delete == '3':
                break
            else:
                continue
    
    elif pilihan_menu == '6':
        break

    elif pilihan_menu == '5':
        if list_log_kosong == []:
            print(f"\nlog masih belum ada data")

        else:
            print_log()
    else:
        continue








