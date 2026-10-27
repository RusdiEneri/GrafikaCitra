"""
Script untuk menyusun dokumen laporan akademik lengkap dalam format HTML + CSS
dan mengompilasinya menjadi PDF berstandar publikasi:
'Laporan_Tugas2_GrafikaCitra_Transformasi2D.pdf'
"""

import os
import base64
import subprocess

WEEK3_DIR = r"c:\Users\Administrator\Documents\PROJECT-GITHUB\GrafikaCitra\Week3"
IMG_T1 = os.path.join(WEEK3_DIR, "tugas1_rotasi_persegi.png")
IMG_T2 = os.path.join(WEEK3_DIR, "tugas2_simulator_2d.png")
IMG_T3 = os.path.join(WEEK3_DIR, "tugas3_perbandingan_urutan.png")
HTML_OUT = os.path.join(WEEK3_DIR, "laporan.html")
PDF_OUT = os.path.join(WEEK3_DIR, "Laporan_Tugas2_GrafikaCitra_Transformasi2D.pdf")


def get_base64_img(filepath):
    if os.path.exists(filepath):
        with open(filepath, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded}"
    return ""


def build_html():
    b64_t1 = get_base64_img(IMG_T1)
    b64_t2 = get_base64_img(IMG_T2)
    b64_t3 = get_base64_img(IMG_T3)

    html_content = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Laporan Praktikum Grafika Komputer - Transformasi 2D</title>
<style>
    @page {{
        size: A4 portrait;
        margin: 1.5cm 1.4cm 1.5cm 1.4cm;
    }}
    * {{
        box-sizing: border-box;
    }}
    body {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        color: #2c3e50;
        line-height: 1.5;
        font-size: 9.5pt;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }}
    .header-box {{
        text-align: center;
        border-bottom: 2.5px solid #2980b9;
        padding-bottom: 10px;
        margin-bottom: 16px;
    }}
    .header-box h1 {{
        margin: 0 0 4px 0;
        font-size: 15.5pt;
        color: #1a365d;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .header-box h2 {{
        margin: 0 0 4px 0;
        font-size: 11pt;
        color: #2980b9;
        font-weight: 600;
    }}
    .header-box p {{
        margin: 0;
        font-size: 9pt;
        color: #636e72;
    }}
    .rubrik-badge {{
        display: inline-block;
        background: #ebf5fb;
        border: 1px solid #aed6f1;
        border-radius: 4px;
        padding: 4px 10px;
        margin-top: 6px;
        font-size: 8pt;
        color: #1b4f72;
    }}
    h2.section-title {{
        color: #1a365d;
        border-left: 4.5px solid #2980b9;
        padding-left: 8px;
        font-size: 11pt;
        margin-top: 18px;
        margin-bottom: 8px;
        text-transform: uppercase;
        page-break-after: avoid;
    }}
    h3.sub-title {{
        color: #2c3e50;
        font-size: 9.8pt;
        margin-top: 12px;
        margin-bottom: 5px;
        font-weight: 700;
        page-break-after: avoid;
    }}
    p, li {{
        text-align: justify;
    }}
    .formula-box {{
        background-color: #f8f9fa;
        border-left: 3.5px solid #3498db;
        padding: 8px 12px;
        margin: 8px 0;
        border-radius: 0 4px 4px 0;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 8.8pt;
        color: #2c3e50;
        page-break-inside: avoid;
    }}
    .matrix-display {{
        display: inline-block;
        vertical-align: middle;
        margin: 4px 0;
        font-family: 'Consolas', monospace;
        font-size: 8.2pt;
        background: #ffffff;
        padding: 5px 8px;
        border: 1px solid #dcdde1;
        border-radius: 4px;
        line-height: 1.35;
    }}
    table.data-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 8px 0;
        font-size: 8.2pt;
        page-break-inside: avoid;
    }}
    table.data-table th {{
        background-color: #2980b9;
        color: #ffffff;
        padding: 6px 8px;
        text-align: center;
        border: 1px solid #2471a3;
        font-weight: 600;
    }}
    table.data-table td {{
        padding: 5px 8px;
        border: 1px solid #d5dbdb;
        text-align: center;
    }}
    table.data-table tr:nth-child(even) {{
        background-color: #f8f9fa;
    }}
    .image-container {{
        text-align: center;
        margin: 10px 0;
        page-break-inside: avoid;
    }}
    .image-container img {{
        max-width: 78%;
        height: auto;
        border: 1px solid #bdc3c7;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.08);
    }}
    .image-caption {{
        font-size: 7.8pt;
        color: #566573;
        margin-top: 4px;
        font-style: italic;
    }}
    .highlight-box {{
        background-color: #fef9e7;
        border-left: 3.5px solid #f39c12;
        padding: 8px 12px;
        margin: 8px 0;
        border-radius: 0 4px 4px 0;
        font-size: 8.8pt;
        page-break-inside: avoid;
    }}
    .success-box {{
        background-color: #eafaf1;
        border-left: 3.5px solid #2ecc71;
        padding: 8px 12px;
        margin: 8px 0;
        border-radius: 0 4px 4px 0;
        font-size: 8.8pt;
        page-break-inside: avoid;
    }}
    .page-break {{
        page-break-before: always;
    }}
    ul, ol {{
        margin-top: 3px;
        margin-bottom: 6px;
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 2px;
    }}
    .math {{
        font-family: 'Cambria Math', 'Times New Roman', serif;
        font-style: italic;
    }}
