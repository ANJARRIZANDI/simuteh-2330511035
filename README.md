# SIMUTEH
## Sistem Pemeriksaan Mutu Daun Teh Berbasis Citra
### Computer Vision – Digital Image Processing

SIMUTEH merupakan proyek praktikum **Computer Vision** yang berfokus pada pengolahan dan analisis citra daun teh. Proyek ini menerapkan teknik pengolahan citra untuk menganalisis warna, histogram, mengurangi derau, meningkatkan kualitas citra, mendeteksi tepi, serta menganalisis bercak pada daun teh sebelum digunakan pada tahap analisis berikutnya.

Proyek ini menggunakan dataset sintetis dan dikembangkan menggunakan Python, OpenCV, serta Google Colab. Hasil pengujian bersifat ilustratif dan belum menjadi acuan diagnosis penyakit tanaman secara langsung.

---

## 1. Tujuan Proyek

1. Menganalisis karakteristik warna citra daun teh.
2. Mempelajari histogram dan teknik peningkatan kontras.
3. Menerapkan konvolusi dan penapisan citra.
4. Mengurangi derau dengan mempertahankan detail bercak.
5. Menyusun dan mengevaluasi rangkaian praproses citra daun teh.
6. Menerapkan berbagai metode deteksi tepi pada citra daun teh.
7. Mempelajari operasi morfologi untuk memperbaiki mask bercak.
8. Menganalisis komponen terhubung dan mengukur karakteristik bercak daun teh.
9. Mengintegrasikan proses analisis bercak ke dalam modul SIMUTEH.

## 2. Teknologi dan Lingkungan

| Komponen | Versi |
|---|---|
| Python | 3.13.18 |
| OpenCV | 5.0.0 |
| NumPy | 2.1.3 |
| Matplotlib | 3.10.0 |
| scikit-image | 0.25.2 |
| Pandas | 2.2.3 |
| Pillow | 11.3.0 |
| Platform | Google Colab |

## 3. Dataset

Dataset sintetis terdiri dari 60 citra daun teh dengan pembagian sebagai berikut:

| Kelas | Jumlah |
|---|---:|
| Sehat | 20 |
| Ringan | 20 |
| Berat | 20 |
| **Total** | **60** |

Setiap kelas memiliki lima kondisi pencahayaan, yaitu normal, gelap, terang, kontras rendah, dan bayangan. Setiap kondisi diwakili oleh empat citra.

Pembangkitan dataset menggunakan nilai SEED berikut:

```python
SEED = 1035
```

Nilai SEED digunakan agar dataset sintetis dapat dibuat kembali dengan konfigurasi generator yang sama.

## 4. Struktur Repository

```text
simuteh-2330511035/
│
├── data/
│   └── sintetis/
│       ├── citra/
│       ├── bersih/
│       ├── mask_daun/
│       ├── mask_bercak/
│       └── label.csv
│
├── hasil/
│   ├── param_praproses.json
│   ├── p5_tabel_tepi.csv
│   ├── p5_f1_kondisi.png
│   ├── p6_eksperimen_se.csv
│   ├── p6_scatter_komponen.png
│   ├── p6_evaluasi_bercak.csv
│   └── ...
│
├── notebook/
│   ├── B1_lingkungan.ipynb
│   ├── B2_citra_warna.ipynb
│   ├── B3_histogram.ipynb
│   ├── B4_penapisan.ipynb
│   ├── B5_praproses.ipynb
│   ├── P5_tepi.ipynb
│   └── P6_morfologi.ipynb
│
├── src/
│   ├── utils_cv.py
│   ├── praproses.py
│   ├── utils_tepi.py
│   ├── bercak.py
│   └── data_sintetis.py
│
├── laporan/
│
├── requirements.txt
│
└── README.md
```

**Keterangan folder:**

