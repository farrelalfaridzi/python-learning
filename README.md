# Dokumentasi Belajar Python & Project Game RPG

Selamat datang di repositori dokumentasi belajar pemrograman Python gwa. Repositori ini dibuat sebagai rekam jejak dalam mendalami bahasa pemrograman Python, logika algoritma, struktur data, serta implementasi *Version Control System* menggunakan Git & GitHub.

Project utama dalam repositori ini adalah sebuah **Game RPG (Role-Playing Game) Berbasis Teks** yang dibangun dari nol untuk mengimplementasikan konsep penanganan file (*file handling*), manipulasi data, dan prinsip *clean code*.

---

## 📂 Struktur Repositori

Repositori ini dibagi menjadi beberapa direktori khusus sesuai dengan tahap pembelajaran:

* **`Project/`**: Berisi *source code* utama dari Game RPG (`rpg_v5.py`) beserta file penyimpanan data game (*save states*).
* **`Dasar/`**: Berisi skrip latihan dasar Python (Variabel, Perulangan, Percabangan, dan Fungsi).
* **`Challenge/`**: Berisi latihan pemecahan masalah (problem-solving) dan logika algoritma.

---

## 🚀 Fitur Utama Game RPG (v5)

Game RPG ini dikembangkan secara bertahap dengan fitur-fitur berikut:

1.  **Sistem Pertarungan Turn-Based**: Mekanisme pertarungan interaktif melawan monster yang muncul secara dinamis (*spawn monster*).
2.  **Manajemen Inventory (Tas)**: Logika penggunaan item (Potion, Elixir) yang aman disertai penanganan kondisi tas kosong untuk menghindari error pada data player.
3.  **Penyimpanan Data Game (Save & Load)**: Sistem *file handling* kustom yang menyimpan data player serta struktur data kompleks (List/Inventory) ke dalam file teks biasa menggunakan teknik serialisasi string (`.join()` dan `.split()`).
4.  **Sistem Penanganan Error (Error Handling)**: Proteksi game menggunakan blok `try-except` agar game tidak *crash* jika file *save-an* belum terbuat atau tidak ditemukan.

---

## 🛠️ Teknologi & Tools yang Digunakan

* **Bahasa Pemrograman**: Python 3.x
* **Version Control**: Git & GitHub (Manajemen Branch Utama: `main`)
* **Lingkungan Pengembangan**: VS Code di Linux (Fedora Enterprise)

---

## 📈 Rencana Pengembangan ke Depan

* Mengimplementasikan Pemrograman Berorientasi Objek (OOP) agar kode lebih modular.
* Menambahkan sistem papan skor lokal (*High-Score Database*).
* Memperluas sistem item, toko belanja (shop), dan sistem *crafting*.