</style>
</head>
<body>

<!-- HEADER UTAMA -->
<div class="header-box">
    <h1>LAPORAN PRAKTIKUM & TUGAS CODING TRANSFORMASI GEOMETRI 2D</h1>
    <h2>Mata Kuliah: Grafika Komputer dan Pengolahan Citra (Pertemuan 2 / Minggu 3)</h2>
    <p>Topik: Representasi Objek 2D, Koordinat Homogen 3&times;3, Transformasi Affine, & Analisis Komposisi Urutan</p>
    <div class="rubrik-badge">
        <strong>Standar Rubrik:</strong> Demo (10%) | Rumus Matematis (25%) | Fungsi Modular (30%) | Visualisasi (15%) | Kualitas Kode (10%) | Analisis Ilmiah (10%)
    </div>
</div>

<!-- BAGIAN I: DASAR TEORI & FORMULASI MATEMATIS -->
<h2 class="section-title">1. Dasar Teori & Formulasi Matematis (Bobot Rumus 25%)</h2>
<p>
    Dalam grafika komputer 2D, objek dimodelkan sebagai himpunan titik sudut (vertex) dalam ruang euklidian &reals;<sup>2</sup>. Tiga transformasi geometri dasar meliputi perpindahan posisi (<strong>translasi</strong>), pemutaran orientasi (<strong>rotasi</strong>), dan pengubahan ukuran (<strong>scaling</strong>).
</p>

<h3 class="sub-title">A. Koordinat Homogen 2D</h3>
<p>
    Operasi translasi bersifat penambahan vektor (<span class="math">P' = P + T</span>), sedangkan rotasi dan skala merupakan perkalian matriks linear (<span class="math">P' = M &middot; P</span>). Agar seluruh transformasi affine ini dapat dinyatakan secara seragam sebagai operasi <strong>perkalian matriks tunggal terpadu</strong>, digunakan sistem <em>Koordinat Homogen 2D</em> dengan menambahkan komponen skalar <span class="math">w = 1</span>:
</p>
<div class="formula-box">
    Koordinat Kartesius: P = [x, y]ᵀ &nbsp;⟶&nbsp; Koordinat Homogen: P_h = [x, y, 1]ᵀ
</div>

<h3 class="sub-title">B. Matriks Transformasi Dasar 3&times;3 Terhadap Origin (0,0)</h3>
<ul>
    <li>
        <strong>Translasi sebesar (t<sub>x</sub>, t<sub>y</sub>):</strong>
        <div class="matrix-display">
            T(t<sub>x</sub>, t<sub>y</sub>) = <br>
            [ 1 &nbsp; 0 &nbsp; t<sub>x</sub> ]<br>
            [ 0 &nbsp; 1 &nbsp; t<sub>y</sub> ]<br>
            [ 0 &nbsp; 0 &nbsp;  1  ]
        </div>
        &nbsp;&DoubleRightArrow;&nbsp; x' = x + t<sub>x</sub> &nbsp;|&nbsp; y' = y + t<sub>y</sub>
    </li>
    <li>
        <strong>Rotasi sudut &theta; (Counter-Clockwise / Berlawanan Arah Jarum Jam) terhadap Origin:</strong>
        <div class="matrix-display">
            R(&theta;) = <br>
            [ cos(&theta;) &nbsp; -sin(&theta;) &nbsp; 0 ]<br>
            [ sin(&theta;) &nbsp; &nbsp;cos(&theta;) &nbsp; 0 ]<br>
            [   0     &nbsp; &nbsp;  0     &nbsp; 1 ]
        </div>
        &nbsp;&DoubleRightArrow;&nbsp; x' = x&middot;cos(&theta;) - y&middot;sin(&theta;) &nbsp;|&nbsp; y' = x&middot;sin(&theta;) + y&middot;cos(&theta;)
    </li>
    <li>
        <strong>Scaling faktor (s<sub>x</sub>, s<sub>y</sub>) terhadap Origin:</strong>
        <div class="matrix-display">
            S(s<sub>x</sub>, s<sub>y</sub>) = <br>
            [ s<sub>x</sub> &nbsp;  0  &nbsp; 0 ]<br>
            [  0  &nbsp; s<sub>y</sub> &nbsp; 0 ]<br>
            [  0  &nbsp;  0  &nbsp; 1 ]
        </div>
        &nbsp;&DoubleRightArrow;&nbsp; x' = x &middot; s<sub>x</sub> &nbsp;|&nbsp; y' = y &middot; s<sub>y</sub>
    </li>