- `data/sintetis/`: Menyimpan dataset citra daun teh, citra bersih, mask daun, mask bercak, dan label dataset.
- `hasil/`: Menyimpan hasil pengujian, tabel evaluasi, grafik, serta parameter praproses.
- `notebook/`: Menyimpan seluruh notebook praktikum dari tahap persiapan hingga analisis morfologi.
- `src/`: Menyimpan modul Python untuk pengolahan citra, praproses, deteksi tepi, dan analisis bercak.
- `laporan/`: Menyimpan dokumen laporan praktikum.
- `requirements.txt`: Menyimpan daftar pustaka yang diperlukan untuk menjalankan proyek.

## 5. Tahapan Praktikum

| Notebook | Tahapan | Kegiatan |
|---|---|---|
| B1 | Lingkungan | Persiapan lingkungan dan dataset |
| B2 | Citra warna | Analisis kanal warna, sampling, dan kuantisasi |
| B3 | Histogram | Analisis histogram dan perbaikan citra |
| B4 | Penapisan | Konvolusi dan pengurangan derau |
| B5 | Praproses | Integrasi dan evaluasi rangkaian praproses |
| P5 | Deteksi tepi | Gradien citra, operator Sobel, Prewitt, LoG, Canny, serta evaluasi deteksi tepi |
| P6 | Morfologi dan komponen terhubung | Erosi, dilasi, opening, closing, analisis komponen, pengukuran bercak, dan integrasi modul analisis bercak |

## 6. Parameter Final Praproses

| Parameter | Nilai |
|---|---|
| Lebar citra | 640 piksel |
| Gamma | 1.0 |
| CLAHE clip limit | 2.0 |
| CLAHE tile | 8 × 8 |
| Penapis | Median |
| Kernel | 3 × 3 |
| Sigma | 1.0 (tidak digunakan oleh median filter) |
| Penajaman | 0.0 (tidak diterapkan) |
| Kanal analisis | R (Red) |

Urutan proses meliputi resize, koreksi gamma, CLAHE pada kanal V, reduksi derau menggunakan median filter, dan penajaman opsional.

## 7. Ringkasan Hasil Pengujian

### 7.1 Hasil Analisis Kanal Warna

Kanal R menghasilkan nilai Kontras Bercak (KB) tertinggi pada lima kondisi pencahayaan kelas berat, yaitu:

| Kondisi | KB Kanal R |
|---|---:|
| Normal | 9.95 |
| Gelap | 10.86 |
| Terang | 8.55 |
| Kontras rendah | 3.19 |
| Bayangan | 5.38 |

Berdasarkan hasil tersebut, kanal R dipilih sebagai kanal analisis untuk pengukuran kontras bercak.

### 7.2 Hasil Penapisan

Median filter 3 × 3 menghasilkan PSNR sebesar 48.18 dB pada pengujian derau salt-and-pepper 4%.

Pada 12 citra normal, rata-rata PSNR meningkat dari 28.49 dB menjadi 35.83 dB setelah menggunakan median filter 3 × 3.

### 7.3 Hasil Praproses

Perubahan nilai KB sebelum dan sesudah praproses ditampilkan pada tabel berikut:

| Kondisi | KB Sebelum | KB Sesudah | Perubahan |
|---|---:|---:|---:|
| Normal | 8.93 | 10.42 | +16.69% |
| Gelap | 10.54 | 17.14 | +62.62% |
| Terang | 7.66 | 6.66 | -13.05% |
| Kontras rendah | 3.23 | 4.09 | +26.63% |
| Bayangan | 4.46 | 7.22 | +61.88% |

Praproses meningkatkan KB pada empat kondisi pencahayaan, sedangkan kondisi terang mengalami penurunan.

Pengujian pada lima citra sehat yang ditampilkan tidak menunjukkan titik atau area terang baru yang jelas menyerupai bercak. Hasil ini terbatas pada sampel visual yang diperiksa.

### 7.4 Hasil Praktikum P5 – Deteksi Tepi

