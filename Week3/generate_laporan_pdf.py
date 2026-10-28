"""
Script untuk menyusun dokumen laporan akademik lengkap dalam format HTML + CSS
dan mengompilasinya menjadi PDF berstandar publikasi akademik formal:
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
        margin: 1.6cm 1.5cm 1.6cm 1.5cm;
    }}
    * {{
        box-sizing: border-box;
    }}
    body {{
        font-family: 'Times New Roman', Times, 'Cambria', Georgia, serif;
        color: #000000;
        line-height: 1.4;
        font-size: 9.8pt;
        background-color: #ffffff;
        margin: 0;
        padding: 0;
    }}

    /* Header & Biodata */
    .header-box {{
        text-align: center;
        margin-bottom: 8px;
        padding-bottom: 2px;
    }}
    .header-box h1 {{
        margin: 0 0 3px 0;
        font-size: 13pt;
        font-weight: bold;
        color: #000000;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }}
    .header-box h2 {{
        margin: 0 0 3px 0;
        font-size: 10.5pt;
        font-weight: bold;
        color: #000000;
        text-transform: uppercase;
    }}
    .header-box p.topik-sub {{
        margin: 0 0 6px 0;
        font-size: 9pt;
        color: #000000;
        font-style: italic;
    }}
    .header-divider {{
        border-top: 1.5px solid #000000;
        border-bottom: 0.5px solid #000000;
        height: 2px;
        margin: 5px 0 8px 0;
    }}

    table.biodata-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 3px 0 6px 0;
        font-size: 9.2pt;
        color: #000000;
    }}
    table.biodata-table td {{
        padding: 2px 2px;
        border: none;
        vertical-align: top;
    }}
    table.biodata-table td.bio-label {{
        font-weight: bold;
        width: 15%;
    }}
    table.biodata-table td.bio-sep {{
        width: 2%;
        text-align: center;
    }}
    table.biodata-table td.bio-val {{
        width: 33%;
    }}

    /* Section & Sub-titles */
    h2.section-title {{
        color: #000000;
        font-size: 10.8pt;
        font-weight: bold;
        border-bottom: 1.2px solid #000000;
        padding-bottom: 2px;
        margin-top: 12px;
        margin-bottom: 6px;
        text-transform: uppercase;
        page-break-after: avoid;
    }}
    h3.sub-title {{
        color: #000000;
        font-size: 9.8pt;
        font-weight: bold;
        margin-top: 8px;
        margin-bottom: 3px;
        page-break-after: avoid;
    }}
    p, li {{
        text-align: justify;
        color: #000000;
        margin-top: 3px;
        margin-bottom: 3px;
    }}
    ul, ol {{
        margin-top: 2px;
        margin-bottom: 5px;
        padding-left: 20px;
    }}
    li {{
        margin-bottom: 2px;
    }}

    /* Formulas & Mathematics - Consistent Pure Black */
    .formula-box {{
        background-color: #ffffff;
        border: 1px solid #333333;
        padding: 6px 10px;
        margin: 6px 0;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 8.8pt;
        color: #000000;
        line-height: 1.35;
        page-break-inside: avoid;
    }}
    .matrix-display {{
        display: inline-block;
        vertical-align: middle;
        margin: 2px 0;
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 8.2pt;
        color: #000000;
        background: #ffffff;
        padding: 3px 5px;
        border: 1px solid #444444;
        line-height: 1.3;
    }}
    .math {{
        font-family: 'Cambria Math', 'Times New Roman', serif;
        font-style: italic;
        color: #000000;
    }}
    code {{
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 8.5pt;
        color: #000000;
        background: #f5f5f5;
        padding: 1px 3px;
        border: 1px solid #cccccc;
        border-radius: 2px;
    }}

    /* Academic Tables - Clean Booktabs Style (No AI Slop) */
    .table-caption {{
        font-size: 8.8pt;
        font-weight: bold;
        color: #000000;
        margin-top: 6px;
        margin-bottom: 3px;
        text-align: left;
    }}
    table.academic-table {{
        width: 100%;
        border-collapse: collapse;
        margin: 4px 0 10px 0;
        font-size: 8.5pt;
        color: #000000;
        page-break-inside: avoid;
        border-top: 1.6px solid #000000;
        border-bottom: 1.6px solid #000000;
    }}
    table.academic-table th {{
        background-color: #ffffff;
        color: #000000;
        padding: 5px 6px;
        text-align: center;
        border-top: 1.6px solid #000000;
        border-bottom: 1.1px solid #000000;
        border-left: none;
        border-right: none;
        font-weight: bold;
    }}
    table.academic-table td {{
        padding: 4px 6px;
        border: none;
        border-bottom: 0.5px solid #dcdcdc;
        color: #000000;
        vertical-align: middle;
    }}
    table.academic-table tr.row-summary td {{
        border-top: 1.1px solid #000000;
        border-bottom: 1.6px solid #000000;
        font-weight: bold;
        background-color: #ffffff;
    }}
    .text-center {{
        text-align: center !important;
    }}
    .text-left {{
        text-align: left !important;
    }}
    .text-right {{
        text-align: right !important;
    }}
    .font-bold {{
        font-weight: bold !important;
    }}

    /* Images */
    .image-container {{
        text-align: center;
        margin: 8px 0;
        page-break-inside: avoid;
    }}
    .image-container img {{
        max-width: 76%;
        max-height: 360px;
        height: auto;
        border: 1px solid #333333;
    }}
    .image-caption {{
        font-size: 8.2pt;
        color: #000000;
        margin-top: 4px;
        font-style: italic;
    }}

    /* Academic Discussion & Notes */
    .academic-box {{
        background-color: #ffffff;
        border-left: 2.5px solid #000000;
        padding: 6px 10px;
        margin: 6px 0;
        font-size: 8.8pt;
        color: #000000;
        page-break-inside: avoid;
    }}

    /* Page Breaks */
    .page-break {{
        page-break-before: always;
    }}
</style>
</head>
<body>

<!-- ==================== HALAMAN 1: IDENTITAS & DASAR TEORI ==================== -->
<div class="header-box">
    <h1>LAPORAN PRAKTIKUM GRAFIKA KOMPUTER</h1>
    <h2>TRANSFORMASI GEOMETRI 2D</h2>
    <p class="topik-sub">Representasi Objek 2D, Koordinat Homogen 3&times;3, &amp; Analisis Komposisi Transformasi Affine</p>
    <div class="header-divider"></div>

    <table class="biodata-table">
        <tr>
            <td class="bio-label">Nama</td>
            <td class="bio-sep">:</td>
            <td class="bio-val"><strong>Nuruddin Rusydi Ilham</strong></td>
            <td class="bio-label">Mata Kuliah</td>
            <td class="bio-sep">:</td>
            <td class="bio-val">Grafika Komputer dan Pengolahan Citra</td>
        </tr>
        <tr>
            <td class="bio-label">NIM</td>
            <td class="bio-sep">:</td>
            <td class="bio-val"><strong>3012410055</strong></td>
            <td class="bio-label">Topik Praktikum</td>
            <td class="bio-sep">:</td>
            <td class="bio-val">Transformasi Geometri 2D (Minggu 3)</td>
        </tr>
    </table>
    <div class="header-divider"></div>
</div>

<h2 class="section-title">1. Dasar Teori &amp; Formulasi Matematis</h2>
<p>
    Dalam grafika komputer 2D, objek dimodelkan sebagai himpunan titik sudut (vertex) dalam ruang euklidian &reals;<sup>2</sup>. Tiga transformasi geometri dasar meliputi perpindahan posisi (<strong>translasi</strong>), pemutaran orientasi (<strong>rotasi</strong>), dan pengubahan ukuran (<strong>scaling</strong>).
</p>

<h3 class="sub-title">A. Koordinat Homogen 2D</h3>
<p>
    Operasi translasi secara matematis bersifat penambahan vektor (<span class="math">P' = P + T</span>), sedangkan rotasi dan skala merupakan perkalian matriks linear (<span class="math">P' = M &middot; P</span>). Agar seluruh transformasi affine ini dapat dinyatakan secara seragam sebagai operasi <strong>perkalian matriks tunggal terpadu</strong>, digunakan sistem <em>Koordinat Homogen 2D</em> dengan menambahkan komponen skalar <span class="math">w = 1</span>:
</p>
<div class="formula-box">
    Koordinat Kartesius: P = [x, y]ᵀ &nbsp;&nbsp;&longrightarrow;&nbsp;&nbsp; Koordinat Homogen: P_h = [x, y, 1]ᵀ
</div>

<h3 class="sub-title">B. Matriks Transformasi Dasar 3&times;3 Terhadap Origin (0,0)</h3>
<table style="width: 100%; border-collapse: collapse; margin: 4px 0; font-size: 8.8pt;">
    <tr>
        <td style="width: 50%; vertical-align: top; padding: 2px 4px 2px 0;">
            <strong>1. Translasi sebesar (t<sub>x</sub>, t<sub>y</sub>):</strong><br>
            <div class="matrix-display">
                T(t<sub>x</sub>, t<sub>y</sub>) = <br>
                [ 1 &nbsp; 0 &nbsp; t<sub>x</sub> ]<br>
                [ 0 &nbsp; 1 &nbsp; t<sub>y</sub> ]<br>
                [ 0 &nbsp; 0 &nbsp; &nbsp;1 &nbsp;]
            </div><br>
            x' = x + t<sub>x</sub> &nbsp;|&nbsp; y' = y + t<sub>y</sub>
        </td>
        <td style="width: 50%; vertical-align: top; padding: 2px 0 2px 4px;">
            <strong>2. Scaling faktor (s<sub>x</sub>, s<sub>y</sub>):</strong><br>
            <div class="matrix-display">
                S(s<sub>x</sub>, s<sub>y</sub>) = <br>
                [ s<sub>x</sub> &nbsp; 0 &nbsp; 0 ]<br>
                [ &nbsp;0 &nbsp; s<sub>y</sub> &nbsp; 0 ]<br>
                [ &nbsp;0 &nbsp; 0 &nbsp; &nbsp;1 ]
            </div><br>
            x' = x &middot; s<sub>x</sub> &nbsp;|&nbsp; y' = y &middot; s<sub>y</sub>
        </td>
    </tr>
    <tr>
        <td colspan="2" style="padding-top: 4px;">
            <strong>3. Rotasi sudut &theta; (Counter-Clockwise / CCW) terhadap Origin:</strong><br>
            <div class="matrix-display">
                R(&theta;) = <br>
                [ cos(&theta;) &nbsp; -sin(&theta;) &nbsp; 0 ]<br>
                [ sin(&theta;) &nbsp; &nbsp;cos(&theta;) &nbsp; 0 ]<br>
                [ &nbsp; 0 &nbsp; &nbsp; &nbsp; &nbsp; 0 &nbsp; &nbsp; &nbsp; 1 ]
            </div>
            &nbsp;&implies;&nbsp; x' = x&middot;cos(&theta;) - y&middot;sin(&theta;), &nbsp; y' = x&middot;sin(&theta;) + y&middot;cos(&theta;)
        </td>
    </tr>
</table>

<h3 class="sub-title">C. Formulasi Transformasi Terhadap Titik Pusat Arbitrer (Pivot P<sub>p</sub>(p<sub>x</sub>, p<sub>y</sub>))</h3>
<p>
    Apabila rotasi atau scaling dilakukan terhadap titik acuan selain origin (0,0), operasi dilakukan melalui 3 tahap sekuensial: (1) Translasi objek ke origin: T(-p<sub>x</sub>, -p<sub>y</sub>), (2) Transformasi dasar di origin (Rotasi R(&theta;) atau Skala S(s<sub>x</sub>, s<sub>y</sub>)), dan (3) Translasi kembali ke posisi pivot: T(p<sub>x</sub>, p<sub>y</sub>).
</p>
<div class="formula-box">
    <strong>Matriks Rotasi Pivot:</strong> M<sub>R, pivot</sub> = T(p<sub>x</sub>, p<sub>y</sub>) &middot; R(&theta;) &middot; T(-p<sub>x</sub>, -p<sub>y</sub>)<br>
    x' = (x - p<sub>x</sub>)&middot;cos(&theta;) - (y - p<sub>y</sub>)&middot;sin(&theta;) + p<sub>x</sub> &nbsp;|&nbsp; y' = (x - p<sub>x</sub>)&middot;sin(&theta;) + (y - p<sub>y</sub>)&middot;cos(&theta;) + p<sub>y</sub><br>
    <strong>Matriks Scaling Pivot:</strong> M<sub>S, pivot</sub> = T(p<sub>x</sub>, p<sub>y</sub>) &middot; S(s<sub>x</sub>, s<sub>y</sub>) &middot; T(-p<sub>x</sub>, -p<sub>y</sub>)<br>
    x' = (x - p<sub>x</sub>)&middot;s<sub>x</sub> + p<sub>x</sub> &nbsp;|&nbsp; y' = (y - p<sub>y</sub>)&middot;s<sub>y</sub> + p<sub>y</sub>
</div>

<!-- ==================== HALAMAN 2: ARSITEKTUR KODE & TUGAS 1 SPESIFIKASI ==================== -->
<div class="page-break"></div>

<h2 class="section-title">2. Arsitektur Modul Fungsi (transformasi_2d.py)</h2>
<p>
    Seluruh operasi transformasi diimplementasikan secara terstruktur dan modular pada file <code>transformasi_2d.py</code>. Modul ini mendukung pemrosesan titik tunggal maupun matriks vertex berukuran (N, 2) melalui operasi vektorisasi NumPy (P<sub>h</sub> &middot; M<sup>T</sup>), sehingga komputasi berjalan deterministik dan efisien:
</p>
<ul>
    <li><code>to_homogeneous(points)</code> &amp; <code>from_homogeneous(points_h)</code>: Konversi koordinat kartesius 2D &harr; homogen 3D dengan normalisasi komponen proyektif w.</li>
    <li><code>matriks_translasi(tx, ty)</code>, <code>matriks_rotasi(theta_deg, px, py)</code>, <code>matriks_scaling(sx, sy, px, py)</code>: Pembangun matriks transformasi affine homogen 3&times;3 terhadap titik acuan arbitrer.</li>
    <li><code>transform(points, matrix)</code> &amp; <code>hitung_pusat_massa(points)</code>: Eksekutor perkalian matriks affine terpadu serta kalkulasi titik centroid analitik (&Sigma; P<sub>i</sub> / N).</li>
</ul>

<h2 class="section-title">3. Tugas 1: Rotasi Persegi 90&deg; Terhadap Titik Pusat</h2>

<h3 class="sub-title">A. Spesifikasi Soal &amp; Perhitungan Aljabar Manual</h3>
<p>
    Diberikan sebuah persegi dengan 4 titik sudut awal: A(0,0), B(1,0), C(1,1), dan D(0,1).<br>
    <strong>Langkah 1: Menentukan Titik Pusat Persegi (Centroid P<sub>c</sub>):</strong><br>
    p<sub>x</sub> = (0 + 1 + 1 + 0) / 4 = <strong>0.5</strong>, &nbsp;&nbsp;
    p<sub>y</sub> = (0 + 0 + 1 + 1) / 4 = <strong>0.5</strong> &nbsp;&implies;&nbsp; <strong>P<sub>c</sub> = (0.5, 0.5)</strong>
</p>
<p>
    <strong>Langkah 2: Menghitung Aljabar Rotasi 90&deg; Terhadap P<sub>c</sub>(0.5, 0.5):</strong><br>
    Dengan &theta; = 90&deg;, maka cos(90&deg;) = 0 dan sin(90&deg;) = 1.
</p>
<div class="formula-box">
    x' = (x - 0.5)&middot;cos(90&deg;) - (y - 0.5)&middot;sin(90&deg;) + 0.5 = -(y - 0.5) + 0.5 = <strong>1 - y</strong><br>
    y' = (x - 0.5)&middot;sin(90&deg;) + (y - 0.5)&middot;cos(90&deg;) + 0.5 = &nbsp;(x - 0.5) + 0.5 = <strong>x</strong><br><br>
    Bentuk Matriks Homogen 3&times;3:<br>
    M<sub>rot</sub> = <br>
    [ &nbsp;0 &nbsp; -1 &nbsp; 1 ]<br>
    [ &nbsp;1 &nbsp; &nbsp;0 &nbsp; 0 ]<br>
    [ &nbsp;0 &nbsp; &nbsp;0 &nbsp; 1 ]
</div>

<h3 class="sub-title">B. Tabel Koordinat Vertex Sebelum &amp; Sesudah Transformasi</h3>
<div class="table-caption">Tabel 1. Koordinat Vertex Persegi Sebelum dan Sesudah Rotasi 90&deg; terhadap Titik Pusat</div>
<table class="academic-table">
    <thead>
        <tr>
            <th style="width: 14%;">Vertex</th>
            <th style="width: 20%;">Koordinat Awal (x, y)</th>
            <th style="width: 28%;">Perhitungan Aljabar Manual</th>
            <th style="width: 18%;">Koordinat Akhir (x', y')</th>
            <th style="width: 20%;">Keterangan Pergeseran</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="text-center font-bold">A</td>
            <td class="text-center">(0.0, 0.0)</td>
            <td class="text-center">x' = 1 - 0 = 1; &nbsp; y' = 0</td>
            <td class="text-center font-bold">(1.0, 0.0)</td>
            <td class="text-left">Menempati posisi awal vertex B</td>
        </tr>
        <tr>
            <td class="text-center font-bold">B</td>
            <td class="text-center">(1.0, 0.0)</td>
            <td class="text-center">x' = 1 - 0 = 1; &nbsp; y' = 1</td>
            <td class="text-center font-bold">(1.0, 1.0)</td>
            <td class="text-left">Menempati posisi awal vertex C</td>
        </tr>
        <tr>
            <td class="text-center font-bold">C</td>
            <td class="text-center">(1.0, 1.0)</td>
            <td class="text-center">x' = 1 - 1 = 0; &nbsp; y' = 1</td>
            <td class="text-center font-bold">(0.0, 1.0)</td>
            <td class="text-left">Menempati posisi awal vertex D</td>
        </tr>
        <tr>
            <td class="text-center font-bold">D</td>
            <td class="text-center">(0.0, 1.0)</td>
            <td class="text-center">x' = 1 - 1 = 0; &nbsp; y' = 0</td>
            <td class="text-center font-bold">(0.0, 0.0)</td>
            <td class="text-left">Menempati posisi awal vertex A</td>
        </tr>
        <tr class="row-summary">
            <td class="text-center font-bold">Pusat (Pivot)</td>
            <td class="text-center">(0.5, 0.5)</td>
            <td class="text-center">x' = 1 - 0.5 = 0.5; &nbsp; y' = 0.5</td>
            <td class="text-center font-bold">(0.5, 0.5)</td>
            <td class="text-left">Titik pusat bernilai tetap (Invarian)</td>
        </tr>
    </tbody>
</table>

<!-- ==================== HALAMAN 3: TUGAS 1 GRAFIK & ANALISIS ==================== -->
<div class="page-break"></div>

<h3 class="sub-title">C. Tangkapan Grafik Visualisasi Tugas 1</h3>
<div class="image-container">
    <img src="{b64_t1}" alt="Grafik Tugas 1: Rotasi Persegi 90 Derajat terhadap Titik Pusat">
    <div class="image-caption">Gambar 1. Plot Visualisasi Tugas 1: Persegi Awal (Garis Biru), Hasil Rotasi 90&deg; (Garis Putus-putus Merah), Titik Pusat (Bintang Hijau), dan Panah Lintasan Rotasi Siklis.</div>
</div>

<h3 class="sub-title">D. Analisis Hasil Transformasi</h3>
<div class="academic-box">
    <p><strong>Wawasan Geometris Kunci:</strong></p>
    <ol>
        <li>
            <strong>Invarian Bentuk Spasial (Spatial Invariance):</strong><br>
            Persegi memiliki simetri rotasi lipat-4 (C<sub>4</sub>). Oleh karena itu, rotasi sebesar 90&deg; terhadap titik pusat massanya (0.5, 0.5) menghasilkan area poligon yang tepat bertumpuk sempurna dengan bentuk bidang asalnya di dalam bidang 2D.
        </li>
        <li>
            <strong>Perpindahan Siklis Indeks Vertex:</strong><br>
            Meskipun siluet geometris luarnya tampak tidak berubah, identitas dan lokasi setiap titik sudut bergeser satu posisi secara siklis berlawanan arah jarum jam: <strong>A &rarr; B &rarr; C &rarr; D &rarr; A</strong>.
        </li>
        <li>
            <strong>Perbedaan Fundamental dengan Rotasi terhadap Origin (0,0):</strong><br>
            Jika rotasi 90&deg; dieksekusi langsung terhadap titik origin (0,0), seluruh persegi akan terlempar keluar dari kuadran I menuju kuadran II, yaitu menempati koordinat [(0,0), (0,1), (-1,1), (-1,0)]. Penerapan algoritma translasi ke origin lalu rotasi dan translasi balik ke posisi pivot adalah syarat mutlak untuk merealisasikan rotasi di tempat (<em>in-place rotation</em>).
        </li>
    </ol>
</div>

<!-- ==================== HALAMAN 4: TUGAS 2 SPESIFIKASI & TABEL ==================== -->
<div class="page-break"></div>

<h2 class="section-title">4. Tugas 2: Simulator Transformasi Geometri 2D Sederhana</h2>

<h3 class="sub-title">A. Spesifikasi &amp; Desain Poligon</h3>
<p>
    Tugas 2 mengimplementasikan simulator 2D parametrik dengan objek uji poligon beranggotakan <strong>5 vertex</strong>. Dipilih poligon tak beraturan (asimetris) agar deformasi skala dan arah putaran rotasi terlihat jelas tanpa ambiguitas simetri:<br>
    <strong>V<sub>1</sub>(1.0, 1.0), &nbsp; V<sub>2</sub>(4.0, 1.0), &nbsp; V<sub>3</sub>(5.0, 3.0), &nbsp; V<sub>4</sub>(3.0, 5.0), &nbsp; V<sub>5</sub>(1.0, 3.5)</strong><br>
    Titik Pusat Massa (Centroid) dihitung secara analitis:<br>
    <strong>P<sub>centroid</sub> = ((1+4+5+3+1)/5, &nbsp; (1+1+3+5+3.5)/5) = (2.80, 2.70)</strong>
</p>

<h3 class="sub-title">B. Parameter Masukan Pengguna &amp; Formulasi Matriks Komposit</h3>
<p>Program menerima input parameter transformasi dari pengguna melalui antarmuka CLI:</p>
<ul>
    <li>Translasi: t<sub>x</sub> = 4.00, &nbsp; t<sub>y</sub> = 2.50 &nbsp;|&nbsp; Sudut Rotasi: &theta; = 45.00&deg; (Counter-Clockwise)</li>
    <li>Faktor Skala: s<sub>x</sub> = 1.50, &nbsp; s<sub>y</sub> = 1.20 &nbsp;|&nbsp; Titik Pusat (Pivot): P<sub>c</sub>(2.80, 2.70) (Centroid poligon)</li>
</ul>
<p>Matriks komposit gabungan dihitung sebagai perkalian berurutan:</p>
<div class="formula-box">
    M<sub>total</sub> = T(t<sub>x</sub>, t<sub>y</sub>) &middot; M<sub>R</sub>(&theta;, p<sub>x</sub>, p<sub>y</sub>) &middot; M<sub>S</sub>(s<sub>x</sub>, s<sub>y</sub>, p<sub>x</sub>, p<sub>y</sub>)<br><br>
    M<sub>total</sub> = <br>
    [ &nbsp;1.0607 &nbsp; -0.8485 &nbsp; &nbsp;6.1212 ]<br>
    [ &nbsp;1.0607 &nbsp; &nbsp;0.8485 &nbsp; -0.0609 ]<br>
    [ &nbsp;0.0000 &nbsp; &nbsp;0.0000 &nbsp; &nbsp;1.0000 ]
</div>

<h3 class="sub-title">C. Tabel Koordinat Hasil Transformasi Poligon 5 Vertex</h3>
<div class="table-caption">Tabel 2. Hasil Transformasi Poligon 5 Vertex pada Simulator Transformasi 2D</div>
<table class="academic-table">
    <thead>
        <tr>
            <th style="width: 14%;">Vertex</th>
            <th style="width: 22%;">Koordinat Asli (x, y)</th>
            <th style="width: 24%;">Koordinat Hasil (x', y')</th>
            <th style="width: 40%;">Analisis Perubahan Geometris</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="text-center font-bold">V1</td>
            <td class="text-center">(1.00, 1.00)</td>
            <td class="text-center font-bold">(6.33, 1.85)</td>
            <td class="text-left">Mengalami peregangan skala, rotasi 45&deg;, dan translasi ke kanan</td>
        </tr>
        <tr>
            <td class="text-center font-bold">V2</td>
            <td class="text-center">(4.00, 1.00)</td>
            <td class="text-center font-bold">(9.52, 5.03)</td>
            <td class="text-left">Titik terjauh horizontal bergeser mendekati koordinat x = 10</td>
        </tr>
        <tr>
            <td class="text-center font-bold">V3</td>
            <td class="text-center">(5.00, 3.00)</td>
            <td class="text-center font-bold">(8.88, 7.79)</td>
            <td class="text-left">Puncak samping kanan terotasi ke kuadran atas secara proporsional</td>
        </tr>
        <tr>
            <td class="text-center font-bold">V4</td>
            <td class="text-center">(3.00, 5.00)</td>
            <td class="text-center font-bold">(5.06, 7.36)</td>
            <td class="text-left">Puncak tertinggi terotasi 45&deg; berlawanan arah jarum jam (CCW)</td>
        </tr>
        <tr>
            <td class="text-center font-bold">V5</td>
            <td class="text-center">(1.00, 3.50)</td>
            <td class="text-center font-bold">(4.21, 3.97)</td>
            <td class="text-left">Sisi kiri poligon mempertahankan proporsi dan topologi bentuk</td>
        </tr>
        <tr class="row-summary">
            <td class="text-center font-bold">Pivot (Centroid)</td>
            <td class="text-center">(2.80, 2.70)</td>
            <td class="text-center font-bold">(6.80, 5.20)</td>
            <td class="text-left">Berpindah tepat sejauh vektor translasi (+4.00, +2.50)</td>
        </tr>
    </tbody>
</table>

<!-- ==================== HALAMAN 5: TUGAS 2 GRAFIK & ANALISIS ==================== -->
<div class="page-break"></div>

<h3 class="sub-title">D. Tangkapan Grafik Visualisasi Simulator</h3>
<div class="image-container">
    <img src="{b64_t2}" alt="Grafik Tugas 2: Simulator Transformasi 2D">
    <div class="image-caption">Gambar 2. Plot Visualisasi Simulator 2D: Poligon Asli (Garis Biru), Hasil Transformasi Gabungan (Garis Oranye), Pivot Awal &amp; Akhir (Bintang Hijau &amp; Merah), Vektor Perpindahan Pivot, Label Vertex, dan Kisi Koordinat Kartesius.</div>
</div>

<h3 class="sub-title">E. Analisis &amp; Verifikasi Karakteristik Transformasi</h3>
<div class="academic-box">
    <p><strong>Evaluasi Hasil Simulator:</strong></p>
    <ol>
        <li>
            <strong>Integritas Topologi Objek:</strong> Poligon hasil transformasi mempertahankan keterhubungan antar vertex (topologi tertutup) tanpa terjadi distorsi garis silang (<em>non-self-intersecting</em>), membuktikan validitas matriks affine.
        </li>
        <li>
            <strong>Perpindahan Pivot yang Presisi:</strong> Titik pivot berpindah tepat dari (2.80, 2.70) ke (6.80, 5.20), yang bersesuaian persis dengan pergeseran translasi murni (+4.00, +2.50). Hal ini membuktikan bahwa scaling dan rotasi terhadap pivot tidak menggeser titik pivot itu sendiri.
        </li>
        <li>
            <strong>Skalabilitas Vektor NumPy:</strong> Transformasi seluruh poligon dieksekusi dalam satu operasi perkalian matriks terpadu tanpa iterasi per vertex, menjamin efisiensi komputasi grafika.
        </li>
    </ol>
</div>

<!-- ==================== HALAMAN 6: TUGAS 3 SPESIFIKASI & PERHITUNGAN ==================== -->
<div class="page-break"></div>

<h2 class="section-title">5. Tugas 3: Analisis Perbandingan Urutan Transformasi</h2>

<h3 class="sub-title">A. Deskripsi Permasalahan</h3>
<p>
    Tugas ini bertujuan menganalisis sensitivitas urutan operasi transformasi geometri 2D pada satu titik vertex uji <strong>V(2.0, 3.0)</strong> dengan membandingkan dua sekuens transformasi yang berbeda:
</p>
<ul>
    <li><strong>Urutan 1: Translasi &rarr; Rotasi &rarr; Scaling (T &rarr; R &rarr; S)</strong></li>
    <li><strong>Urutan 2: Scaling &rarr; Rotasi &rarr; Translasi (S &rarr; R &rarr; T)</strong></li>
</ul>
<p>
    Parameter pengujian: Translasi T(t<sub>x</sub>=4.0, t<sub>y</sub>=2.0), Rotasi R(&theta;=90&deg; CCW), Scaling S(s<sub>x</sub>=2.0, s<sub>y</sub>=3.0).
</p>

<h3 class="sub-title">B. Perhitungan Numerik Langkah Demi Langkah pada Vertex V(2, 3)</h3>
<div class="table-caption">Tabel 3. Perhitungan Langkah Demi Langkah Transformasi Vertex V(2, 3) (Urutan 1 vs Urutan 2)</div>
<table class="academic-table">
    <thead>
        <tr>
            <th style="width: 26%;">Tahapan Transformasi</th>
            <th style="width: 37%;">Urutan 1: Translasi &rarr; Rotasi &rarr; Scaling</th>
            <th style="width: 37%;">Urutan 2: Scaling &rarr; Rotasi &rarr; Translasi</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="font-bold text-left">0. Titik Asal V</td>
            <td class="text-center font-bold">(2.00, 3.00)</td>
            <td class="text-center font-bold">(2.00, 3.00)</td>
        </tr>
        <tr>
            <td class="font-bold text-left">1. Transformasi Pertama</td>
            <td class="text-left">
                <em>Translasi (+4.0, +2.0):</em><br>
                x<sub>1</sub> = 2 + 4 = 6<br>
                y<sub>1</sub> = 3 + 2 = 5 &nbsp;&implies;&nbsp; <strong>V<sub>1</sub> = (6.00, 5.00)</strong>
            </td>
            <td class="text-left">
                <em>Scaling (2&times;, 3&times;):</em><br>
                x<sub>1</sub> = 2 &times; 2 = 4<br>
                y<sub>1</sub> = 3 &times; 3 = 9 &nbsp;&implies;&nbsp; <strong>W<sub>1</sub> = (4.00, 9.00)</strong>
            </td>
        </tr>
        <tr>
            <td class="font-bold text-left">2. Transformasi Kedua</td>
            <td class="text-left">
                <em>Rotasi 90&deg; thd origin:</em><br>
                x<sub>2</sub> = 6&middot;cos(90&deg;) - 5&middot;sin(90&deg;) = -5<br>
                y<sub>2</sub> = 6&middot;sin(90&deg;) + 5&middot;cos(90&deg;) = 6 &nbsp;&implies;&nbsp; <strong>V<sub>2</sub> = (-5.00, 6.00)</strong>
            </td>
            <td class="text-left">
                <em>Rotasi 90&deg; thd origin:</em><br>
                x<sub>2</sub> = 4&middot;cos(90&deg;) - 9&middot;sin(90&deg;) = -9<br>
                y<sub>2</sub> = 4&middot;sin(90&deg;) + 9&middot;cos(90&deg;) = 4 &nbsp;&implies;&nbsp; <strong>W<sub>2</sub> = (-9.00, 4.00)</strong>
            </td>
        </tr>
        <tr>
            <td class="font-bold text-left">3. Transformasi Ketiga</td>
            <td class="text-left">
                <em>Scaling (2&times;, 3&times;):</em><br>
                x<sub>3</sub> = -5 &times; 2 = -10<br>
                y<sub>3</sub> = 6 &times; 3 = 18 &nbsp;&implies;&nbsp; <strong>V<sub>TRS</sub>' = (-10.00, 18.00)</strong>
            </td>
            <td class="text-left">
                <em>Translasi (+4.0, +2.0):</em><br>
                x<sub>3</sub> = -9 + 4 = -5<br>
                y<sub>3</sub> = 4 + 2 = 6 &nbsp;&implies;&nbsp; <strong>W<sub>SRT</sub>' = (-5.00, 6.00)</strong>
            </td>
        </tr>
        <tr class="row-summary">
            <td class="font-bold text-left">HASIL AKHIR</td>
            <td class="text-center font-bold">V<sub>TRS</sub>' = (-10.00, 18.00)</td>
            <td class="text-center font-bold">W<sub>SRT</sub>' = (-5.00, 6.00)</td>
        </tr>
    </tbody>
</table>

<h3 class="sub-title">C. Pembuktian Aljabar Matriks Komposit 3&times;3 &amp; Jarak Euclidean</h3>
<div class="formula-box">
    <table style="width: 100%; border-collapse: collapse; font-size: 8.5pt;">
        <tr>
            <td style="width: 50%; vertical-align: top; padding-right: 5px;">
                <strong>Urutan 1 (M<sub>TRS</sub> = S &middot; R &middot; T):</strong><br>
                [ &nbsp;0.0 &nbsp; -2.0 &nbsp; -4.0 ]<br>
                [ &nbsp;3.0 &nbsp; &nbsp;0.0 &nbsp; 12.0 ]<br>
                [ &nbsp;0.0 &nbsp; &nbsp;0.0 &nbsp; &nbsp;1.0 ]
            </td>
            <td style="width: 50%; vertical-align: top; padding-left: 5px;">
                <strong>Urutan 2 (M<sub>SRT</sub> = T &middot; R &middot; S):</strong><br>
                [ &nbsp;0.0 &nbsp; -3.0 &nbsp; &nbsp;4.0 ]<br>
                [ &nbsp;2.0 &nbsp; &nbsp;0.0 &nbsp; &nbsp;2.0 ]<br>
                [ &nbsp;0.0 &nbsp; &nbsp;0.0 &nbsp; &nbsp;1.0 ]
            </td>
        </tr>
    </table>
</div>
<div class="formula-box">
    <strong>Perhitungan Selisih Koordinat &amp; Jarak Euclidean:</strong><br>
    &Delta;x = |-10.00 - (-5.00)| = 5.00 satuan, &nbsp;&nbsp; &Delta;y = |18.00 - 6.00| = 12.00 satuan<br>
    d = &radic;((&Delta;x)<sup>2</sup> + (&Delta;y)<sup>2</sup>) = &radic;(5.00<sup>2</sup> + 12.00<sup>2</sup>) = &radic;(25.00 + 144.00) = &radic;169.00 = <strong>13.0000 satuan</strong>
</div>

<!-- ==================== HALAMAN 7: TUGAS 3 GRAFIK & PEMBAHASAN ==================== -->
<div class="page-break"></div>

<h3 class="sub-title">D. Tangkapan Grafik Perbandingan Urutan Transformasi</h3>
<div class="image-container">
    <img src="{b64_t3}" alt="Grafik Tugas 3: Perbandingan Urutan Transformasi">
    <div class="image-caption">Gambar 3. Plot Visualisasi Tugas 3: Perbandingan Lintasan Langkah Demi Langkah Vertex V(2,3) serta Poligon Referensi untuk Urutan 1 (Kiri: T &rarr; R &rarr; S) dan Urutan 2 (Kanan: S &rarr; R &rarr; T).</div>
</div>

<h3 class="sub-title">E. Pembahasan Ilmiah: Mengapa Kedua Urutan Menghasilkan Nilai Berbeda?</h3>
<div class="academic-box">
    <p><strong>Jawaban Evaluasi:</strong><br>
    <strong>TIDAK SAMA.</strong> Hasil akhir kedua urutan transformasi tersebut menghasilkan posisi koordinat, orientasi, dan ukuran spasial yang sama sekali berbeda.</p>

    <p><strong>Penjelasan Berdasarkan Konsep Transformasi Geometris &amp; Aljabar Linier:</strong></p>
    <ol>
        <li>
            <strong>Sifat Non-Komutatif Perkalian Matriks:</strong><br>
            Transformasi affine 2D dinyatakan dalam representasi perkalian matriks. Operasi perkalian matriks secara umum <em>tidak bersifat komutatif</em> (A &middot; B &ne; B &middot; A). Oleh karena itu:
            <br>
            <strong>S &middot; R &middot; T &ne; T &middot; R &middot; S</strong>.
        </li>
        <li>
            <strong>Amplifikasi Translasi oleh Rotasi &amp; Skala (Urutan 1: T &rarr; R &rarr; S):</strong><br>
            Ketika translasi (t<sub>x</sub>, t<sub>y</sub>) diterapkan di awal, posisi titik dijauhkan dari origin (0,0). Ketika rotasi dan scaling diterapkan berikutnya, vektor translasi tersebut ikut terputar sebesar &theta; dan diperbesar oleh faktor skala (s<sub>x</sub>, s<sub>y</sub>):
            <br>
            &Delta;x<sub>eff</sub> = s<sub>x</sub>(t<sub>x</sub> cos&theta; - t<sub>y</sub> sin&theta;) = 2 &middot; (4 &middot; 0 - 2 &middot; 1) = <strong>-4.0</strong><br>
            &Delta;y<sub>eff</sub> = s<sub>y</sub>(t<sub>x</sub> sin&theta; + t<sub>y</sub> cos&theta;) = 3 &middot; (4 &middot; 1 + 2 &middot; 0) = <strong>+12.0</strong>
        </li>
        <li>
            <strong>Translasi Murni Bebas Amplifikasi (Urutan 2: S &rarr; R &rarr; T):</strong><br>
            Pada Urutan 2, titik diskalakan dan dirotasi terlebih dahulu terhadap origin. Translasi (t<sub>x</sub>, t<sub>y</sub>) baru diterapkan pada tahapan terakhir sebagai pergeseran linier murni:
            <br>
            &Delta;x<sub>eff</sub> = t<sub>x</sub> = <strong>+4.0</strong>, &nbsp;&nbsp;
            &Delta;y<sub>eff</sub> = t<sub>y</sub> = <strong>+2.0</strong>.<br>
            Pergeseran translasi ini tidak dipengaruhi oleh nilai rotasi maupun faktor skala.
        </li>
    </ol>
</div>

<!-- ==================== HALAMAN 8: KESIMPULAN & REFERENSI ==================== -->
<div class="page-break"></div>

<h2 class="section-title">6. Kesimpulan Akhir</h2>
<ol>
    <li>
        <strong>Representasi Homogen 3&times;3:</strong> Menjadi standar baku dalam grafika komputer karena memadukan operasi transformasi linear (rotasi, scaling) dan transformasi affine (translasi) ke dalam satu formulasi aljabar perkalian matriks tunggal yang seragam dan efisien.
    </li>
    <li>
        <strong>Pusat Rotasi Arbitrer (Tugas 1):</strong> Rotasi terhadap sembarang titik pivot bukan origin mutlak memerlukan prosedur 3 tahap: T(p) &middot; R &middot; T(-p). Rotasi 90&deg; pada persegi berpusat (0.5, 0.5) membuktikan sifat invarian spasial bentuk (area siluet tetap bertumpuk), namun mengalami pergeseran siklis pada indeks vertex (A &rarr; B &rarr; C &rarr; D &rarr; A).
    </li>
    <li>
        <strong>Simulator Transformasi 2D (Tugas 2):</strong> Mampu memodelkan dan mentransformasikan poligon sembarang secara parametrik dan presisi tinggi dengan menggabungkan pergeseran pivot centroid dan transformasi komposit bertingkat tanpa distorsi topologi.
    </li>
    <li>
        <strong>Sensitivitas Urutan Operasi (Tugas 3):</strong> Urutan penerapan matriks transformasi memegang peranan krusial dalam pipeline grafika komputer (seperti pada <em>Scene Graph</em> dan <em>Hierarchical Modeling</em>). Transformasi skala dan rotasi yang mendahului translasi (ruang lokal ke ruang dunia / <em>Local-to-World Space</em>) merupakan konvensi standar untuk menjaga bentuk dan orientasi objek sebelum ditempatkan pada posisi ruang global.
    </li>
</ol>

<h3 class="sub-title" style="margin-top: 18px;">Referensi Akademik</h3>
<ul style="list-style-type: square;">
    <li>Hearn, D., Baker, M. P., &amp; Carithers, W. (2011). <em>Computer Graphics with OpenGL</em> (4th ed.). Pearson.</li>
    <li>Foley, J. D., van Dam, A., Feiner, S. K., &amp; Hughes, J. F. (1996). <em>Computer Graphics: Principles and Practice in C</em> (2nd ed.). Addison-Wesley.</li>
    <li>Shirley, P., &amp; Marschner, S. (2009). <em>Fundamentals of Computer Graphics</em> (3rd ed.). A K Peters/CRC Press.</li>
</ul>

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