</ul>

<h3 class="sub-title">C. Formulasi Transformasi Terhadap Titik Pusat Arbitrer (Pivot P<sub>p</sub>(p<sub>x</sub>, p<sub>y</sub>))</h3>
<p>
    Apabila rotasi atau scaling dilakukan terhadap sembarang titik pusat selain origin (0,0), operasi dilakukan melalui skema 3 langkah berturutan:
</p>
<ol>
    <li>Translasi objek ke titik origin: T(-p<sub>x</sub>, -p<sub>y</sub>)</li>
    <li>Transformasi dasar (Rotasi R(&theta;) atau Skala S(s<sub>x</sub>, s<sub>y</sub>)) di origin</li>
    <li>Translasi kembali objek ke posisi pivot semula: T(p<sub>x</sub>, p<sub>y</sub>)</li>
</ol>
<div class="formula-box">
    <strong>Matriks Rotasi terhadap Pivot P(p<sub>x</sub>, p<sub>y</sub>):</strong><br>
    M<sub>R, pivot</sub> = T(p<sub>x</sub>, p<sub>y</sub>) &middot; R(&theta;) &middot; T(-p<sub>x</sub>, -p<sub>y</sub>)<br>
    x' = (x - p<sub>x</sub>)&middot;cos(&theta;) - (y - p<sub>y</sub>)&middot;sin(&theta;) + p<sub>x</sub><br>
    y' = (x - p<sub>x</sub>)&middot;sin(&theta;) + (y - p<sub>y</sub>)&middot;cos(&theta;) + p<sub>y</sub><br><br>
    <strong>Matriks Scaling terhadap Pivot P(p<sub>x</sub>, p<sub>y</sub>):</strong><br>
    M<sub>S, pivot</sub> = T(p<sub>x</sub>, p<sub>y</sub>) &middot; S(s<sub>x</sub>, s<sub>y</sub>) &middot; T(-p<sub>x</sub>, -p<sub>y</sub>)<br>
    x' = (x - p<sub>x</sub>)&middot;s<sub>x</sub> + p<sub>x</sub><br>
    y' = (y - p<sub>y</sub>)&middot;s<sub>y</sub> + p<sub>y</sub>
</div>

<!-- BAGIAN II: IMPLEMENTASI FUNGSI MODULAR -->
<h2 class="section-title">2. Arsitektur Modul Fungsi (Bobot Fungsi 30% &amp; Kode 10%)</h2>
<p>
    Seluruh operasi diimplementasikan secara modular pada modul <code>transformasi_2d.py</code>. Modul ini mendukung input titik tunggal maupun matriks vertex berukuran (N, 2) melalui operasi vektorisasi NumPy (P<sub>h</sub> &middot; M<sup>T</sup>), sehingga sangat efisien dan bebas perulangan manual:
</p>
<ul>
    <li><code>to_homogeneous(points)</code>: Mengonversi koordinat kartesius 2D ke format homogen 3D dengan menambahkan kolom w=1.</li>
    <li><code>from_homogeneous(points_h)</code>: Melakukan pembagian komponen proyektif (x/w, y/w) dan mengembalikan koordinat 2D kartesius.</li>
    <li><code>matriks_translasi(tx, ty)</code>: Menghasilkan matriks translasi homogen 3&times;3.</li>
    <li><code>matriks_rotasi(theta_deg, px, py)</code>: Menghasilkan matriks rotasi terhadap sembarang titik pusat.</li>
    <li><code>matriks_scaling(sx, sy, px, py)</code>: Menghasilkan matriks scaling terhadap sembarang titik pusat.</li>
    <li><code>transform(points, matrix)</code>: Melakukan operasi perkalian matriks affine secara terpadu.</li>
    <li><code>hitung_pusat_massa(points)</code>: Menghitung titik centroid pusat poligon secara analitik: &Sigma; P<sub>i</sub> / N.</li>
</ul>

<div class="page-break"></div>

