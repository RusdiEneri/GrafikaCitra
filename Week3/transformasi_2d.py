"""
Modul Transformasi Geometri 2D
Mata Kuliah: Grafika Komputer dan Pengolahan Citra
Implementasi representasi matriks homogen 3x3 dan fungsi aljabar transformasi 2D:
- Translasi
- Rotasi (terhadap origin dan titik pivot sembarang)
- Scaling (terhadap origin dan titik pivot sembarang)
- Komposisi Matriks Transformasi
"""

import numpy as np


def to_homogeneous(points):
    """
    Mengonversi array titik (N, 2) atau (2,) ke koordinat homogen (N, 3) dengan w=1.
    """
    pts = np.asarray(points, dtype=float)
    if pts.ndim == 1:
        return np.append(pts, 1.0)
    return np.hstack([pts, np.ones((pts.shape[0], 1), dtype=float)])


def from_homogeneous(points_h):
    """
    Mengonversi kembali koordinat homogen (N, 3) atau (3,) ke koordinat kartesius 2D (N, 2).
    """
    pts_h = np.asarray(points_h, dtype=float)
    if pts_h.ndim == 1:
        return (pts_h[:2] / pts_h[2])
    return (pts_h[:, :2] / pts_h[:, 2:3])


def matriks_translasi(tx, ty):
    """
    Menghasilkan matriks transformasi translasi 2D homogen 3x3:
    [ 1  0  tx ]
    [ 0  1  ty ]
    [ 0  0  1  ]
    """
    return np.array([
        [1.0, 0.0, float(tx)],
        [0.0, 1.0, float(ty)],
        [0.0, 0.0, 1.0]
    ], dtype=float)


def matriks_rotasi(theta_deg, px=0.0, py=0.0):
    """
    Menghasilkan matriks transformasi rotasi 2D homogen 3x3 sebesar theta_deg (derajat)
    berlawanan arah jarum jam (CCW) terhadap pivot (px, py).
    M = T(px, py) @ R(theta) @ T(-px, -py)
    """
    rad = np.radians(theta_deg)
    cos_t = np.cos(rad)
    sin_t = np.sin(rad)

    r_origin = np.array([
        [cos_t, -sin_t, 0.0],
        [sin_t,  cos_t, 0.0],
        [0.0,    0.0,   1.0]
    ], dtype=float)

    if px == 0.0 and py == 0.0:
        return r_origin

    t_to = matriks_translasi(-px, -py)
    t_back = matriks_translasi(px, py)
    return t_back @ r_origin @ t_to


def matriks_scaling(sx, sy, px=0.0, py=0.0):
    """
    Menghasilkan matriks transformasi scaling 2D homogen 3x3 dengan faktor (sx, sy)
    terhadap pivot (px, py).
    M = T(px, py) @ S(sx, sy) @ T(-px, -py)
    """
    s_origin = np.array([
        [float(sx), 0.0,       0.0],
        [0.0,       float(sy), 0.0],
        [0.0,       0.0,       1.0]
    ], dtype=float)

    if px == 0.0 and py == 0.0:
        return s_origin

    t_to = matriks_translasi(-px, -py)
    t_back = matriks_translasi(px, py)
    return t_back @ s_origin @ t_to


def transform(points, matrix):
    """
    Menerapkan matriks transformasi homogen 3x3 ke titik-titik 2D.
    points: array-like berukuran (N, 2) atau (2,)
    matrix: matriks 3x3
    Return: array titik yang telah ditransformasikan berukuran sama.
    """
    pts = np.asarray(points, dtype=float)
    is_single = (pts.ndim == 1)
    pts_h = to_homogeneous(pts)

    # P_new = (M @ P_col) -> untuk vektor baris: P_h @ M.T
    if is_single:
        pts_new_h = matrix @ pts_h
    else:
        pts_new_h = pts_h @ matrix.T

    return from_homogeneous(pts_new_h)


# Fungsi langsung (direct transformation helpers)
def translasi(points, tx, ty):
    """Menggeser titik sejauh tx dan ty"""
    m = matriks_translasi(tx, ty)
    return transform(points, m)


def rotasi(points, theta_deg, pivot=(0.0, 0.0)):
    """Memutar titik sebesar theta_deg terhadap titik pusat pivot"""
    m = matriks_rotasi(theta_deg, px=pivot[0], py=pivot[1])
    return transform(points, m)


def scaling(points, sx, sy, pivot=(0.0, 0.0)):
    """Menskalakan titik dengan faktor sx, sy terhadap titik pusat pivot"""
    m = matriks_scaling(sx, sy, px=pivot[0], py=pivot[1])
    return transform(points, m)


def hitung_pusat_massa(points):
    """
    Menghitung titik pusat massa (centroid) dari sekumpulan titik 2D.
    """
    pts = np.asarray(points, dtype=float)
    return np.mean(pts, axis=0)
