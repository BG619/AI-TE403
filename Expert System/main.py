
# EXPERT SYSTEM: Diagnosis Awal Transformator

print("====================================")
print(" SISTEM PAKAR TRANSFORMATOR LISTRIK")
print("====================================")

# Mengumpulkan fakta dari pengguna
suhu = input("Apakah suhu transformator tinggi? (ya/tidak): ").lower()
pendingin = input("Apakah sistem pendingin bermasalah? (ya/tidak): ").lower()
alarm = input("Apakah alarm proteksi aktif? (ya/tidak): ").lower()

print("\n========== HASIL ANALISIS ==========")

# Aturan 1
if suhu == "ya" and pendingin == "ya":
    print("Dugaan: Gangguan pada sistem pendingin.")
    print("Saran: Periksa kipas, pompa, dan sistem pendingin.")

# Aturan 2
elif suhu == "ya" and alarm == "ya":
    print("Dugaan: Kondisi temperatur tinggi disertai alarm.")
    print("Saran: Periksa indikasi alarm dan data temperatur.")

# Aturan 3
elif suhu == "tidak" and pendingin == "tidak" and alarm == "tidak":
    print("Dugaan: Tidak ditemukan indikasi gangguan dari input.")
    print("Saran: Lanjutkan pemantauan dan pemeriksaan rutin.")

# Aturan 4
else:
    print("Kesimpulan: Data belum cukup untuk menentukan dugaan.")
    print("Saran: Periksa kondisi transformator lebih lanjut.")

print("====================================")

