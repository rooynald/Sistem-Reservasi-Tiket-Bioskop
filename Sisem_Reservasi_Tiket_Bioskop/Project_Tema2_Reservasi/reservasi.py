# Modul pengelolaan data reservasi Tahap 1
# Struktur data: Array of Struct (list of dict)

daftar_reservasi = []


def format_tanggal_valid(tanggal):
    """Memeriksa format YYYY-MM-DD sesuai ketentuan Tahap 1."""
    if not tanggal or tanggal.count("-") != 2:
        return False
    bagian = tanggal.split("-")
    return (
        len(bagian) == 3
        and len(bagian[0]) == 4
        and len(bagian[1]) == 2
        and len(bagian[2]) == 2
        and all(item.isdigit() for item in bagian)
    )


def cari_indeks_kode(kode):
    """Mengembalikan indeks reservasi berdasarkan kode, atau -1 jika tidak ada."""
    for indeks, reservasi in enumerate(daftar_reservasi):
        if reservasi["kode_reservasi"].lower() == kode.lower():
            return indeks
    return -1


def tampilkan_tabel(data):
    """Menampilkan daftar reservasi dalam format tabel teks."""
    if not data:
        print("Belum ada data reservasi yang tersimpan.")
        return

    print("-" * 112)
    print(f"{'No':<4} {'Kode':<12} {'Nama Pemesan':<22} {'Jenis':<10} {'Detail':<24} {'Tanggal':<12} {'Status':<14}")
    print("-" * 112)
    for nomor, item in enumerate(data, start=1):
        print(
            f"{nomor:<4} {item['kode_reservasi']:<12} "
            f"{item['nama_pemesan'][:21]:<22} {item['jenis']:<10} "
            f"{item['detail'][:23]:<24} {item['tanggal']:<12} [{item['status']}]"
        )
    print("-" * 112)
    print(f"Jumlah data: {len(data)}")


def tambah_reservasi():
    print("\n=== TAMBAH RESERVASI ===")
    kode = input("Kode reservasi: ").strip()
    if not kode:
        print("Error: Kode reservasi tidak boleh kosong.")
        return
    if len(kode) < 3:
        print("Error: Kode reservasi minimal 3 karakter.")
        return
    if cari_indeks_kode(kode) != -1:
        print("Error: Kode reservasi sudah digunakan.")
        return

    nama = input("Nama pemesan: ").strip()
    if not nama:
        print("Error: Nama pemesan tidak boleh kosong.")
        return

    jenis_input = input("Jenis (Ruangan/Tiket): ").strip().lower()
    if jenis_input not in ("ruangan", "tiket"):
        print("Error: Jenis hanya boleh Ruangan atau Tiket.")
        return
    jenis = jenis_input.capitalize()

    detail = input("Detail ruangan/nama acara: ").strip()
    if not detail:
        print("Error: Detail tidak boleh kosong.")
        return

    tanggal = input("Tanggal (YYYY-MM-DD): ").strip()
    if not format_tanggal_valid(tanggal):
        print("Format tanggal salah. Gunakan format YYYY-MM-DD, contoh: 2026-10-15.")
        return

    data = {
        "kode_reservasi": kode,
        "nama_pemesan": nama,
        "jenis": jenis,
        "detail": detail,
        "tanggal": tanggal,
        "status": "Aktif",
    }
    daftar_reservasi.append(data)
    print(f"Reservasi {kode} atas nama {nama} berhasil ditambahkan.")


def tampilkan_semua_reservasi():
    print("\n=== SEMUA RESERVASI ===")
    tampilkan_tabel(daftar_reservasi)


def cari_reservasi():
    print("\n=== CARI RESERVASI ===")
    print("1. Berdasarkan kode")
    print("2. Berdasarkan nama pemesan")
    pilihan = input("Pilih mode pencarian (1/2): ").strip()
    kata_kunci = input("Masukkan kata kunci: ").strip()
    if not kata_kunci:
        print("Error: Kata kunci tidak boleh kosong.")
        return

    if pilihan == "1":
        indeks = cari_indeks_kode(kata_kunci)
        if indeks == -1:
            print(f"Reservasi dengan kode '{kata_kunci}' tidak ditemukan.")
        else:
            tampilkan_tabel([daftar_reservasi[indeks]])
    elif pilihan == "2":
        hasil = [
            item for item in daftar_reservasi
            if kata_kunci.lower() in item["nama_pemesan"].lower()
        ]
        if not hasil:
            print(f"Reservasi dengan nama pemesan '{kata_kunci}' tidak ditemukan.")
        else:
            tampilkan_tabel(hasil)
    else:
        print("Pilihan mode pencarian tidak valid.")


def update_status_reservasi():
    print("\n=== UPDATE STATUS RESERVASI ===")
    kode = input("Kode reservasi: ").strip()
    indeks = cari_indeks_kode(kode)
    if indeks == -1:
        print(f"Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    item = daftar_reservasi[indeks]
    if item["status"] in ("Selesai", "Dibatalkan"):
        print("Status reservasi ini sudah final dan tidak bisa diubah lagi.")
        return

    status_input = input("Status baru (Selesai/Dibatalkan): ").strip().lower()
    if status_input not in ("selesai", "dibatalkan"):
        print("Error: Status baru hanya boleh Selesai atau Dibatalkan.")
        return

    status_lama = item["status"]
    status_baru = status_input.capitalize()
    item["status"] = status_baru
    print(
        f"Status reservasi {kode} atas nama {item['nama_pemesan']} "
        f"berhasil diperbarui: {status_lama} menjadi {status_baru}."
    )


def filter_reservasi_status():
    print("\n=== FILTER RESERVASI BERDASARKAN STATUS ===")
    status_input = input("Pilih status (Aktif/Selesai/Dibatalkan): ").strip().lower()
    pilihan_status = {
        "aktif": "Aktif",
        "selesai": "Selesai",
        "dibatalkan": "Dibatalkan",
    }
    if status_input not in pilihan_status:
        print("Error: Status harus Aktif, Selesai, atau Dibatalkan.")
        return

    status = pilihan_status[status_input]
    hasil = [item for item in daftar_reservasi if item["status"] == status]
    if not hasil:
        print(f"Tidak ada reservasi dengan status '{status}'.")
        return

    print(f"Menampilkan reservasi dengan status: {status} ({len(hasil)} data)")
    tampilkan_tabel(hasil)


def hapus_reservasi():
    print("\n=== HAPUS RESERVASI ===")
    kode = input("Kode reservasi yang akan dihapus: ").strip()
    indeks = cari_indeks_kode(kode)
    if indeks == -1:
        print(f"Reservasi dengan kode '{kode}' tidak ditemukan.")
        return

    item = daftar_reservasi[indeks]
    print("\nData yang akan dihapus:")
    print(f"Kode       : {item['kode_reservasi']}")
    print(f"Nama       : {item['nama_pemesan']}")
    print(f"Jenis      : {item['jenis']}")
    print(f"Detail     : {item['detail']}")
    print(f"Tanggal    : {item['tanggal']}")
    print(f"Status     : {item['status']}")

    konfirmasi = input("Yakin hapus reservasi ini? (y/n): ").strip().lower()
    if konfirmasi == "y":
        daftar_reservasi.pop(indeks)
        print(f"Reservasi {kode} atas nama {item['nama_pemesan']} berhasil dihapus dari sistem.")
    else:
        print("Penghapusan dibatalkan.")
