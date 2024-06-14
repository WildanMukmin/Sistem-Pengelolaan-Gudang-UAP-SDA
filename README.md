# Sistem-Pengelolaan-Gudang-UAP-SDA
Tugas Akhir Struktur Data dan Algortima Prakter

# Nama-nama Anggota:
1. Wildan Mukmin 2317051080
2. Syauqi Rahmat 2317051084

# Manajemen Inventaris Gudang

Repositori ini berisi aplikasi Python untuk mengelola inventaris di gudang menggunakan file CSV untuk penyimpanan. Aplikasi ini menyediakan fungsionalitas untuk menambahkan, menghapus, memperbarui, mencari, dan mengurutkan barang dalam inventaris melalui antarmuka pengguna grafis (GUI) yang dibangun dengan Tkinter.

## Fitur

- **Tambah Barang**: Menambahkan barang baru ke inventaris.
- **Hapus Barang**: Menghapus barang dari inventaris berdasarkan nama atau ID.
- **Perbarui Barang**: Memperbarui nama, jumlah, atau harga barang.
- **Cari Barang**: Mencari barang berdasarkan nama.
- **Tampilkan Semua Barang**: Menampilkan semua barang di inventaris.
- **Urutkan Barang**: Mengurutkan barang berdasarkan ID, jumlah, atau harga.

## Prasyarat

- Python 3.x
- Tkinter (sudah termasuk dalam distribusi standar Python)

## Instalasi

1. Clone repositori ini:

    ```sh
    git clone https://github.com/your-username/gudang-inventory-management.git
    cd gudang-inventory-management
    ```

2. Instal paket-paket yang diperlukan (jika ada):

    ```sh
    pip install -r requirements.txt
    ```

3. Pastikan ada file `items.csv` di direktori dengan header berikut:

    ```csv
    id,name,quantity,price
    ```

## Penggunaan

Jalankan aplikasi menggunakan perintah berikut:

```sh
python gudang_inventory.py
```

## Ringkasan Kode

### Akses File

Fungsi untuk membaca dan menulis file CSV:

- `readFileCsv(fileName)`: Membaca barang dari file CSV dan mengembalikan daftar objek `Item`.
- `updateFileCsv()`: Menulis daftar barang saat ini ke file CSV.

### Algoritma Pengurutan

Fungsi untuk mengurutkan barang menggunakan merge sort:

- `mergeSort(arr, parameter)`: Mengurutkan daftar barang secara rekursif berdasarkan parameter yang ditentukan.
- `merge(left, right, parameter)`: Menggabungkan dua daftar yang sudah diurutkan menjadi satu daftar yang terurut.

### Algoritma Pencarian

Fungsi untuk mencari barang menggunakan binary search:

- `binarySearch(arr, target_id)`: Mencari barang berdasarkan ID-nya dan mengembalikan indeksnya.

### Kelas Item dan Gudang

- `Item`: Merepresentasikan barang dengan atribut ID, nama, jumlah, dan harga.
- `Gudang`: Mengelola daftar objek `Item` dan menyediakan metode untuk memanipulasi inventaris.

### Aplikasi GUI

- `GudangApp`: GUI berbasis Tkinter untuk mengelola inventaris, menyediakan tombol dan bidang teks untuk interaksi pengguna.

## Komponen GUI

- **Navigasi Frame**: Berisi tombol untuk berbagai tindakan (misalnya, Tampilkan Semua, Tambah Barang, Hapus Barang, Cari Barang, Perbarui Barang, Urutkan berdasarkan Harga, Urutkan berdasarkan Jumlah, Urutkan berdasarkan ID).
- **Konten Frame**: Menampilkan konten berdasarkan tindakan yang dipilih.

### Contoh Tindakan GUI

- **Tampilkan Semua Barang**: Menampilkan semua barang di inventaris.
- **Tambah Barang**: Meminta pengguna memasukkan detail barang dan menambahkan barang ke inventaris.
- **Hapus Barang**: Meminta pengguna memasukkan nama barang yang akan dihapus.
- **Cari Barang**: Meminta pengguna memasukkan nama barang yang ingin dicari.
- **Urutkan berdasarkan Harga**: Mengurutkan barang berdasarkan harga.
- **Urutkan berdasarkan Jumlah**: Mengurutkan barang berdasarkan jumlah.
- **Urutkan berdasarkan ID**: Mengurutkan barang berdasarkan ID.

## Kontribusi

1. Fork repositori ini.
2. Buat branch baru (`git checkout -b fitur-baru`).
3. Lakukan perubahan Anda dan commit (`git commit -m 'Tambahkan beberapa fitur'`).
4. Push ke branch (`git push origin fitur-baru`).
5. Buat Pull Request baru.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT - lihat file [LICENSE](LICENSE) untuk detail lebih lanjut.

---

Silakan sesuaikan file `README.md` ini lebih lanjut sesuai kebutuhan spesifik Anda atau tambahkan lebih banyak bagian jika diperlukan.