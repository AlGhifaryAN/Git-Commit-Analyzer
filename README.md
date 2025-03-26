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
Selain itu, unduh lexicon VADER dengan menjalankan perintah berikut di Python:

python
Copy
import nltk
nltk.download('vader_lexicon')
Cara Penggunaan
Jalankan di dalam Repository Git:
Pastikan Anda menjalankan script ini di dalam direktori repository Git yang ingin dianalisis, karena alat ini membutuhkan akses ke log commit Git.

Jalankan Program:
Dari terminal, jalankan:

bash
Copy
python git_commit_analyzer.py
Hasil Analisis:
Program akan:

Menampilkan statistik dasar seperti jumlah commit dan rata-rata skor sentimen.

Menampilkan grafik batang frekuensi commit per hari.

Menampilkan histogram distribusi skor sentimen.

Mencetak daftar kata yang paling sering muncul dalam pesan commit.

Struktur Proyek
bash
Copy
.
├── git_commit_analyzer.py   # Script utama untuk analisis commit
└── README.md                # Dokumentasi proyek
Pengembangan Selanjutnya
Beberapa ide pengembangan untuk proyek ini:

Menambahkan fitur analisis waktu commit berdasarkan jam.

Integrasi dengan sistem CI/CD untuk menghasilkan laporan otomatis.

Menyimpan output analisis dalam format file (misalnya, CSV atau HTML).

Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki ide, perbaikan, atau fitur baru, silakan buat fork repositori ini, buat pull request, atau buka issue untuk diskusi.

Lisensi
Proyek ini dilisensikan di bawah MIT License.

yaml
Copy

---

Jika Anda ingin membuat file **README.md** secara otomatis menggunakan Python, Anda juga dapat menjalankan skrip berikut:

```python
readme_content = """# Git Commit Analyzer

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
Selain itu, unduh lexicon VADER dengan menjalankan perintah berikut di Python:

python
Copy
import nltk
nltk.download('vader_lexicon')
Cara Penggunaan
Jalankan di dalam Repository Git:
Pastikan Anda menjalankan script ini di dalam direktori repository Git yang ingin dianalisis, karena alat ini membutuhkan akses ke log commit Git.

Jalankan Program:
Dari terminal, jalankan:

bash
Copy
python git_commit_analyzer.py
Hasil Analisis:
Program akan:

Menampilkan statistik dasar seperti jumlah commit dan rata-rata skor sentimen.

Menampilkan grafik batang frekuensi commit per hari.

Menampilkan histogram distribusi skor sentimen.

Mencetak daftar kata yang paling sering muncul dalam pesan commit.

Struktur Proyek
bash
Copy
.
├── git_commit_analyzer.py   # Script utama untuk analisis commit
└── README.md                # Dokumentasi proyek
Pengembangan Selanjutnya
Beberapa ide pengembangan untuk proyek ini:

Menambahkan fitur analisis waktu commit berdasarkan jam.

Integrasi dengan sistem CI/CD untuk menghasilkan laporan otomatis.

Menyimpan output analisis dalam format file (misalnya, CSV atau HTML).

Kontribusi
Kontribusi sangat diterima! Jika Anda memiliki ide, perbaikan, atau fitur baru, silakan buat fork repositori ini, buat pull request, atau buka issue untuk diskusi.

Lisensi
Proyek ini dilisensikan di bawah MIT License. """
