def print_barang(daftar_barang):
    print(f"\n{'nama barang':<13} | {'stock':<8} | {'kategori':<10} | {'harga':<10}")
    for barang in daftar_barang:
        print(f"{barang['nama_barang']:<13} | {barang['stock']:<8} | {barang['kategori']:<10} | {barang['harga']:<10}")

def create_barang(daftar_barang):
    nama_barang_tambah = input("Masukkan nama barang yang ingin ditambahkan: ")
    for barang in daftar_barang:
        if barang['nama_barang'] == nama_barang_tambah:
            print("Barang yang ditambahkan sudah ada.")
            return
    stock = int(input("Silahkan masukkan jumlah stock barang: "))
    kategori = input("Silahkan masukkan kategori barang: ")
    harga = int(input("Silahkan masukkan harga barang: "))
    while True:
        is_done = input("Yakin mau disimpan (y/n)? ")
        if is_done == "n":
            return
        elif is_done == 'y':
            daftar_barang.append({'nama_barang': nama_barang_tambah, 'stock': stock, 'kategori': kategori, 'harga': harga})
            print("Data telah disimpan.")
            return

def update_barang(daftar_barang):
    barang_yang_diupdate = input("Masukkan nama barang yang ingin diubah: ")
    for barang in daftar_barang:
        if barang['nama_barang'] == barang_yang_diupdate:
            print_barang([barang])
            while True:
                pilihan = input("Tekan Y jika ingin lanjut UPDATE atau N jika ingin CANCEL (y/n): ")
                if pilihan == 'y':
                    kolom_yang_ingin_diganti = input("Masukkan kolom yang ingin diganti: ")
                    hasil = input(f"Masukkan data {kolom_yang_ingin_diganti} yang baru: ")
                    while True:
                        is_done = input("Yakin mau disimpan (y/n)? ")
                        if is_done == "n":
                            print("Data tidak jadi disimpan.")
                            return
                        elif is_done == 'y':
                            barang[kolom_yang_ingin_diganti] = hasil
                            print("Data telah diupdate.")
                            return
                elif pilihan == 'n':
                    return

def delete_barang(daftar_barang):
    barang_yang_dihapus = input("Masukkan nama barang yang ingin dihapus: ")
    for i, barang in enumerate(daftar_barang):
        if barang['nama_barang'] == barang_yang_dihapus:
            while True:
                yn_hapus = input("Yakin data mau dihapus? (y/n)")
                if yn_hapus == 'y':
                    del daftar_barang[i]
                    print("Data sudah dihapus.")
                    return
                elif yn_hapus == 'n':
                    return

def main():
    daftar_barang = [
        {'nama_barang': 'sepatu', 'stock': 100, 'kategori': 'apd', 'harga': 20000},
        {'nama_barang': 'helm', 'stock': 20, 'kategori': 'apd', 'harga': 15000},
        {'nama_barang': 'solder', 'stock': 20, 'kategori': 'elektronik', 'harga': 35000}
    ]

    while True:
        print("Selamat Datang di Cek Stok Gudang")
        print("List Menu:")
        print("1. Menampilkan daftar barang")
        print("2. Menambah barang")
        print("3. Mengubah data barang")
        print("4. Menghapus stok barang")
        print("5. Exit Program")

        pilihan_menu = input("Masukkan menu yang ingin di cek: ")

        if pilihan_menu == '1':
            while True:
                print("Silahkan pilih sub menu read data")
                print("1. Cek Seluruh daftar barang yang ada")
                print("2. Cari barang yang ada")
                print("3. Sortir barang berdasarkan kategori")
                print("4. Kembali ke menu utama")

                pilihan = input("Silahkan pilih sub menu read data: ")

                if pilihan == '1':
                    if len(daftar_barang) == 0:
                        print("Tidak ada daftar barang")
                    else:
                        print_barang(daftar_barang)

                elif pilihan == '2':
                    if len(daftar_barang) == 0:
                        print("Tidak ada daftar barang")
                    else:
                        barang_yang_dicari = input("Masukkan nama barang yang ingin dicari: ")
                        for barang in daftar_barang:
                            if barang['nama_barang'] == barang_yang_dicari:
                                print_barang([barang])
                                break
                        else:
                            print("Barang tidak ditemukan")

                elif pilihan == '3':
                    barang_yang_disortir = input("Masukkan nama kategori yang ingin dicari: ")
                    barang_yang_disortir_list = [barang for barang in daftar_barang if barang['kategori'] == barang_yang_disortir]
                    if barang_yang_disortir_list:
                        print_barang(barang_yang_disortir_list)
                    else:
                        print("Kategori barang tidak ditemukan")

                elif pilihan == '4':
                    break

        elif pilihan_menu == '2':
            while True:
                print("++++++++++Tambah data barang++++++++++")
                print("1. Tambah data barang")
                print("2. Kembali ke menu utama")

                pilihan = input("Silahkan pilih sub menu create data 1 - 2: ")
                if pilihan == '1':
                    create_barang(daftar_barang)
                elif pilihan == '2':
                    break

        elif pilihan_menu == '3':
            while True:
                print("++++++++++Ubah data barang++++++++++")
                print("1. Ubah data barang")
                print("2. Kembali ke menu utama")

                pilihan_update = input("Silahkan pilihan sub menu update: ")
                if pilihan_update == '1':
                    update_barang(daftar_barang)
                elif pilihan_update == '2':
                    break

        elif pilihan_menu == '4':
            delete_barang(daftar_barang)

        elif pilihan_menu == '5':
            break

if __name__ == "__main__":
    main()
