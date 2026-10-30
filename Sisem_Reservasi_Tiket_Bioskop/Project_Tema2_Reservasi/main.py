from reservasi import (
    tambah_reservasi,
    tampilkan_semua_reservasi,
    cari_reservasi,
    update_status_reservasi,
    filter_reservasi_status,
    hapus_reservasi,
)


def tampilkan_menu():
    print("\n" + "=" * 44)
    print("       SISTEM RESERVASI TIKET / RUANGAN")
    print("=" * 44)
    print("1. Tambah reservasi baru")
    print("2. Tampilkan semua reservasi")
    print("3. Cari reservasi")
    print("4. Update status reservasi")
    print("5. Filter reservasi berdasarkan status")
    print("6. Hapus reservasi")
    print("0. Keluar")
    print("=" * 44)


def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-6): ").strip()

        if pilihan == "1":
            tambah_reservasi()
        elif pilihan == "2":
            tampilkan_semua_reservasi()
        elif pilihan == "3":
            cari_reservasi()
        elif pilihan == "4":
            update_status_reservasi()
        elif pilihan == "5":
            filter_reservasi_status()
        elif pilihan == "6":
            hapus_reservasi()
        elif pilihan == "0":
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka 0 sampai 6.")


if __name__ == "__main__":
    main()
