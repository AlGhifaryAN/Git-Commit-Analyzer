# Git Commit Analyzer

Git Commit Analyzer adalah sebuah alat yang ditulis dengan Python untuk menganalisis riwayat commit dari repository Git lokal Anda. Proyek ini mengekstrak data commit (seperti hash, tanggal, dan pesan commit) dan menyediakan analisis berupa:

- **Frekuensi Commit:** Visualisasi jumlah commit per hari.
- **Analisis Sentimen:** Analisis sentimen pesan commit menggunakan VADER dari pustaka NLTK.
- **Analisis Kata:** Menghitung frekuensi kata yang muncul di pesan commit.

## Fitur

- **Ekstraksi Data Commit:** Mengambil data commit dari repository Git menggunakan perintah `git log`.
- **Visualisasi:** Menampilkan grafik batang frekuensi commit per hari dan histogram distribusi skor sentimen.
- **Analisis Sentimen:** Menggunakan NLTK VADER untuk mengukur sentimen dari pesan commit.
- **Analisis Frekuensi Kata:** Menampilkan kata-kata yang paling sering digunakan dalam pesan commit.

## Instalasi

Pastikan Anda telah menginstal [Python 3](https://www.python.org/downloads/). Kemudian, instal dependensi yang diperlukan:

```bash
pip install pandas matplotlib nltk
