# SIMUTEH
## Sistem Pemeriksaan Mutu Daun Teh Berbasis Citra
### Computer Vision – Digital Image Processing

SIMUTEH merupakan proyek praktikum **Computer Vision** yang berfokus pada pengolahan dan analisis citra daun teh. Proyek ini menerapkan teknik pengolahan citra untuk menganalisis warna, histogram, mengurangi derau, serta meningkatkan kualitas citra sebelum digunakan pada tahap analisis berikutnya.

Proyek ini menggunakan dataset sintetis dan dikembangkan menggunakan Python, OpenCV, serta Google Colab. Hasil pengujian bersifat ilustratif dan belum menjadi acuan diagnosis penyakit tanaman secara langsung.

---

## 1. Tujuan Proyek

1. Menganalisis karakteristik warna citra daun teh.
2. Mempelajari histogram dan teknik peningkatan kontras.
3. Menerapkan konvolusi dan penapisan citra.
4. Mengurangi derau dengan mempertahankan detail bercak.
5. Menyusun dan mengevaluasi rangkaian praproses citra daun teh.

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
│   └── ...
│
├── notebook/
│   ├── B1_lingkungan.ipynb
│   ├── B2_citra_warna.ipynb
│   ├── B3_histogram.ipynb
│   ├── B4_penapisan.ipynb
│   └── B5_praproses.ipynb
│
├── src/
│   ├── utils_cv.py
│   └── praproses.py
│
└── README.md
```

## 5. Tahapan Praktikum

| Notebook | Tahapan | Kegiatan |
|---|---|---|
| B1 | Lingkungan | Persiapan lingkungan dan dataset |
| B2 | Citra warna | Analisis kanal warna, sampling, dan kuantisasi |
| B3 | Histogram | Analisis histogram dan perbaikan citra |
| B4 | Penapisan | Konvolusi dan pengurangan derau |
| B5 | Praproses | Integrasi dan evaluasi rangkaian praproses |

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

Gunakan menu **Runtime → Restart session and run all** pada setiap notebook untuk menguji ulang seluruh proses. Pastikan semua cell berhasil dijalankan dan hasil pengujian tersimpan pada folder `hasil`.

## 9. Reproduksibilitas dan Versi

Reproduksibilitas proyek didukung oleh pencatatan SEED, versi pustaka, dan parameter praproses. Konfigurasi praproses disimpan dalam file `hasil/param_praproses.json`.

| Informasi | Keterangan |
|---|---|
| Nama proyek | SIMUTEH |
| Bidang | Computer Vision |
| SEED | 1035 |
| Parameter praproses | `param_praproses.json` |
| Versi repository | `v0.1-praproses` |

Tag `v0.1-praproses` digunakan sebagai penanda versi proyek setelah penyelesaian tahap praproses.

## 10. Repository

**GitHub:** [ANJARRIZANDI/simuteh-2330511035](https://github.com/ANJARRIZANDI/simuteh-2330511035)

---

**SIMUTEH – Computer Vision Project**  
Pengolahan dan Analisis Citra Digital Daun Teh.
