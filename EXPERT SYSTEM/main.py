
# ---------------------------------------------------------------
# 1. KNOWLEDGE BASE
# Setiap aturan: JIKA semua kondisi terpenuhi, MAKA kesimpulan benar.
# Kesimpulan sebuah aturan bisa dipakai sebagai kondisi aturan lain.
# ---------------------------------------------------------------
ATURAN = [
    {
        "id": "R1",
        "jika": ["laptop_tidak_menyala", "lampu_charger_mati"],
        "maka": "charger_bermasalah",
    },
    {
        "id": "R2",
        "jika": ["laptop_tidak_menyala", "lampu_charger_nyala"],
        "maka": "baterai_atau_motherboard_bermasalah",
    },
    {
        "id": "R3",
        "jika": ["laptop_menyala", "layar_hitam", "ada_suara_kipas"],
        "maka": "layar_atau_kabel_layar_bermasalah",
    },
    {
        "id": "R4",
        "jika": ["laptop_menyala", "sangat_lambat", "hdd_berbunyi"],
        "maka": "harddisk_bermasalah",
    },
    {
        "id": "R5",
        "jika": ["laptop_menyala", "sangat_lambat", "sering_panas"],
        "maka": "overheat",
    },
    {
        "id": "R6",
        "jika": ["overheat", "kipas_berisik"],
        "maka": "kipas_kotor_perlu_dibersihkan",
    },
]

# Pertanyaan untuk user (setiap pertanyaan = 1 fakta)
PERTANYAAN = {
    "laptop_tidak_menyala": "Apakah laptop sama sekali tidak menyala?",
    "lampu_charger_mati": "Apakah lampu indikator charger mati?",
    "lampu_charger_nyala": "Apakah lampu indikator charger menyala?",
    "laptop_menyala": "Apakah laptop bisa menyala?",
    "layar_hitam": "Apakah layar tetap hitam?",
    "ada_suara_kipas": "Apakah terdengar suara kipas?",
    "sangat_lambat": "Apakah laptop sangat lambat?",
    "hdd_berbunyi": "Apakah terdengar bunyi 'klik' dari harddisk?",
    "sering_panas": "Apakah laptop sering panas?",
    "kipas_berisik": "Apakah kipas terdengar sangat berisik?",
}

# Penjelasan solusi untuk tiap kesimpulan akhir
SOLUSI = {
    "charger_bermasalah": "Coba ganti charger atau cek kabel & colokan listrik.",
    "baterai_atau_motherboard_bermasalah": "Lepas baterai lalu coba nyalakan dengan charger. Jika tetap gagal, bawa ke servis.",
    "layar_atau_kabel_layar_bermasalah": "Coba sambungkan ke monitor eksternal. Jika tampil, layar/kabel fleksibelnya rusak.",
    "harddisk_bermasalah": "Segera backup data, lalu ganti harddisk (disarankan ke SSD).",
    "overheat": "Pastikan ventilasi tidak tertutup dan gunakan cooling pad.",
    "kipas_kotor_perlu_dibersihkan": "Bersihkan debu pada kipas dan ganti thermal paste.",
}


# ---------------------------------------------------------------
# 2. INFERENCE ENGINE (Forward Chaining)
# ---------------------------------------------------------------
def inference_engine(fakta):
    """
    fakta: himpunan (set) fakta yang diketahui dari jawaban user.
    Mengembalikan fakta lengkap + riwayat aturan yang dijalankan.
    """
    riwayat = []  # untuk explanation facility
    ada_perubahan = True

    while ada_perubahan:
        ada_perubahan = False
        for aturan in ATURAN:
            # Cek: semua kondisi aturan ada di fakta? & kesimpulan belum diketahui?
            kondisi_terpenuhi = all(k in fakta for k in aturan["jika"])
            if kondisi_terpenuhi and aturan["maka"] not in fakta:
                fakta.add(aturan["maka"])  # fakta baru!
                riwayat.append(aturan)
                ada_perubahan = True

    return fakta, riwayat


# ---------------------------------------------------------------
# 3. USER INTERFACE
# ---------------------------------------------------------------
def tanya_ya_tidak(teks):
    while True:
        jawab = input(f"{teks} (y/t): ").strip().lower()
        if jawab in ("y", "t"):
            return jawab == "y"
        print("  Jawab dengan 'y' atau 't' saja.")


def main():
    print("=" * 50)
    print("  EXPERT SYSTEM: DIAGNOSA KERUSAKAN LAPTOP")
    print("=" * 50)
    print("Jawab pertanyaan berikut dengan y (ya) atau t (tidak).\n")

    # Kumpulkan fakta dari user (working memory)
    fakta = set()
    for kode, teks in PERTANYAAN.items():
        if tanya_ya_tidak(teks):
            fakta.add(kode)

    # Jalankan mesin inferensi
    fakta_akhir, riwayat = inference_engine(fakta)

    # Tampilkan hasil
    print("\n" + "=" * 50)
    print("  HASIL DIAGNOSA")
    print("=" * 50)

    kesimpulan = [a["maka"] for a in riwayat]
    # Ambil hanya kesimpulan yang punya solusi (kesimpulan akhir)
    hasil_akhir = [k for k in kesimpulan if k in SOLUSI]

    if not hasil_akhir:
        print("Maaf, sistem tidak menemukan kesimpulan dari gejala tersebut.")
        print("Sebaiknya konsultasikan ke teknisi.")
        return

    for k in hasil_akhir:
        print(f"\nDiagnosa : {k.replace('_', ' ').title()}")
        print(f"Solusi   : {SOLUSI[k]}")

    # EXPLANATION FACILITY: ciri khas expert system, bisa menjelaskan "kenapa"
    print("\n--- Penjelasan (bagaimana sistem sampai ke kesimpulan) ---")
    for a in riwayat:
        kondisi = " DAN ".join(a["jika"])
        print(f"[{a['id']}] JIKA {kondisi}")
        print(f"       MAKA {a['maka']}")


if __name__ == "__main__":
    main()
