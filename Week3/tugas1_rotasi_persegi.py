"""
TUGAS 1: Rotasi Persegi 90 Derajat Terhadap Titik Pusat (Bukan Origin)
Mata Kuliah : Grafika Komputer dan Pengolahan Citra (Pertemuan 2)

Deskripsi Soal:
Diberikan sebuah persegi dengan titik sudut:
A(0,0), B(1,0), C(1,1), D(0,1).
Buatlah program Python yang:
1. Merotasi persegi tersebut sebesar 90° terhadap titik pusatnya (bukan origin).
2. Menampilkan bentuk sebelum dan sesudah transformasi dalam satu plot.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from transformasi_2d import (
    matriks_translasi,
    matriks_rotasi,
    transform,
    hitung_pusat_massa
)


def run_tugas1(save_path="tugas1_rotasi_persegi.png", show_plot=True):
    print("=" * 70)
    print("TUGAS 1: ROTASI PERSEGI 90° TERHADAP TITIK PUSAT (PIVOT CENTROID)")
    print("=" * 70)

    # 1. Definisi Titik Sudut Persegi
    # Format baris: [x, y]
    persegi_awal = np.array([
        [0.0, 0.0],  # Titik A
        [1.0, 0.0],  # Titik B
        [1.0, 1.0],  # Titik C
        [0.0, 1.0]   # Titik D
    ], dtype=float)
    label_titik = ['A', 'B', 'C', 'D']

    # 2. Perhitungan Titik Pusat (Centroid) Persegi
    # x_c = (0 + 1 + 1 + 0) / 4 = 0.5
    # y_c = (0 + 0 + 1 + 1) / 4 = 0.5
    pusat = hitung_pusat_massa(persegi_awal)
    px, py = pusat[0], pusat[1]
    print(f"\n1. Titik Pusat (Centroid) Persegi:")
    print(f"   Pusat P = ({px:.2f}, {py:.2f})")

    # 3. Parameter Rotasi
    sudut = 90.0  # Derajat (berlawanan arah jarum jam / Counter-Clockwise)

    # 4. Pembentukan Matriks Transformasi Homogen 3x3
    # M_rotasi_pivot = T(px, py) @ R(90) @ T(-px, -py)
    m_rotasi = matriks_rotasi(sudut, px=px, py=py)
    
    print("\n2. Matriks Transformasi Homogen 3x3 (Rotasi 90° terhadap (0.5, 0.5)):")
    print(np.round(m_rotasi, 4))

    # 5. Transformasi Titik
    persegi_rotasi = transform(persegi_awal, m_rotasi)

    # 6. Tampilkan Tabel Koordinat Sebelum dan Sesudah
    print("\n3. Tabel Koordinat Vertex Sebelum & Sesudah Transformasi:")
    print("-" * 65)
    print(f"{'Vertex':<8} | {'Koordinat Awal (x, y)':<22} | {'Hasil Rotasi 90° (x\', y\')':<24}")
    print("-" * 65)
    for i, lbl in enumerate(label_titik):
        x_awal, y_awal = persegi_awal[i]
        x_rot, y_rot = persegi_rotasi[i]
        print(f"  {lbl:<6} | ({x_awal:4.1f}, {y_awal:4.1f})               | ({x_rot:4.1f}, {y_rot:4.1f})")
    print("-" * 65)

    print("\nAnalisis Hasil Geometris:")
    print("- Karena persegi berpusat simetris di (0.5, 0.5), rotasi 90° di sekeliling")
    print("  pusat mempertahankan area bidang yang sama (invariance bounding box).")
    print("- Namun, posisi masing-masing vertex bergeser 90° secara siklis:")
    print("  A(0,0) -> B(1,0) -> C(1,1) -> D(0,1) -> A(0,0).")

    # 7. Visualisasi dengan Matplotlib
    fig, ax = plt.subplots(figsize=(9, 8), dpi=150)
    
    # Grid dan Garis Sumbu Utama
    ax.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax.grid(True, which='both', color='#d3d3d3', linestyle=':', linewidth=0.8)

    # Helper menutup poligon (menambahkan titik awal di akhir)
    def close_poly(pts):
        return np.vstack([pts, pts[0]])

    poly_awal_closed = close_poly(persegi_awal)
    poly_rot_closed = close_poly(persegi_rotasi)

    # Plot Poligon Asli
    ax.plot(poly_awal_closed[:, 0], poly_awal_closed[:, 1],
            'o-', color='#1f77b4', linewidth=2.2, label='Persegi Awal (Original)', zorder=4)
    ax.fill(poly_awal_closed[:, 0], poly_awal_closed[:, 1],
            color='#1f77b4', alpha=0.18, zorder=2)

    # Plot Poligon Hasil Rotasi
    ax.plot(poly_rot_closed[:, 0], poly_rot_closed[:, 1],
            's--', color='#d62728', linewidth=2.0, label='Hasil Rotasi 90° terhadap Pusat', zorder=5)
    ax.fill(poly_rot_closed[:, 0], poly_rot_closed[:, 1],
            color='#d62728', alpha=0.15, zorder=3)

    # Plot Titik Pusat / Pivot
    ax.plot(px, py, marker='*', markersize=14, color='#2ca02c', markeredgecolor='black',
            linestyle='None', label=f'Pusat Rotasi ({px:.1f}, {py:.1f})', zorder=6)

    # Anotasi Label Titik Sudut Awal dan Hasil
    offset_awal = [(-0.10, -0.08), (0.05, -0.08), (0.05, 0.05), (-0.10, 0.05)]
    offset_rot = [(0.06, -0.03), (0.06, 0.03), (-0.15, 0.03), (-0.15, -0.03)]

    for i, lbl in enumerate(label_titik):
        # Awal
        xa, ya = persegi_awal[i]
        dxa, dya = offset_awal[i]
        ax.text(xa + dxa, ya + dya, f"{lbl}({xa:.0f},{ya:.0f})",
                color='#1f77b4', fontsize=10, fontweight='bold', zorder=7)

        # Hasil Rotasi
        xr, yr = persegi_rotasi[i]
        dxr, dyr = offset_rot[i]
        ax.text(xr + dxr, yr + dyr, f"{lbl}'({xr:.0f},{yr:.0f})",
                color='#d62728', fontsize=10, fontweight='bold', zorder=7)

        # Panah kurva rotasi dari titik awal ke titik hasil
        arc = patches.FancyArrowPatch(
            (xa, ya), (xr, yr),
            connectionstyle="arc3,rad=0.35",
            arrowstyle="->,head_width=3,head_length=5",
            color='#9467bd', linestyle='-.', linewidth=1.2, alpha=0.75, zorder=6
        )
        ax.add_patch(arc)

    # Set Aspect Equal dan Limit Tampilan
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-0.6, 1.6)
    ax.set_ylim(-0.6, 1.6)
    ax.set_xlabel("Sumbu X (Posisi Horizontal)", fontsize=11, fontweight='semibold')
    ax.set_ylabel("Sumbu Y (Posisi Vertikal)", fontsize=11, fontweight='semibold')
    ax.set_title("Tugas 1: Rotasi Persegi 90° terhadap Titik Pusat (0.5, 0.5)",
                 fontsize=13, fontweight='bold', pad=15)
    
    # Legend dan Anotasi Info
    ax.legend(loc='upper left', framealpha=0.92, edgecolor='#cccccc', fontsize=9.5)
    
    info_box = (
        "Rumus Matriks Rotasi terhadap Pivot P(px, py):\n"
        "M = T(px, py) · R(90°) · T(-px, -py)\n"
        "x' = -(y - 0.5) + 0.5 = 1 - y\n"
        "y' =  (x - 0.5) + 0.5 = x\n"
        "Rotasi siklis: A→B, B→C, C→D, D→A"
    )
    ax.text(0.98, 0.03, info_box, transform=ax.transAxes, fontsize=8.5,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8f9fa', edgecolor='#bdc3c7', alpha=0.9))

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n[INFO] Gambar grafik berhasil disimpan di: {save_path}")

    if show_plot:
        plt.show()

    return persegi_awal, persegi_rotasi, pusat


if __name__ == '__main__':
    show = "--no-show" not in sys.argv
    run_tugas1(show_plot=show)
