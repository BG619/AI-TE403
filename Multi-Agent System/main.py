# 1. Agen Pencari Data
class AgenPencari:
    def bekerja(self, query):
        print(f"🔍 [Agen Pencari]: Mencari data tentang '{query}'...")
        return f"Data mentah tentang {query}"

# 2. Agen Pengolah/Penyaring Data
class AgenPengolah:
    def bekerja(self, data_mentah):
        print(f"⚙️ [Agen Pengolah]: Merapikan dan menganalisis data...")
        return f"Hasil laporan bersih dari: {data_mentah}"

# --- SIMULASI KERJASAMA (MAS) ---
if __name__ == "__main__":
    # Inisialisasi agen
    pencari = AgenPencari()
    pengolah = AgenPengolah()

    # Alur kerja estafet antar agen
    print("--- MEMULAI SISTEM MULTI-AGENT ---")
    
    tugas_user = "Cuaca Hari Ini"
    
    # Langkah 1: Agen pencari bekerja
    hasil_cari = pencari.bekerja(tugas_user)
    
    # Langkah 2: Hasil agen pencari dioper ke agen pengolah
    hasil_akhir = pengolah.bekerja(hasil_cari)
    
    print("\n📦 Hasil Akhir:", hasil_akhir)
