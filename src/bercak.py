"""bercak.py: analisis bercak SIMUTEH (dipakai ulang mulai P7).""" 
import json 
import cv2 
import numpy as np 
from utils_tepi import mask_daun_awal, bercak_awal 
  
PARAM_BERCAK = { 
    "kanal": 2,            # kanal terpilih (2 = R) 
    "k": 4.0,              # ambang median + k x MAD 
    "se_bentuk": "elips",  # "elips", "persegi", "silang" 
    "se_open": 5,          # ukuran SE opening (0 = tidak dipakai) 
    "se_close": 5,         # ukuran SE closing (0 = tidak dipakai) 
    "luas_min": 20,        # piksel 
    "bulat_min": 0.5, 
    "rasio_maks": 1.8, 
    "batas_ringan": 0.1,   # persen bercak minimum kelas Ringan 
    "batas_berat": 2.0,    # persen bercak minimum kelas Berat 
    "mm_per_px": 0.4375, 
} 

_BENTUK = {"elips": cv2.MORPH_ELLIPSE, "persegi": cv2.MORPH_RECT, "silang": cv2.MORPH_CROSS} 
  
def _se(p, uk): 
    return cv2.getStructuringElement(_BENTUK[p["se_bentuk"]], (uk, uk)) 
  
def bersihkan(biner, p): 
    """Opening membuang titik derau dan potongan tipis; closing menutup celah.""" 
    # TODO 1: bila p["se_open"] > 0, lakukan opening dengan SE _se(p, p["se_open"]) 
    if p["se_open"] > 0:
        se_open = _se(p, p["se_open"])
        biner = cv2.morphologyEx(biner, cv2.MORPH_OPEN, se_open)
        
    # TODO 2: bila p["se_close"] > 0, lakukan closing dengan SE _se(p, p["se_close"]) 
    if p["se_close"] > 0:
        se_close = _se(p, p["se_close"])
        biner = cv2.morphologyEx(biner, cv2.MORPH_CLOSE, se_close)
        
    return biner 
  
def ukur_dan_saring(biner, p): 
    """Mengembalikan mask bercak tersaring dan daftar ukuran setiap bercak.""" 
    # TODO 3: label komponen terhubung (konektivitas 8) dengan cv2.connectedComponentsWithStats 
    n, lbl, st, cen = cv2.connectedComponentsWithStats((biner > 0).astype(np.uint8), connectivity=8)
    
    keluar, daftar = np.zeros_like(biner), [] 
    
    # TODO 4 & 5: Loop setiap komponen, hitung ukuran, dan saring
    for i in range(1, n): 
        # TODO 4: hitung luas, keliling, kebulatan, dan rasio aspek
        A = int(st[i, cv2.CC_STAT_AREA])
        
        # Cari kontur untuk keliling dan rasio aspek
        komponen = (lbl == i).astype(np.uint8)
        kontur, _ = cv2.findContours(komponen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        if len(kontur) > 0:
            keliling = cv2.arcLength(kontur[0], True)
            
            # Rumus kebulatan: 4 * pi * luas / keliling^2
            kebulatan = 0.0 if keliling == 0 else 4 * np.pi * A / (keliling ** 2)
            
            # Rumus rasio aspek
            w, h = cv2.minAreaRect(kontur[0])[1]
            rasio = max(w, h) / max(min(w, h), 1) 
            
            # TODO 5: simpan ke mask keluar hanya komponen yang memenuhi syarat
            if (A >= p["luas_min"]) and (kebulatan >= p["bulat_min"]) and (rasio <= p["rasio_maks"]):
                keluar[lbl == i] = 255  # Masukkan ke mask keluar
                
                # Catat ukurannya ke daftar
                daftar.append({
                    "luas_px": A,
                    "luas_mm2": round(A * p["mm_per_px"] ** 2, 2),
                    "keliling_px": round(keliling, 1),
                    "kebulatan": round(kebulatan, 2),
                    "rasio_aspek": round(rasio, 2),
                    "cx": int(cen[i][0]),
                    "cy": int(cen[i][1])
                })
                
    return keluar, daftar

def analisis_daun(img_praproses, p=None): 
    """Masukan: citra BGR hasil praproses. Keluaran: kamus hasil analisis.""" 
    p = {**PARAM_BERCAK, **(p or {})} 
    m_daun = mask_daun_awal(img_praproses) 
    biner = bercak_awal(img_praproses, m_daun, kanal=p["kanal"], k=p["k"]) 
    m_bercak, daftar = ukur_dan_saring(bersihkan(biner, p), p) 
    
    # TODO 6: hitung persen bercak = luas bercak / luas daun x 100 
    luas_bercak = np.sum(m_bercak > 0)
    luas_daun = np.sum(m_daun > 0)
    
    # Hindari pembagian dengan nol
    if luas_daun == 0:
        persen = 0.0
    else:
        persen = (luas_bercak / luas_daun) * 100.0
        
    # TODO 7: tentukan kelas dengan batas_ringan dan batas_berat 
    if persen < p["batas_ringan"]:
        kelas = "Sehat"
    elif persen >= p["batas_ringan"] and persen < p["batas_berat"]:
        kelas = "Ringan"
    else:
        kelas = "Berat"
        
    return {
        "mask_daun": m_daun, 
        "mask_bercak": m_bercak, 
        "jumlah_bercak": len(daftar), 
        "persen_bercak": round(float(persen), 3), 
        "kelas": kelas, 
        "bercak": daftar
    } 
  
def simpan_param(p, path="./hasil/param_bercak.json"): 
    with open(path, "w") as f: 
        json.dump({**PARAM_BERCAK, **p}, f, indent=2)