<!-- BAGIAN III: TUGAS 1 -->
<h2 class="section-title">3. Tugas 1: Rotasi Persegi 90&deg; Terhadap Titik Pusat (Bukan Origin)</h2>

<h3 class="sub-title">A. Spesifikasi Soal &amp; Perhitungan Manual</h3>
<p>
    Diberikan sebuah persegi dengan 4 titik sudut: A(0,0), B(1,0), C(1,1), D(0,1).<br>
    <strong>Langkah 1: Menentukan Titik Pusat Persegi (Centroid P<sub>c</sub>):</strong><br>
    p<sub>x</sub> = (0 + 1 + 1 + 0) / 4 = <strong>0.5</strong>, &nbsp;&nbsp;
    p<sub>y</sub> = (0 + 0 + 1 + 1) / 4 = <strong>0.5</strong> &nbsp;&DoubleRightArrow;&nbsp; <strong>P<sub>c</sub> = (0.5, 0.5)</strong>
</p>
<p>
    <strong>Langkah 2: Menghitung Aljabar Rotasi 90&deg; Terhadap P<sub>c</sub>(0.5, 0.5):</strong><br>
    Karena &theta; = 90&deg;, maka cos(90&deg;) = 0 dan sin(90&deg;) = 1.
</p>
<div class="formula-box">
    x' = (x - 0.5)&middot;cos(90&deg;) - (y - 0.5)&middot;sin(90&deg;) + 0.5 = -(y - 0.5) + 0.5 = <strong>1 - y</strong><br>
    y' = (x - 0.5)&middot;sin(90&deg;) + (y - 0.5)&middot;cos(90&deg;) + 0.5 =  (x - 0.5) + 0.5 = <strong>x</strong><br><br>
    Bentuk Matriks Homogen 3&times;3:<br>
    M<sub>rot</sub> = [ [ 0, -1,  1],<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1,  0,  0],<br>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0,  0,  1] ]
</div>

<h3 class="sub-title">B. Tabel Koordinat Vertex Sebelum &amp; Sesudah Transformasi</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Vertex</th>
            <th>Koordinat Awal (x, y)</th>
            <th>Perhitungan Aljabar Manual</th>
            <th>Koordinat Akhir (x', y')</th>
            <th>Keterangan Pergeseran Siklis</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>A</strong></td>
            <td>(0.0, 0.0)</td>
            <td>x' = 1 - 0 = 1; y' = 0</td>
            <td><strong>(1.0, 0.0)</strong></td>
            <td>Vertex A berpindah menempati posisi asal vertex B</td>
        </tr>
        <tr>
            <td><strong>B</strong></td>
            <td>(1.0, 0.0)</td>
            <td>x' = 1 - 0 = 1; y' = 1</td>
            <td><strong>(1.0, 1.0)</strong></td>
            <td>Vertex B berpindah menempati posisi asal vertex C</td>
        </tr>
        <tr>
            <td><strong>C</strong></td>
            <td>(1.0, 1.0)</td>
            <td>x' = 1 - 1 = 0; y' = 1</td>
            <td><strong>(0.0, 1.0)</strong></td>
            <td>Vertex C berpindah menempati posisi asal vertex D</td>
        </tr>
        <tr>
            <td><strong>D</strong></td>
            <td>(0.0, 1.0)</td>
            <td>x' = 1 - 1 = 0; y' = 0</td>
            <td><strong>(0.0, 0.0)</strong></td>
            <td>Vertex D berpindah menempati posisi asal vertex A</td>
        </tr>
        <tr style="background-color: #eafaf1; font-weight: bold;">
            <td>Pusat (Pivot)</td>
            <td>(0.5, 0.5)</td>
            <td>x' = 1 - 0.5 = 0.5; y' = 0.5</td>
            <td>(0.5, 0.5)</td>
            <td>Titik pusat bernilai tetap (Invarian)</td>
        </tr>
    </tbody>
</table>

<h3 class="sub-title">C. Tangkapan Grafik Visualisasi (Bobot Visual 15%)</h3>
<div class="image-container">
    <img src="{b64_t1}" alt="Grafik Tugas 1: Rotasi Persegi 90 Derajat terhadap Titik Pusat">
    <div class="image-caption">Gambar 1: Visualisasi Plot Tugas 1 &mdash; Persegi Awal (Biru), Hasil Rotasi 90&deg; (Merah Putus-putus), Titik Pusat (Bintang Hijau), dan Panah Rotasi Siklis.</div>
</div>

