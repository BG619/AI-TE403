"""
CONTOH SIMPEL MULTI-AGENT SYSTEM
================================
Tiga agent bekerja sama membuat artikel pendek:

    Peneliti  --(fakta)-->  Penulis  --(draft)-->  Kritikus
                               ^                       |
                               +-----(saran revisi)----+

Ide utamanya:
  1. Setiap agent punya PERAN yang berbeda.
  2. Agent saling BERKOMUNIKASI lewat pesan (di sini: return value).
  3. Ada FEEDBACK LOOP: Kritikus bisa menolak, Penulis memperbaiki.

Jalankan:  python multi_agent_simple.py
"""
import time


class Agent:
    def __init__(self, nama):
        self.nama = nama

    def bicara(self, teks):
        print(f"[{self.nama:<9}] {teks}")
        time.sleep(0.8)  # pura-pura "berpikir"


class Peneliti(Agent):
    def kerja(self, topik):
        self.bicara(f"Mencari informasi tentang '{topik}'...")
        fakta = [
            "Python dibuat oleh Guido van Rossum pada tahun 1991.",
            "Python populer untuk AI, data science, dan web.",
            "Sintaksnya mudah dibaca sehingga cocok untuk pemula.",
        ]
        self.bicara(f"Ketemu {len(fakta)} fakta. Kirim ke Penulis.")
        return fakta


class Penulis(Agent):
    def kerja(self, fakta, saran=None):
        if saran is None:
            self.bicara("Menulis draft pertama...")
            return " ".join(fakta)

        self.bicara(f"Menerima saran: '{saran}'. Merevisi draft...")
        return " ".join(fakta) + " Kesimpulan: Python adalah pilihan bagus untuk belajar programming."


class Kritikus(Agent):
    def kerja(self, draft):
        self.bicara("Memeriksa draft...")
        if "Kesimpulan" not in draft:
            self.bicara("DITOLAK - belum ada kesimpulan.")
            return False, "Tambahkan kesimpulan di akhir"
        self.bicara("DISETUJUI - draft sudah bagus!")
        return True, None


def main():
    peneliti = Peneliti("Peneliti")
    penulis = Penulis("Penulis")
    kritikus = Kritikus("Kritikus")

    print("=" * 60)
    print(" TIM AGENT: membuat artikel tentang Python")
    print("=" * 60)

    # Langkah 1: Peneliti mengumpulkan fakta
    fakta = peneliti.kerja("Bahasa Python")

    # Langkah 2: Penulis membuat draft pertama
    draft = penulis.kerja(fakta)

    # Langkah 3: loop Kritikus <-> Penulis sampai disetujui
    for ronde in range(1, 4):
        print(f"\n--- Ronde review {ronde} ---")
        disetujui, saran = kritikus.kerja(draft)
        if disetujui:
            break
        draft = penulis.kerja(fakta, saran)

    print("\n" + "=" * 60)
    print(" HASIL AKHIR")
    print("=" * 60)
    print(draft)


if __name__ == "__main__":
    main()
