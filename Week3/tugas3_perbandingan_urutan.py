"""
TUGAS 3: Perbandingan Urutan Transformasi Geometri 2D
Mata Kuliah : Grafika Komputer dan Pengolahan Citra (Pertemuan 2)

Deskripsi Soal:
1. Bandingkan hasil Translasi -> Rotasi -> Scaling (T -> R -> S)
   dengan Scaling -> Rotasi -> Translasi (S -> R -> T) pada satu vertex,
   dan berikan hasil analisisnya.
2. Apakah hasil akhir kedua urutan transformasi tersebut sama?
   Jelaskan berdasarkan hasil eksperimen dan konsep transformasi geometris.
"""

import sys
import numpy as np
import matplotlib.pyplot as plt
from transformasi_2d import (
    matriks_translasi,
    matriks_rotasi,
    matriks_scaling,
    transform
)


def run_tugas3(save_path="tugas3_perbandingan_urutan.png", show_plot=True):
    print("=" * 75)
    print("TUGAS 3: ANALISIS PERBANDINGAN URUTAN TRANSFORMASI GEOMETRI 2D")
    print("=" * 75)

    # 1. Definisi Vertex Uji & Parameter Transformasi
    # Satu vertex uji sesuai ketentuan soal:
    v_uji = np.array([2.0, 3.0], dtype=float)
    
    # Poligon pembantu (segitiga referensi) untuk memberikan konteks visual orientasi & bentuk
    poly_ref = np.array([
        [2.0, 3.0],  # Vertex uji V
        [4.0, 3.0],
        [3.0, 5.0]
    ], dtype=float)

    # Parameter Transformasi
    tx, ty = 4.0, 2.0         # Translasi
    sudut = 90.0              # Rotasi dalam derajat (CCW)
    sx, sy = 2.0, 3.0         # Scaling

    print(f"\n[TITIK UJI & PARAMETER]")
    print(f"• Titik Uji (Vertex) : V({v_uji[0]:.1f}, {v_uji[1]:.1f})")
    print(f"• Translasi (tx, ty) : (+{tx:.1f}, +{ty:.1f})")
    print(f"• Rotasi (sudut)     : {sudut:.1f}°")
    print(f"• Scaling (sx, sy)   : ({sx:.1f}x, {sy:.1f}x)")

    # 2. Definisi Matriks Homogen Dasar (terhadap origin)
    T = matriks_translasi(tx, ty)
    R = matriks_rotasi(sudut, px=0.0, py=0.0)
    S = matriks_scaling(sx, sy, px=0.0, py=0.0)

    # -------------------------------------------------------------------------
    # URUTAN 1: TRANSLASI -> ROTASI -> SCALING (T -> R -> S)
    # -------------------------------------------------------------------------
    # Matriks Komposit: M_TRS = S @ R @ T  (karena P' = S @ (R @ (T @ P)))
    M_TRS = S @ R @ T

    # Jejak koordinat langkah demi langkah untuk vertex V:
    v1_step0 = v_uji.copy()
    v1_step1 = transform(v1_step0, T)      # Setelah Translasi
    v1_step2 = transform(v1_step1, R)      # Setelah Rotasi
    v1_step3 = transform(v1_step2, S)      # Setelah Scaling (Hasil Akhir Urutan 1)

    # -------------------------------------------------------------------------
    # URUTAN 2: SCALING -> ROTASI -> TRANSLASI (S -> R -> T)
    # -------------------------------------------------------------------------
    # Matriks Komposit: M_SRT = T @ R @ S  (karena P' = T @ (R @ (S @ P)))
    M_SRT = T @ R @ S

    # Jejak koordinat langkah demi langkah untuk vertex V:
    v2_step0 = v_uji.copy()
    v2_step1 = transform(v2_step0, S)      # Setelah Scaling
    v2_step2 = transform(v2_step1, R)      # Setelah Rotasi
    v2_step3 = transform(v2_step2, T)      # Setelah Translasi (Hasil Akhir Urutan 2)

    # Transformasi poligon referensi
    poly_trs = transform(poly_ref, M_TRS)
    poly_srt = transform(poly_ref, M_SRT)

    # Jarak Euklidian antara kedua hasil akhir
    jarak_selisih = np.linalg.norm(v1_step3 - v2_step3)

    # 3. Output Terminal
    print("\n" + "=" * 75)
    print("HASIL PERHITUNGAN LANGKAH DEMI LANGKAH PADA VERTEX V(2.0, 3.0)")
    print("=" * 75)
    print(f"Tahap                 | Urutan 1: T -> R -> S          | Urutan 2: S -> R -> T")
    print("-" * 75)
    print(f"0. Posisi Awal        | ({v1_step0[0]:6.2f}, {v1_step0[1]:6.2f})             | ({v2_step0[0]:6.2f}, {v2_step0[1]:6.2f})")
    print(f"1. Transformasi Ke-1  | [T] -> ({v1_step1[0]:6.2f}, {v1_step1[1]:6.2f})       | [S] -> ({v2_step1[0]:6.2f}, {v2_step1[1]:6.2f})")
    print(f"2. Transformasi Ke-2  | [R] -> ({v1_step2[0]:6.2f}, {v1_step2[1]:6.2f})       | [R] -> ({v2_step2[0]:6.2f}, {v2_step2[1]:6.2f})")
    print(f"3. Transformasi Ke-3  | [S] -> ({v1_step3[0]:6.2f}, {v1_step3[1]:6.2f})       | [T] -> ({v2_step3[0]:6.2f}, {v2_step3[1]:6.2f})")
    print("-" * 75)
    print(f"HASIL AKHIR (V')      | V_TRS' = ({v1_step3[0]:5.2f}, {v1_step3[1]:5.2f})      | V_SRT' = ({v2_step3[0]:5.2f}, {v2_step3[1]:5.2f})")
    print(f"Perbedaan Jarak (Euclidean Distance): {jarak_selisih:.4f} satuan")
    print("-" * 75)

    print("\n[PERBANDINGAN MATRIKS HOMOGEN KOMPOSIT 3x3]")
    print("\nMatriks M_TRS (S @ R @ T):")
    print(np.round(M_TRS, 4))
    print("\nMatriks M_SRT (T @ R @ S):")
    print(np.round(M_SRT, 4))
    print(f"\nApakah M_TRS == M_SRT? {'YA (SAMA)' if np.allclose(M_TRS, M_SRT) else 'TIDAK (BERBEDA SECARA SIGNIFIKAN)'}")

    print("\n" + "=" * 75)
    print("KESIMPULAN DAN ANALISIS ILMIAH:")
    print("=" * 75)
    print("1. Apakah hasil akhir kedua urutan sama?")
    print("   JAWABAN: TIDAK SAMA. Hasil akhir kedua urutan menghasilkan posisi,")
    print("   orientasi, dan deformasi spasial yang sangat berbeda.")
    print("   - Urutan T -> R -> S menghasilkan titik akhir: (-10.00, 18.00)")
    print("   - Urutan S -> R -> T menghasilkan titik akhir: ( -5.00,  6.00)")
    print("   - Selisih jarak spasial = 13.0000 satuan.")
    print("\n2. Mengapa hal ini terjadi? (Penjelasan Konseptual):")
    print("   a. Sifat Aljabar Matriks (Non-Komutatif):")
    print("      Perkalian matriks bersifat non-komutatif (A @ B != B @ A).")
    print("      Akibatnya: S @ R @ T != T @ R @ S.")
    print("   b. Pengaruh Translasi Awal:")
    print("      Pada urutan T -> R -> S, vektor translasi diterapkan lebih dulu")
    print("      sehingga posisi objek menjauh dari origin (titik pusat rotasi/skala).")
    print("      Ketika rotasi dan scaling diterapkan kemudian, jarak pergeseran translasi")
    print("      ikut diputar dan dilipatgandakan (teramplifikasi) oleh faktor skala.")
    print("   c. Pengaruh Translasi Akhir:")
    print("      Pada urutan S -> R -> T, objek diskalakan dan diputar terlebih dahulu")
    print("      di sekitar origin, lalu pergeseran translasi murni ditambahkan di akhir")
    print("      tanpa terpengaruh oleh faktor rotasi maupun skala.")
    print("=" * 75)

    # 4. Visualisasi Komprehensif (Subplots)
    fig, axs = plt.subplots(1, 2, figsize=(14, 6.5), dpi=150)
    fig.suptitle("Tugas 3: Perbandingan Urutan Transformasi (T->R->S vs S->R->T)",
                 fontsize=14, fontweight='bold', y=0.98)

    def close_poly(pts):
        return np.vstack([pts, pts[0]])

    # Subplot 1: Lintasan Vertex dan Poligon pada Urutan 1 (T -> R -> S)
    ax1 = axs[0]
    ax1.set_title("Urutan 1: Translasi → Rotasi → Scaling (T → R → S)\nPosisi Akhir: V' = (-10, 18)",
                  fontsize=11, fontweight='bold', color='#1f77b4')
    ax1.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax1.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax1.grid(True, linestyle=':', alpha=0.6)

    # Plot lintasan vertex Urutan 1
    steps_1 = np.array([v1_step0, v1_step1, v1_step2, v1_step3])
    labels_1 = ["V(2,3) Awal", "V_T(6,5) [T]", "V_TR(-5,6) [R]", "V_TRS'(-10,18) [S]"]
    colors_1 = ['#333333', '#2ca02c', '#ff7f0e', '#d62728']

    ax1.plot(steps_1[:, 0], steps_1[:, 1], 'k:', linewidth=1.2, alpha=0.5, zorder=3)
    for idx, (pt, lbl, col) in enumerate(zip(steps_1, labels_1, colors_1)):
        ax1.scatter(pt[0], pt[1], color=col, s=70, zorder=5, label=lbl)
        offset = (0.3, 0.4) if idx % 2 == 0 else (-2.5, -0.7)
        ax1.text(pt[0] + offset[0], pt[1] + offset[1], lbl, fontsize=8.5, fontweight='bold', color=col)

    # Poligon awal vs akhir Urutan 1
    p_orig = close_poly(poly_ref)
    p_trs = close_poly(poly_trs)
    ax1.plot(p_orig[:, 0], p_orig[:, 1], 'b-', linewidth=1.5, alpha=0.6, label='Poligon Awal')
    ax1.fill(p_orig[:, 0], p_orig[:, 1], 'blue', alpha=0.15)
    ax1.plot(p_trs[:, 0], p_trs[:, 1], 'r--', linewidth=1.8, label='Poligon Akhir (T->R->S)')
    ax1.fill(p_trs[:, 0], p_trs[:, 1], 'red', alpha=0.15)

    ax1.set_xlabel("Sumbu X", fontweight='semibold')
    ax1.set_ylabel("Sumbu Y", fontweight='semibold')
    ax1.legend(loc='lower left', fontsize=8, framealpha=0.9)
    ax1.set_aspect('equal', adjustable='box')

    # Subplot 2: Lintasan Vertex dan Poligon pada Urutan 2 (S -> R -> T)
    ax2 = axs[1]
    ax2.set_title("Urutan 2: Scaling → Rotasi → Translasi (S → R → T)\nPosisi Akhir: V' = (-5, 6)",
                  fontsize=11, fontweight='bold', color='#d62728')
    ax2.axhline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax2.axvline(0, color='gray', linestyle='--', linewidth=0.8, alpha=0.7)
    ax2.grid(True, linestyle=':', alpha=0.6)

    # Plot lintasan vertex Urutan 2
    steps_2 = np.array([v2_step0, v2_step1, v2_step2, v2_step3])
    labels_2 = ["V(2,3) Awal", "V_S(4,9) [S]", "V_SR(-9,4) [R]", "V_SRT'(-5,6) [T]"]
    colors_2 = ['#333333', '#9467bd', '#17becf', '#2ca02c']

    ax2.plot(steps_2[:, 0], steps_2[:, 1], 'k:', linewidth=1.2, alpha=0.5, zorder=3)
    for idx, (pt, lbl, col) in enumerate(zip(steps_2, labels_2, colors_2)):
        ax2.scatter(pt[0], pt[1], color=col, s=70, zorder=5, label=lbl)
        offset = (0.3, 0.4) if idx % 2 == 0 else (-2.2, -0.6)
        ax2.text(pt[0] + offset[0], pt[1] + offset[1], lbl, fontsize=8.5, fontweight='bold', color=col)

    # Poligon awal vs akhir Urutan 2
    p_srt = close_poly(poly_srt)
    ax2.plot(p_orig[:, 0], p_orig[:, 1], 'b-', linewidth=1.5, alpha=0.6, label='Poligon Awal')
    ax2.fill(p_orig[:, 0], p_orig[:, 1], 'blue', alpha=0.15)
    ax2.plot(p_srt[:, 0], p_srt[:, 1], 'g--', linewidth=1.8, label='Poligon Akhir (S->R->T)')
    ax2.fill(p_srt[:, 0], p_srt[:, 1], 'green', alpha=0.15)

    ax2.set_xlabel("Sumbu X", fontweight='semibold')
    ax2.set_ylabel("Sumbu Y", fontweight='semibold')
    ax2.legend(loc='lower left', fontsize=8, framealpha=0.9)
    ax2.set_aspect('equal', adjustable='box')

    # Samakan batas sumbu kedua plot agar perbandingan skala visual adil dan intuitif
    min_x = min(ax1.get_xlim()[0], ax2.get_xlim()[0], -12)
    max_x = max(ax1.get_xlim()[1], ax2.get_xlim()[1], 8)
    min_y = min(ax1.get_ylim()[0], ax2.get_ylim()[0], -2)
    max_y = max(ax1.get_ylim()[1], ax2.get_ylim()[1], 20)

    for ax in [ax1, ax2]:
        ax.set_xlim(min_x, max_x)
        ax.set_ylim(min_y, max_y)

    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"\n[INFO] Gambar grafik perbandingan berhasil disimpan di: {save_path}")

    if show_plot:
        plt.show()

    return v1_step3, v2_step3, M_TRS, M_SRT


if __name__ == '__main__':
    show = "--no-show" not in sys.argv
    run_tugas3(show_plot=show)