<h3 class="sub-title">D. Analisis Hasil Transformasi (Bobot Analisis 10%)</h3>
<div class="highlight-box">
    <strong>Wawasan Geometris Kunci:</strong><br>
    1. <strong>Invarian Bentuk Spasial (Spatial Invariance):</strong> Persegi memiliki simetri rotasi lipat-4 (C<sub>4</sub>). Oleh karena itu, rotasi 90&deg; terhadap titik pusat massanya (0.5, 0.5) menghasilkan area spasial yang tepat bertumpuk dengan bidang asalnya.<br>
    2. <strong>Perpindahan Siklis Indeks Vertex:</strong> Meskipun siluet luarnya tampak identik, identitas setiap titik sudut bergeser 90&deg; secara siklis: <strong>A &rarr; B &rarr; C &rarr; D &rarr; A</strong>.<br>
    3. <strong>Perbedaan Mendasar dengan Rotasi Origin (0,0):</strong> Jika rotasi 90&deg; dilakukan terhadap origin (0,0), seluruh persegi akan terlempar ke kuadran II [ (0,0), (0,1), (-1,1), (-1,0) ]. Translasi ke origin lalu rotasi dan translasi balik ke (0.5, 0.5) adalah kunci keberhasilan rotasi di tempat (<em>in-place rotation</em>).
</div>

<div class="page-break"></div>

<!-- BAGIAN IV: TUGAS 2 -->
<h2 class="section-title">4. Tugas 2: Simulator Transformasi Geometri 2D Sederhana</h2>

<h3 class="sub-title">A. Spesifikasi &amp; Desain Poligon</h3>
<p>
    Tugas 2 mengimplementasikan simulator 2D interaktif dengan poligon beranggotakan <strong>5 vertex</strong>. Dipilih poligon asimetris agar orientasi perputaran dan deformasi skala terlihat jelas tanpa distorsi simetri:<br>
    <strong>V<sub>1</sub>(1.0, 1.0), &nbsp; V<sub>2</sub>(4.0, 1.0), &nbsp; V<sub>3</sub>(5.0, 3.0), &nbsp; V<sub>4</sub>(3.0, 5.0), &nbsp; V<sub>5</sub>(1.0, 3.5)</strong><br>
    Titik Pusat Massa (Centroid) terhitung secara otomatis:<br>
    <strong>P<sub>centroid</sub> = ((1+4+5+3+1)/5, (1+1+3+5+3.5)/5) = (2.80, 2.70)</strong>
</p>

<h3 class="sub-title">B. Parameter Masukan Pengguna &amp; Formulasi Matriks Komposit</h3>
<p>Program menerima input parameter dari pengguna melalui prompt interaktif CLI (dengan fallback default otomatis):</p>
<ul>
    <li>Translasi: t<sub>x</sub> = 4.00, &nbsp; t<sub>y</sub> = 2.50</li>
    <li>Sudut Rotasi: &theta; = 45.00&deg; (Counter-Clockwise)</li>
    <li>Faktor Skala: s<sub>x</sub> = 1.50, &nbsp; s<sub>y</sub> = 1.20</li>
    <li>Titik Pusat (Pivot): P<sub>c</sub>(2.80, 2.70) (Centroid)</li>
</ul>
<p>Matriks komposit gabungan dihitung sebagai:</p>
<div class="formula-box">
    M<sub>total</sub> = T(t<sub>x</sub>, t<sub>y</sub>) &middot; M<sub>R</sub>(&theta;, p<sub>x</sub>, p<sub>y</sub>) &middot; M<sub>S</sub>(s<sub>x</sub>, s<sub>y</sub>, p<sub>x</sub>, p<sub>y</sub>)<br><br>
    M<sub>total</sub> = <br>
    [  1.0607 &nbsp; -0.8485 &nbsp;  6.1212 ]<br>
    [  1.0607 &nbsp;  0.8485 &nbsp; -0.0609 ]<br>
    [  0.0000 &nbsp;  0.0000 &nbsp;  1.0000 ]
</div>

