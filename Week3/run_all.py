"""
Script Utama: Menjalankan Seluruh Tugas 1, 2, dan 3 (Grafika Citra Week 3)
Secara Sekaligus dan Menyimpan Seluruh Grafik Visual.
"""

import sys
from tugas1_rotasi_persegi import run_tugas1
from tugas2_simulator_2d import run_simulator
from tugas3_perbandingan_urutan import run_tugas3


def main():
    show_plot = "--no-show" not in sys.argv
    print("*" * 80)
    print("EKSEKUSI SELURUH PENUGASAN REPRESENTASI 2D & TRANSFORMASI DASAR")
    print("Mata Kuliah : Grafika Komputer dan Pengolahan Citra")
    print("Pertemuan   : Week 3 / Pertemuan 2")
    print("*" * 80)

    print("\n>>> MENJALANKAN TUGAS 1...")
    run_tugas1(save_path="tugas1_rotasi_persegi.png", show_plot=show_plot)

    print("\n>>> MENJALANKAN TUGAS 2...")
    run_simulator(save_path="tugas2_simulator_2d.png", show_plot=show_plot)

    print("\n>>> MENJALANKAN TUGAS 3...")
    run_tugas3(save_path="tugas3_perbandingan_urutan.png", show_plot=show_plot)

    print("\n" + "*" * 80)
    print("SEMUA PENUGASAN (TUGAS 1, 2, 3) TELAH SELESAI DIEKSEKUSI DENGAN SUKSES!")
    print("Grafik tersimpan:")
    print("1. tugas1_rotasi_persegi.png")
    print("2. tugas2_simulator_2d.png")
    print("3. tugas3_perbandingan_urutan.png")
    print("*" * 80)


if __name__ == '__main__':
    main()
