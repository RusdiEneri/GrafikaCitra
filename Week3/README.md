# Praktikum Grafika Komputer dan Pengolahan Citra - Week 3
## Topik: Representasi 2D dan Transformasi Geometri Dasar

Repositori ini berisi solusi lengkap, terverifikasi, dan siap dikumpulkan untuk penugasan coding Week 3 (Pertemuan 2) sesuai panduan materi PDF `Pertemuan_2_Representasi_2D_Transformasi.pdf`.

---

### 📂 Struktur Berkas di Folder `Week3/`

| Berkas | Deskripsi |
| :--- | :--- |
| `transformasi_2d.py` | Modul library fungsi transformasi 2D berbasis koordinat homogen $3 \times 3$ (Translasi, Rotasi pivot, Skala pivot, perkalian matriks terpadu). |
| `tugas1_rotasi_persegi.py` | Skrip eksekusi **Tugas 1**: Rotasi persegi 90° terhadap titik pusat massa / centroid $(0.5, 0.5)$. |
| `tugas2_simulator_2d.py` | Skrip eksekusi **Tugas 2**: Simulator 2D interaktif berbasis poligon 5 vertex dengan parameter input dinamis dari pengguna. |
| `tugas3_perbandingan_urutan.py` | Skrip eksekusi **Tugas 3**: Analisis perbandingan urutan transformasi ($T \to R \to S$ vs $S \to R \to T$) pada vertex uji $V(2, 3)$. |
| `run_all.py` | Skrip master untuk menjalankan ketiga tugas secara berurutan dan menyimpan seluruh grafik visualisasi. |
| `tugas_transformasi_2d.ipynb` | Jupyter Notebook interaktif lengkap dengan rumus LaTeX, kode program, output tabel, dan plot inline. |
| `tugas1_rotasi_persegi.png` | Tangkapan grafik hasil eksekusi Tugas 1 (Resolusi tinggi 300 DPI). |
| `tugas2_simulator_2d.png` | Tangkapan grafik hasil eksekusi Tugas 2 (Resolusi tinggi 300 DPI). |
| `tugas3_perbandingan_urutan.png` | Tangkapan grafik hasil eksekusi Tugas 3 (Resolusi tinggi 300 DPI). |
| `generate_laporan_pdf.py` | Skrip generator penyusun dokumen laporan HTML & kompilasi PDF otomatis. |
| `laporan.html` | Dokumen laporan format web dengan style CSS academic publication. |
| `Laporan_Tugas2_GrafikaCitra_Transformasi2D.pdf` | **Laporan akhir PDF resmi** siap kumpul di Google Classroom (berisi teori, rumus, tabel, grafik, kode, dan analisis). |

---

### 🚀 Cara Menjalankan Program

#### 1. Menjalankan Semua Tugas Sekaligus
```bash
python run_all.py
```
*(Tambahkan argumen `--no-show` jika ingin menjalankan secara otomatis tanpa memunculkan jendela popup Matplotlib)*:
```bash
python run_all.py --no-show
```

#### 2. Menjalankan Setiap Tugas Secara Terpisah
- **Tugas 1 (Rotasi Persegi 90° Terhadap Pusat):**
  ```bash
  python tugas1_rotasi_persegi.py
  ```
- **Tugas 2 (Simulator 2D Poligon 5 Vertex):**
  ```bash
  python tugas2_simulator_2d.py
  ```
  *(Program akan meminta input translasi $t_x, t_y$, sudut, skala $s_x, s_y$, dan pilihan pivot. Tekan Enter untuk memakai nilai default).*
- **Tugas 3 (Perbandingan Urutan Transformasi):**
  ```bash
  python tugas3_perbandingan_urutan.py
  ```

#### 3. Membuka Jupyter Notebook
Buka file `tugas_transformasi_2d.ipynb` di Jupyter Lab, VS Code Notebook, atau Google Colaboratory.

#### 4. Menghasilkan Ulang Dokumen Laporan PDF
```bash
python generate_laporan_pdf.py
```

---

### 📊 Ringkasan Rubrik Penilaian

| Komponen Rubrik | Bobot | Bukti Implementasi & Verifikasi |
| :--- | :---: | :--- |
| **Demo** | 10% | Skrip dapat dijalankan secara mandiri (`python run_all.py`), interaktif, dan non-interaktif. |
| **Rumus** | 25% | Formulasi analitik lengkap matriks homogen $3 \times 3$, rotasi pivot $M = T(p) \cdot R \cdot T(-p)$, dan perbandingan $S \cdot R \cdot T \neq T \cdot R \cdot S$. |
| **Fungsi** | 30% | Modul `transformasi_2d.py` yang modular, reusable, dan mendukung vektorisasi NumPy. |
| **Visual** | 15% | Grafik Matplotlib beresolusi tinggi (300 DPI) dengan sumbu kartesius, grid, aspect equal, legenda, label vertex, dan panah trajektori. |
| **Kode** | 10% | Struktur kode bersih (clean code PEP8), anti-slop, terdokumentasi docstring, dan penanganan input yang tangguh. |
| **Analisis** | 10% | Penjelasan mendalam mengenai simetri $C_4$ persegi (Tugas 1) dan sifat non-komutatif aljabar matriks serta amplifikasi translasi (Tugas 3). |