<h3 class="sub-title">C. Tabel Koordinat Hasil Transformasi Poligon 5 Vertex</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Vertex</th>
            <th>Koordinat Asli (x, y)</th>
            <th>Koordinat Hasil Transformasi (x', y')</th>
            <th>Analisis Perubahan Geometris</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>V1</strong></td>
            <td>(1.00, 1.00)</td>
            <td><strong>(6.33, 1.85)</strong></td>
            <td>Mengalami peregangan, rotasi 45&deg;, dan pergeseran ke kanan</td>
        </tr>
        <tr>
            <td><strong>V2</strong></td>
            <td>(4.00, 1.00)</td>
            <td><strong>(9.52, 5.03)</strong></td>
            <td>Titik terjauh horizontal bergeser hingga mendekati x=10</td>
        </tr>
        <tr>
            <td><strong>V3</strong></td>
            <td>(5.00, 3.00)</td>
            <td><strong>(8.88, 7.79)</strong></td>
            <td>Puncak samping kanan terotasi ke kuadran atas</td>
        </tr>
        <tr>
            <td><strong>V4</strong></td>
            <td>(3.00, 5.00)</td>
            <td><strong>(5.06, 7.36)</strong></td>
            <td>Puncak tertinggi terotasi 45&deg; CCW</td>
        </tr>
        <tr>
            <td><strong>V5</strong></td>
            <td>(1.00, 3.50)</td>
            <td><strong>(4.21, 3.97)</strong></td>
            <td>Sisi kiri objek tetap proporsional</td>
        </tr>
        <tr style="background-color: #fcf3cf; font-weight: bold;">
            <td>Pivot Point</td>
            <td>(2.80, 2.70)</td>
            <td><strong>(6.80, 5.20)</strong></td>
            <td>Berpindah sejauh vektor translasi (+4.0, +2.5)</td>
        </tr>
    </tbody>
</table>

<h3 class="sub-title">D. Tangkapan Grafik Visualisasi Simulator</h3>
<div class="image-container">
    <img src="{b64_t2}" alt="Grafik Tugas 2: Simulator Transformasi 2D">
    <div class="image-caption">Gambar 2: Visualisasi Simulator 2D &mdash; Poligon Asli (Biru), Hasil Transformasi (Oranye), Titik Pivot Awal &amp; Akhir (Bintang Hijau &amp; Merah), Vektor Translasi Pivot, Label Vertex, dan Grid Koordinat.</div>
</div>

<div class="page-break"></div>

<!-- BAGIAN V: TUGAS 3 -->
<h2 class="section-title">5. Tugas 3: Analisis Perbandingan Urutan Transformasi (Bobot Analisis 10%)</h2>

<h3 class="sub-title">A. Deskripsi Permasalahan</h3>
<p>
    Tugas ini membandingkan dua sekuens transformasi yang berbeda pada satu titik vertex <strong>V(2.0, 3.0)</strong>:
</p>
<ul>
    <li><strong>Urutan 1: Translasi &rarr; Rotasi &rarr; Scaling (T &rarr; R &rarr; S)</strong></li>
    <li><strong>Urutan 2: Scaling &rarr; Rotasi &rarr; Translasi (S &rarr; R &rarr; T)</strong></li>
</ul>
<p>
    Parameter pengujian: Translasi T(t<sub>x</sub>=4.0, t<sub>y</sub>=2.0), Rotasi R(&theta;=90&deg; CCW), Scaling S(s<sub>x</sub>=2.0, s<sub>y</sub>=3.0).
</p>

<h3 class="sub-title">B. Perhitungan Numerik Langkah Demi Langkah pada Vertex V(2, 3)</h3>
<table class="data-table">
    <thead>
        <tr>
            <th>Tahapan Transformasi</th>
            <th>Urutan 1: Translasi &rarr; Rotasi &rarr; Scaling</th>
            <th>Urutan 2: Scaling &rarr; Rotasi &rarr; Translasi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><strong>0. Titik Asal V</strong></td>
            <td><strong>(2.00, 3.00)</strong></td>
            <td><strong>(2.00, 3.00)</strong></td>
        </tr>
        <tr>
            <td><strong>1. Transformasi Pertama</strong></td>
            <td>
                <em>Translasi (+4, +2):</em><br>
                x<sub>1</sub> = 2 + 4 = 6<br>
                y<sub>1</sub> = 3 + 2 = 5<br>
                <strong>V<sub>1</sub> = (6.00, 5.00)</strong>
            </td>
            <td>
                <em>Scaling (2&times;, 3&times;):</em><br>
                x<sub>1</sub> = 2 &times; 2 = 4<br>
                y<sub>1</sub> = 3 &times; 3 = 9<br>
                <strong>W<sub>1</sub> = (4.00, 9.00)</strong>
            </td>
        </tr>
        <tr>
            <td><strong>2. Transformasi Kedua</strong></td>
            <td>
                <em>Rotasi 90&deg; terhadap origin:</em><br>
                x<sub>2</sub> = 6&middot;cos(90&deg;) - 5&middot;sin(90&deg;) = -5<br>
                y<sub>2</sub> = 6&middot;sin(90&deg;) + 5&middot;cos(90&deg;) = 6<br>
                <strong>V<sub>2</sub> = (-5.00, 6.00)</strong>
            </td>
            <td>
                <em>Rotasi 90&deg; terhadap origin:</em><br>
                x<sub>2</sub> = 4&middot;cos(90&deg;) - 9&middot;sin(90&deg;) = -9<br>
                y<sub>2</sub> = 4&middot;sin(90&deg;) + 9&middot;cos(90&deg;) = 4<br>
                <strong>W<sub>2</sub> = (-9.00, 4.00)</strong>
            </td>
        </tr>
        <tr>
            <td><strong>3. Transformasi Ketiga</strong></td>
            <td>
                <em>Scaling (2&times;, 3&times;):</em><br>
                x<sub>3</sub> = -5 &times; 2 = -10<br>
                y<sub>3</sub> = 6 &times; 3 = 18<br>
                <strong>V<sub>TRS</sub>' = (-10.00, 18.00)</strong>
            </td>
            <td>
                <em>Translasi (+4, +2):</em><br>
                x<sub>3</sub> = -9 + 4 = -5<br>
                y<sub>3</sub> = 4 + 2 = 6<br>
                <strong>W<sub>SRT</sub>' = (-5.00, 6.00)</strong>
            </td>
        </tr>
        <tr style="background-color: #fcf3cf; font-weight: bold; font-size: 8.8pt;">
            <td>HASIL AKHIR</td>
            <td>V<sub>TRS</sub>' = (-10.00, 18.00)</td>
            <td>W<sub>SRT</sub>' = (-5.00, 6.00)</td>
        </tr>
    </tbody>