Praktikum P5 menerapkan beberapa operator deteksi tepi, yaitu Sobel, Prewitt, Laplacian of Gaussian (LoG), dan Canny.

Pengujian dilakukan menggunakan kanal Gray dan kanal R, baik pada citra mentah maupun citra hasil praproses. Evaluasi menggunakan metrik Precision, Recall, dan F1-Score dengan membandingkan hasil deteksi terhadap tepi acuan dari mask daun dan mask bercak.

Hasil pengujian menunjukkan bahwa kombinasi citra mentah dengan kanal R dan operator Canny menghasilkan rata-rata F1-Score tertinggi sebesar 0.973.

| Sumber | Kanal | Metode | Precision | Recall | F1-Score |
|---|---|---|---:|---:|---:|
| Mentah | R | Canny | 0.982 | 0.968 | 0.973 |
| Mentah | R | LoG | 0.883 | 0.997 | 0.928 |
| Mentah | Gray | Prewitt | 0.812 | 0.961 | 0.872 |
| Praproses | R | Canny | 0.956 | 0.988 | 0.970 |
| Praproses | R | LoG | 0.792 | 0.997 | 0.869 |

Eksperimen Canny menunjukkan bahwa kanal R dengan ambang tetap 30/90 dan sigma 2.0 memberikan hasil yang relatif konsisten pada lima kondisi pencahayaan, dengan F1-Score antara 0.956 hingga 0.982 pada pengujian yang dilakukan.

Pada eksperimen ambang persentil, kanal R dengan persentil 98 menghasilkan rata-rata F1-Score sebesar 0.918.

Hasil tersebut menunjukkan bahwa pemilihan kanal warna, metode deteksi tepi, dan parameter ambang berpengaruh terhadap kualitas deteksi tepi.

File hasil pengujian disimpan pada:

- `hasil/p5_tabel_tepi.csv`
- `hasil/p5_f1_kondisi.png`

### 7.5 Hasil Praktikum P6 – Operasi Morfologi dan Komponen Terhubung

Praktikum P6 menerapkan operasi morfologi untuk memperbaiki mask bercak dan menganalisis komponen terhubung pada citra daun teh.

Operasi yang diterapkan meliputi:

1. Erosi untuk mengurangi area objek.
2. Dilasi untuk memperbesar area objek.
3. Opening untuk menghilangkan objek kecil atau noise.
4. Closing untuk menutup celah kecil pada objek.
5. Analisis structuring element dengan bentuk persegi, elips, dan silang.

Pengujian menggunakan ukuran structuring element 3 × 3, 5 × 5, dan 7 × 7 serta variasi parameter deteksi bercak.

Pada pengujian awal terhadap tiga citra, mask daun menghasilkan nilai IoU sebesar 0.996, 0.998, dan 0.999.

Hasil eksperimen menunjukkan bahwa kombinasi operasi opening dan closing serta penyaringan berdasarkan luas, kebulatan, dan rasio aspek dapat mengurangi jumlah komponen yang tidak sesuai.

Pada pengujian penyaringan komponen, aturan luas minimal 20 piksel, kebulatan minimal 0.5, dan rasio aspek maksimal 1.8 menghasilkan rata-rata galat jumlah komponen:

| Kelas | Rata-rata Galat |
|---|---:|
| Berat | 1.75 |
| Ringan | 0.65 |
| Sehat | 0.25 |

Pengukuran komponen bercak juga dilakukan menggunakan beberapa karakteristik, yaitu:

- Luas dalam piksel.
- Luas dalam mm².
- Keliling.
- Kebulatan.
- Rasio aspek.
- Titik pusat komponen.

Pada pengujian citra `teh_041.png`, ditemukan 8 komponen bercak setelah proses morfologi.

### 7.6 Hasil Integrasi Modul Analisis Bercak

