"""
TUGAS 2: Simulator Transformasi Geometri 2D Sederhana
Mata Kuliah : Grafika Komputer dan Pengolahan Citra (Pertemuan 2)

Deskripsi Soal:
1. Buat poligon minimal 5 vertex.
2. Program dapat menerima parameter dari pengguna (input tx, ty, sudut derajat, sx, sy, dan titik pusat).
3. Output harus memperlihatkan objek asli dan hasil transformasi dalam satu sistem koordinat.
4. Plot objek asal dan hasil dengan label serta grid.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from transformasi_2d import (
    matriks_translasi,
    matriks_rotasi,
    matriks_scaling,
    transform,
    hitung_pusat_massa
)


def get_default_polygon():
    """
    Poligon default 5 vertex (bentuk poligon asimetris agar orientasi dan deformasi
    rotasi/skala terlihat sangat jelas).
    Vertex:
    V1: (1.0, 1.0)
    V2: (4.0, 1.0)
    V3: (5.0, 3.0)
    V4: (3.0, 5.0)
    V5: (1.0, 3.5)
    """
    return np.array([
        [1.0, 1.0],
        [4.0, 1.0],
        [5.0, 3.0],
        [3.0, 5.0],
        [1.0, 3.5]
    ], dtype=float)


def prompt_user_parameters(auto_default=False):
    """
    Meminta parameter transformasi dari input pengguna dengan fallback nilai default.
    Jika auto_default=True (atau stdin tidak interaktif), gunakan nilai default.
    """
    defaults = {
        'tx': 4.0,
        'ty': 2.5,
        'sudut': 45.0,
        'sx': 1.5,
        'sy': 1.2,
        'use_centroid': True,
        'px': 2.8,  # diisi nanti jika centroid
        'py': 2.7
    }

    if auto_default or not sys.stdin.isatty():
        print("[INFO] Menggunakan parameter default (Mode Otomatis/Non-Interaktif).")
        return defaults

    print("\n" + "=" * 60)
    print("MASUKKAN PARAMETER TRANSFORMASI 2D")
    print("(Tekan Enter langsung untuk menggunakan nilai default dalam kurung siku)")
    print("=" * 60)

    def ask(prompt, def_val, conv=float):
        val = input(f"{prompt} [{def_val}]: ").strip()
        if not val:
            return def_val
        try:
            return conv(val)
        except ValueError:
            print(f"Input tidak valid, memakai default: {def_val}")
            return def_val

    tx = ask("1. Translasi horizontal (tx)", defaults['tx'])
    ty = ask("2. Translasi vertikal (ty)", defaults['ty'])
    sudut = ask("3. Sudut rotasi dalam derajat (berlawanan jarum jam)", defaults['sudut'])
    sx = ask("4. Faktor skala horizontal (sx)", defaults['sx'])
    sy = ask("5. Faktor skala vertikal (sy)", defaults['sy'])

    ans_center = input("6. Gunakan titik pusat massa (centroid) poligon sebagai pivot? (y/n) [y]: ").strip().lower()
    use_centroid = (ans_center != 'n')

    px, py = 0.0, 0.0
    if not use_centroid:
        px = ask("   - Koordinat pivot X (px)", 0.0)
        py = ask("   - Koordinat pivot Y (py)", 0.0)

    return {
        'tx': tx,
        'ty': ty,
        'sudut': sudut,
        'sx': sx,
        'sy': sy,
        'use_centroid': use_centroid,
        'px': px,
        'py': py
    }


def run_simulator(params=None, save_path="tugas2_simulator_2d.png", show_plot=True):
    print("=" * 70)
    print("TUGAS 2: SIMULATOR TRANSFORMASI GEOMETRI 2D SEDERHANA")
    print("=" * 70)

    poly_awal = get_default_polygon()
    centroid = hitung_pusat_massa(poly_awal)

    if params is None:
        auto_mode = ("--default" in sys.argv or "--no-show" in sys.argv or not sys.stdin.isatty())
        params = prompt_user_parameters(auto_default=auto_mode)

    if params.get('use_centroid', True):
        px, py = centroid[0], centroid[1]
    else:
        px, py = params['px'], params['py']

    tx = params['tx']
    ty = params['ty']
    sudut = params['sudut']
    sx = params['sx']
    sy = params['sy']

    print(f"\n[PARAMETER TERPILIH]")
    print(f"- Poligon Awal       : 5 Vertex")
    print(f"- Titik Pusat Pivot  : ({px:.2f}, {py:.2f}) {'(Centroid)' if params.get('use_centroid', True) else '(Custom)'}")
    print(f"- Translasi (tx, ty) : ({tx:.2f}, {ty:.2f})")
    print(f"- Rotasi (derajat)   : {sudut:.2f}°")
    print(f"- Scaling (sx, sy)   : ({sx:.2f}, {sy:.2f})")

    # Pembentukan Matriks Transformasi Komposit Homogen 3x3:
    # Transformasi objek dilakukan terhadap titik pivot:
    # 1. Objek diskalakan terhadap pivot: S_pivot = T(px, py) @ S(sx, sy) @ T(-px, -py)
    # 2. Objek dirotasi terhadap pivot:   R_pivot = T(px, py) @ R(theta) @ T(-px, -py)
    # 3. Objek ditranslasikan sebesar tx, ty: T(tx, ty)
    # Komposisi total:
    # M_total = T(tx, ty) @ R_pivot @ S_pivot
    m_translasi = matriks_translasi(tx, ty)
    m_rot_pivot = matriks_rotasi(sudut, px=px, py=py)
    m_scale_pivot = matriks_scaling(sx, sy, px=px, py=py)

    m_komposit = m_translasi @ m_rot_pivot @ m_scale_pivot

    print("\n[MATRIKS TRANSFORMASI HOMOGEN 3x3 KOMPOSIT]")
    print(np.round(m_komposit, 4))

    # Terapkan transformasi
    poly_hasil = transform(poly_awal, m_komposit)
    pivot_awal = np.array([px, py])
    pivot_hasil = transform(pivot_awal, m_translasi)  # Pivot ikut berpindah karena translasi

    # Tabel Koordinat
    print("\n[TABEL KOORDINAT HASIL TRANSFORMASI]")
    print("-" * 65)
    print(f"{'Vertex':<8} | {'Koordinat Asal (x, y)':<22} | {'Hasil Transformasi (x\', y\')':<24}")
    print("-" * 65)
    for i in range(len(poly_awal)):
        v_awal = poly_awal[i]
        v_hasil = poly_hasil[i]
        print(f"  V{i+1:<5} | ({v_awal[0]:5.2f}, {v_awal[1]:5.2f})             | ({v_hasil[0]:5.2f}, {v_hasil[1]:5.2f})")
    print("-" * 65)
    print(f"  Pivot  | ({px:5.2f}, {py:5.2f})             | ({pivot_hasil[0]:5.2f}, {pivot_hasil[1]:5.2f})")
    print("-" * 65)

    # Visualisasi
    fig, ax = plt.subplots(figsize=(10, 8.5), dpi=150)
    
    # Grid dan Axes
    ax.axhline(0, color='#888888', linestyle='--', linewidth=0.9, alpha=0.8)
    ax.axvline(0, color='#888888', linestyle='--', linewidth=0.9, alpha=0.8)
    ax.grid(True, which='both', color='#e0e0e0', linestyle=':', linewidth=0.9)

    def close_poly(pts):
        return np.vstack([pts, pts[0]])

    poly_awal_c = close_poly(poly_awal)
    poly_hasil_c = close_poly(poly_hasil)

    # Plot Objek Asli
    ax.plot(poly_awal_c[:, 0], poly_awal_c[:, 1],
            'o-', color='#1f77b4', linewidth=2.0, label='Poligon Asli (5 Vertex)', zorder=4)
    ax.fill(poly_awal_c[:, 0], poly_awal_c[:, 1],
            color='#1f77b4', alpha=0.20, zorder=2)

    # Plot Objek Hasil Transformasi
    ax.plot(poly_hasil_c[:, 0], poly_hasil_c[:, 1],
            's-', color='#ff7f0e', linewidth=2.0,
            label=f'Hasil Transformasi (T+R+S)', zorder=5)
    ax.fill(poly_hasil_c[:, 0], poly_hasil_c[:, 1],
            color='#ff7f0e', alpha=0.22, zorder=3)

    # Plot Pivot Point
    ax.plot(px, py, marker='*', markersize=13, color='#2ca02c', markeredgecolor='black',
            linestyle='None', label=f'Pivot Awal ({px:.2f}, {py:.2f})', zorder=6)
    ax.plot(pivot_hasil[0], pivot_hasil[1], marker='*', markersize=13, color='#d62728', markeredgecolor='black',
            linestyle='None', label=f'Pivot Akhir ({pivot_hasil[0]:.2f}, {pivot_hasil[1]:.2f})', zorder=6)

    # Garis vektor pergeseran pivot
    ax.annotate(
        "", xy=(pivot_hasil[0], pivot_hasil[1]), xytext=(px, py),
        arrowprops=dict(arrowstyle="->", color='#2ca02c', linestyle='--', linewidth=1.5, alpha=0.8)
    )

    # Label Titik Vertex
    for i in range(len(poly_awal)):
        xa, ya = poly_awal[i]
        xh, yh = poly_hasil[i]
        ax.text(xa - 0.15, ya + 0.15, f"V{i+1}", color='#1f77b4', fontsize=9.5, fontweight='bold')
        ax.text(xh + 0.15, yh + 0.15, f"V{i+1}'", color='#d35400', fontsize=9.5, fontweight='bold')

    # Atur Batas dan Aspek Plot
    all_x = np.concatenate([poly_awal[:, 0], poly_hasil[:, 0], [px, pivot_hasil[0]]])
    all_y = np.concatenate([poly_awal[:, 1], poly_hasil[:, 1], [py, pivot_hasil[1]]])
    margin_x = (all_x.max() - all_x.min()) * 0.25 + 1.0
    margin_y = (all_y.max() - all_y.min()) * 0.25 + 1.0

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(min(0, all_x.min()) - 1.0, all_x.max() + margin_x)
    ax.set_ylim(min(0, all_y.min()) - 1.0, all_y.max() + margin_y)

    ax.set_xlabel("Sumbu X (Satuan Koordinat)", fontsize=11, fontweight='semibold')
    ax.set_ylabel("Sumbu Y (Satuan Koordinat)", fontsize=11, fontweight='semibold')
    ax.set_title("Tugas 2: Simulator Transformasi Geometri 2D (5 Vertex)",
                 fontsize=13, fontweight='bold', pad=15)
    
    ax.legend(loc='upper left', framealpha=0.93, edgecolor='#cccccc', fontsize=9)

    info_box = (
        f"Parameter Pengguna:\n"
        f"• Translasi (tx, ty) = ({tx:.2f}, {ty:.2f})\n"
        f"• Sudut Rotasi     = {sudut:.1f}°\n"
        f"• Skala (sx, sy)   = ({sx:.2f}, {sy:.2f})\n"
        f"• Titik Pusat      = ({px:.2f}, {py:.2f})\n\n"
        f"Urutan Komposit:\n"
        f"M = T(tx,ty) · R_pivot(θ) · S_pivot(sx,sy)"
    )
    ax.text(0.98, 0.03, info_box, transform=ax.transAxes, fontsize=8.5,
            verticalalignment='bottom', horizontalalignment='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#ffffff', edgecolor='#bdc3c7', alpha=0.92))

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n[INFO] Gambar grafik simulator berhasil disimpan di: {save_path}")

    if show_plot:
        plt.show()

    return poly_awal, poly_hasil, params


if __name__ == '__main__':
    show = "--no-show" not in sys.argv
    run_simulator(show_plot=show)