</table>

<div class="highlight-box">
    <strong>Selisih Spasial Kedua Hasil Transformasi:</strong><br>
    &Delta;x = |-10 - (-5)| = 5.00, &nbsp;&nbsp; &Delta;y = |18 - 6| = 12.00<br>
    <strong>Jarak Euclidean (Selisih)</strong> = &radic;(5<sup>2</sup> + 12<sup>2</sup>) = &radic;(25 + 144) = <strong>13.0000 satuan</strong>
</div>

<h3 class="sub-title">C. Pembuktian Aljabar Matriks Komposit 3&times;3</h3>
<p>
    Secara formal, perkalian matriks untuk koordinat vektor kolom P' = M &middot; P:
</p>
<div class="formula-box">
    <strong>Matriks Komposit Urutan 1 (M<sub>TRS</sub> = S &middot; R &middot; T):</strong><br>
    M<sub>TRS</sub> = <br>
    [  0.0 &nbsp; -2.0 &nbsp; -4.0 ]<br>
    [  3.0 &nbsp; &nbsp;0.0 &nbsp; 12.0 ]<br>
    [  0.0 &nbsp; &nbsp;0.0 &nbsp; &nbsp;1.0 ]<br><br>
    <strong>Matriks Komposit Urutan 2 (M<sub>SRT</sub> = T &middot; R &middot; S):</strong><br>
    M<sub>SRT</sub> = <br>
    [  0.0 &nbsp; -3.0 &nbsp;  4.0 ]<br>
    [  2.0 &nbsp; &nbsp;0.0 &nbsp;  2.0 ]<br>
    [  0.0 &nbsp; &nbsp;0.0 &nbsp;  1.0 ]
</div>
<p>
    Tampak jelas bahwa <strong>M<sub>TRS</sub> &ne; M<sub>SRT</sub></strong>. Baik elemen matriks rotasi-skala maupun vektor kolom translasi memiliki nilai yang sama sekali berbeda.
</p>

<h3 class="sub-title">D. Tangkapan Grafik Perbandingan Urutan Transformasi</h3>
<div class="image-container">
    <img src="{b64_t3}" alt="Grafik Tugas 3: Perbandingan Urutan Transformasi">
    <div class="image-caption">Gambar 3: Visualisasi Tugas 3 &mdash; Perbandingan Lintasan Langkah Demi Langkah Vertex V(2,3) serta Poligon Referensi untuk Urutan 1 (Kiri) dan Urutan 2 (Kanan).</div>
</div>

