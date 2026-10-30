# Sistem Reservasi (Tiket / Ruangan)

## 1. Nama dan Anggota Kelompok
- Nama sistem: Sistem Reservasi (Tiket / Ruangan)
- Anggota 1: [Nama] — [NIM]
- Anggota 2: [Nama] — [NIM]
- Anggota 3: [Nama] — [NIM]
- Anggota 4 (jika ada): [Nama] — [NIM]
- Anggota 5 (jika ada): [Nama] — [NIM]

## 2. Deskripsi Sistem
Sistem Reservasi adalah program berbasis Python dengan antarmuka Command Line Interface (CLI) untuk membantu admin mengelola data reservasi tiket atau ruangan. Sistem menyediakan fitur tambah, tampil, cari, ubah status, filter status, dan hapus reservasi. Pada Tahap 1, data disimpan sementara di dalam list Python dan akan hilang ketika program ditutup.

## 3. Cara Menjalankan
1. Pastikan Python 3.8 atau lebih baru sudah terpasang.
2. Buka terminal pada folder project.
3. Jalankan perintah `python main.py`.
4. Pilih menu dengan mengetik angka 0 sampai 6.

## 4. Fitur yang Sudah Ada
1. Tambah reservasi dengan validasi kode unik, nama, jenis, detail, dan format tanggal.
2. Tampilkan seluruh data reservasi.
3. Cari berdasarkan kode (exact match) atau nama (partial match).
4. Update status dari Aktif menjadi Selesai atau Dibatalkan.
5. Filter data berdasarkan status.
6. Hapus reservasi dengan menampilkan detail dan meminta konfirmasi.

## 5. Pembagian Tugas
- [Nama anggota 1]: [Tugas yang dikerjakan]
- [Nama anggota 2]: [Tugas yang dikerjakan]
- [Nama anggota 3]: [Tugas yang dikerjakan]
- [Nama anggota 4 jika ada]: [Tugas yang dikerjakan]
- [Nama anggota 5 jika ada]: [Tugas yang dikerjakan]

## Struktur Data
Data reservasi disimpan dalam `daftar_reservasi`, yaitu sebuah list berisi dictionary. Setiap dictionary memiliki atribut wajib `kode_reservasi`, `nama_pemesan`, `jenis`, `detail`, `tanggal`, dan `status`.

## Catatan
Program ini mengikuti cakupan Tahap 1. Data belum disimpan secara permanen, dan fitur Linked List, Stack, Queue, Tree, serta Sorting merupakan tahap berikutnya sesuai addendum dosen.