Tahap integrasi dilakukan dengan menggunakan modul `bercak.py` untuk menggabungkan proses praproses, deteksi bercak, pengukuran persentase bercak, dan klasifikasi kondisi daun.

Evaluasi dilakukan terhadap seluruh 60 citra sintetis.

Hasil pengujian menunjukkan:

| Metrik | Hasil |
|---|---:|
| Galat absolut rerata persentase bercak | 0.606 |
| Korelasi prediksi dan acuan | 0.852 |
| Akurasi klasifikasi | 0.333 (33.3%) |

Hasil klasifikasi menunjukkan bahwa seluruh 20 citra sehat berhasil diklasifikasikan sebagai sehat. Namun, pada kelas bercak ringan dan berat masih terdapat kesalahan klasifikasi.

Kesalahan tersebut terutama berkaitan dengan perbedaan jumlah dan luas bercak hasil prediksi terhadap mask acuan. Beberapa bercak kecil atau bercak dengan intensitas rendah belum terdeteksi secara optimal.

Hasil ini menunjukkan bahwa modul analisis bercak masih memerlukan penyempurnaan, terutama pada proses segmentasi, penyaringan komponen, dan penentuan batas klasifikasi.

File hasil pengujian disimpan pada:

- `hasil/p6_eksperimen_se.csv`
- `hasil/p6_scatter_komponen.png`
- `hasil/p6_evaluasi_bercak.csv`

## 8. Cara Menjalankan Proyek

Proyek dijalankan menggunakan Google Colab dengan langkah-langkah berikut.

### 8.1 Clone Repository

Jalankan perintah berikut pada cell Google Colab:

```bash
!git clone https://github.com/ANJARRIZANDI/simuteh-2330511035.git
```

### 8.2 Masuk ke Folder Proyek

```python
%cd /content/simuteh-2330511035
```

### 8.3 Buka Folder Notebook

```python
%cd /content/simuteh-2330511035/notebook
```

### 8.4 Jalankan Notebook

Buka dan jalankan notebook secara berurutan:

1. `B1_lingkungan.ipynb`
2. `B2_citra_warna.ipynb`
3. `B3_histogram.ipynb`
4. `B4_penapisan.ipynb`
5. `B5_praproses.ipynb`
6. `P5_tepi.ipynb`
7. `P6_morfologi.ipynb`

Gunakan menu **Runtime → Restart session and run all** pada setiap notebook untuk menguji ulang seluruh proses. Pastikan semua cell berhasil dijalankan dan hasil pengujian tersimpan pada folder `hasil`.

**Catatan:** Notebook P5 dan P6 membutuhkan modul pendukung yang tersedia pada folder `src`, serta dataset dan parameter praproses yang telah dibuat pada tahap sebelumnya.

## 9. Reproduksibilitas dan Versi

Reproduksibilitas proyek didukung oleh pencatatan SEED, versi pustaka, dan parameter praproses. Konfigurasi praproses disimpan dalam file `hasil/param_praproses.json`.

| Informasi | Keterangan |
|---|---|
| Nama proyek | SIMUTEH |
| Bidang | Computer Vision |
| SEED | 1035 |
| Parameter praproses | `param_praproses.json` |
| Versi repository | `v0.1-praproses` |

## Riwayat Versi Proyek

1. **`v0.1-praproses`** digunakan sebagai penanda versi proyek setelah penyelesaian tahap praproses citra.

2. **`v0.2-tepi`** digunakan sebagai penanda versi proyek setelah penyelesaian tahap deteksi tepi.

3. **`v0.3-morfologi`** digunakan sebagai penanda versi proyek setelah penyelesaian tahap operasi morfologi dan komponen terhubung.

## 10. Repository

**GitHub:** [ANJARRIZANDI/simuteh-2330511035](https://github.com/ANJARRIZANDI/simuteh-2330511035)

---

**SIMUTEH – Computer Vision Project**  
Pengolahan dan Analisis Citra Digital Daun Teh.