<h3 class="sub-title">E. Pembahasan Ilmiah: Mengapa Kedua Urutan Menghasilkan Nilai Berbeda?</h3>
<div class="success-box">
    <strong>Jawaban Soal Tugas 3:</strong><br>
    <strong>TIDAK SAMA.</strong> Hasil akhir kedua urutan transformasi tersebut menghasilkan posisi koordinat, orientasi, dan ukuran spasial yang sama sekali berbeda.<br><br>
    <strong>Penjelasan Berdasarkan Konsep Transformasi Geometris &amp; Aljabar Linier:</strong>
    <ol>
        <li>
            <strong>Sifat Non-Komutatif Perkalian Matriks:</strong><br>
            Transformasi affine 2D diwakili oleh matriks linier. Perkalian matriks pada umumnya <em>tidak bersifat komutatif</em> (A &middot; B &ne; B &middot; A). Oleh karena itu:
            <strong>S &middot; R &middot; T &ne; T &middot; R &middot; S</strong>.
        </li>
        <li>
            <strong>Amplifikasi Translasi oleh Rotasi &amp; Skala (Urutan 1: T &rarr; R &rarr; S):</strong><br>
            Ketika translasi (t<sub>x</sub>, t<sub>y</sub>) dilakukan di awal, titik dijauhkan dari origin. Ketika rotasi dan scaling diterapkan setelahnya, vektor translasi (t<sub>x</sub>, t<sub>y</sub>) <em>ikut terputar sejauh &theta; dan dilipatgandakan oleh faktor skala (s<sub>x</sub>, s<sub>y</sub>)</em>:
            <br>
            &Delta;x<sub>eff</sub> = s<sub>x</sub>(t<sub>x</sub> cos&theta; - t<sub>y</sub> sin&theta;) = 2 &middot; (4 &middot; 0 - 2 &middot; 1) = <strong>-4.0</strong><br>
            &Delta;y<sub>eff</sub> = s<sub>y</sub>(t<sub>x</sub> sin&theta; + t<sub>y</sub> cos&theta;) = 3 &middot; (4 &middot; 1 + 2 &middot; 0) = <strong>+12.0</strong>
        </li>
        <li>
            <strong>Translasi Murni Bebas Amplifikasi (Urutan 2: S &rarr; R &rarr; T):</strong><br>
            Sebaliknya, pada Urutan 2, titik diskalakan dan dirotasi terlebih dahulu di sekeliling origin. Translasi (t<sub>x</sub>, t<sub>y</sub>) baru diterapkan pada tahap paling akhir sebagai pergeseran linier murni:
            <br>
            &Delta;x<sub>eff</sub> = t<sub>x</sub> = <strong>+4.0</strong>, &nbsp;&nbsp;
            &Delta;y<sub>eff</sub> = t<sub>y</sub> = <strong>+2.0</strong>.<br>
            Pergeseran ini sama sekali tidak dipengaruhi oleh nilai rotasi maupun faktor skala.
        </li>
    </ol>
</div>

<!-- BAGIAN VI: KESIMPULAN -->
<div style="page-break-inside: avoid; margin-top: 15px;">
<h2 class="section-title">6. Kesimpulan Akhir</h2>
<ol>
    <li>
        <strong>Representasi Homogen 3&times;3:</strong> Menjadi standar industri grafika komputer karena menyatukan operasi linear (rotasi, scaling) dan affine (translasi) ke dalam satu aljabar perkalian matriks yang kompak.
    </li>
    <li>
        <strong>Pusat Rotasi (Tugas 1):</strong> Titik pivot bukan origin mutlak memerlukan prosedur 3 tahap (T(p) &middot; R &middot; T(-p)). Rotasi 90&deg; pada persegi berpusat (0.5, 0.5) membuktikan sifat invarian spasial bentuk namun mengalami pergeseran siklis pada vertex.
    </li>
    <li>
        <strong>Simulator 2D (Tugas 2):</strong> Mampu memodelkan poligon sembarang secara parametrik dan presisi dengan menggabungkan pergeseran pivot dan transformasi multi-langkah.
    </li>
    <li>
        <strong>Sensitivitas Urutan (Tugas 3):</strong> Urutan transformasi memegang peranan krusial dalam grafika komputer (seperti pada <em>Scene Graph</em> dan <em>Hierarchical Modeling</em>). Transformasi skala dan rotasi yang mendahului translasi (Local-to-World space) adalah pola standar untuk mempertahankan ukuran dan bentuk objek sebelum ditempatkan pada posisi ruang global.
    </li>
</ol>
</div>

</body>
</html>
"""
    with open(HTML_OUT, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[INFO] File HTML Laporan berhasil diperbarui di: {HTML_OUT}")
    return HTML_OUT


def compile_pdf():
    build_html()
    print("[INFO] Mengompilasi dokumen HTML ke PDF menggunakan Headless Google Chrome...")
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    cmd = [
        chrome_path,
        "--headless=new",
        "--disable-gpu",
        "--no-pdf-header-footer",
        f"--print-to-pdf={PDF_OUT}",
        HTML_OUT
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0 and os.path.exists(PDF_OUT):
        size_kb = os.path.getsize(PDF_OUT) / 1024
        print(f"[SUCCESS] PDF Laporan berhasil dibuat: {PDF_OUT} ({size_kb:.1f} KB)")
        return True
    else:
        print(f"[ERROR] Gagal membuat PDF: {res.stderr}")
        return False


if __name__ == "__main__":
    compile_pdf()
