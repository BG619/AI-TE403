# Sistem Pakar Rekomendasi Laptop (Forward Chaining)

Proyek mata kuliah **Kecerdasan Buatan (AI)** berupa sistem pakar sederhana berbasis aturan (*rule-based expert system*) yang merekomendasikan jenis laptop sesuai kebutuhan pengguna. Sistem memakai metode inferensi **forward chaining (rantai maju)** dan ditulis dengan Python murni, tanpa library tambahan.

> Struktur dan ide dasar proyek ini diadaptasi dari repositori template open source [vwang99/429assignment4](https://github.com/vwang99/429assignment4), lalu diterjemahkan ke Bahasa Indonesia, dilengkapi basis pengetahuan 15 aturan, dan disatukan dalam satu file.

---

## Daftar Isi

1. [Apa Itu Sistem Pakar?](#1-apa-itu-sistem-pakar)
2. [Komponen Sistem Pakar](#2-komponen-sistem-pakar)
3. [Metode Inferensi](#3-metode-inferensi)
4. [Gambaran Proyek](#4-gambaran-proyek)
5. [Struktur Kode](#5-struktur-kode)
6. [Basis Pengetahuan](#6-basis-pengetahuan)
7. [Cara Kerja Mesin Inferensi](#7-cara-kerja-mesin-inferensi)
8. [Cara Menjalankan](#8-cara-menjalankan)
9. [Contoh Eksekusi](#9-contoh-eksekusi)
10. [Cara Menambah Aturan](#10-cara-menambah-aturan)
11. [Kelebihan dan Keterbatasan](#11-kelebihan-dan-keterbatasan)
12. [Pengembangan Lanjutan](#12-pengembangan-lanjutan)
13. [Referensi](#13-referensi)

---

## 1. Apa Itu Sistem Pakar?

**Sistem pakar (expert system)** adalah cabang kecerdasan buatan klasik (*symbolic AI*) yang meniru kemampuan pengambilan keputusan seorang pakar manusia dalam bidang tertentu. Pengetahuan pakar direpresentasikan secara eksplisit dalam bentuk **aturan** berbentuk `JIKA ... MAKA ...` (*IF ... THEN ...*), lalu sebuah mesin inferensi menalar dari fakta yang diketahui untuk menghasilkan kesimpulan.

Berbeda dengan *machine learning* yang belajar dari data, sistem pakar bekerja dari pengetahuan yang ditulis manusia. Karena itu, keputusannya mudah dijelaskan dan ditelusuri.

Contoh penerapan sistem pakar: diagnosa penyakit, diagnosa kerusakan mesin atau peralatan, penasihat keuangan, dan konfigurasi produk.

---

## 2. Komponen Sistem Pakar

| Komponen | Fungsi | Padanan di proyek ini |
|---|---|---|
| **Basis pengetahuan** (*knowledge base*) | Menyimpan aturan dan pengetahuan pakar | List `ATURAN_LAPTOP` |
| **Working memory** (memori kerja) | Menyimpan fakta yang sedang diketahui, termasuk fakta hasil penalaran | `self.fakta` (sebuah `set`) di `MesinRantaiMaju` |
| **Mesin inferensi** (*inference engine*) | Menerapkan aturan pada fakta untuk menarik kesimpulan | Class `MesinRantaiMaju` |
| **Antarmuka pengguna** | Mengumpulkan fakta dan menampilkan hasil | Fungsi `kumpulkan_fakta_awal()` dan `cetak_hasil()` |
| **Fasilitas penjelasan** (*explanation facility*) | Menjelaskan alasan sebuah kesimpulan | `self.jejak` dan bagian "Jejak penalaran" |

---

## 3. Metode Inferensi

### Forward chaining (rantai maju) — dipakai di proyek ini
Penalaran **berbasis data** (*data-driven*). Mulai dari fakta yang sudah diketahui, sistem mencari aturan yang semua kondisinya terpenuhi, menjalankannya untuk menambah fakta baru, lalu mengulang sampai tidak ada aturan baru yang bisa dijalankan.

```
Fakta awal  ──►  cocokkan aturan  ──►  tambah fakta baru  ──►  ulangi  ──►  kesimpulan
```

Cocok dipakai ketika data sudah tersedia lebih dulu dan kita ingin tahu kesimpulan apa saja yang bisa ditarik.

### Backward chaining (rantai mundur) — sebagai pembanding
Penalaran **berbasis tujuan** (*goal-driven*). Mulai dari hipotesis atau tujuan, sistem mencari aturan yang konsekuennya sama dengan tujuan, lalu memeriksa apakah kondisinya bisa dibuktikan. Cocok untuk diagnosa, saat kita ingin memverifikasi satu dugaan tertentu.

| Aspek | Forward chaining | Backward chaining |
|---|---|---|
| Arah penalaran | Fakta → kesimpulan | Tujuan → fakta pendukung |
| Pendekatan | Data-driven | Goal-driven |
| Titik awal | Fakta yang diketahui | Hipotesis yang diuji |
| Cocok untuk | Konfigurasi, rekomendasi, monitoring | Diagnosa, verifikasi hipotesis |

---

## 4. Gambaran Proyek

Sistem mengajukan 10 pertanyaan ya/tidak kepada pengguna (portabilitas, baterai, anggaran, sistem operasi, kebutuhan gaming, dan seterusnya). Jawaban "ya" diubah menjadi **fakta awal**. Mesin inferensi lalu menjalankan aturan secara berulang dan menampilkan:

- **Rekomendasi**: jenis laptop yang cocok.
- **Spesifikasi**: saran spesifikasi minimum yang sesuai kebutuhan.
- **Penjelasan**: aturan mana yang menghasilkan tiap kesimpulan.
- **Jejak penalaran**: urutan lengkap aturan yang dijalankan.

---

## 5. Struktur Kode

Seluruh program ada dalam satu file, `main.py`, yang terbagi menjadi empat bagian:

```
main.py
├── 1. Model aturan        → dataclass Aturan
├── 2. Basis pengetahuan   → list ATURAN_LAPTOP (15 aturan)
├── 3. Mesin inferensi     → class MesinRantaiMaju
└── 4. Antarmuka CLI       → tanya(), kumpulkan_fakta_awal(), cetak_hasil(), main()
```

### Class `Aturan`

| Atribut | Tipe | Keterangan |
|---|---|---|
| `anteseden` | `List[str]` | Kondisi (bagian JIKA). Semua harus terpenuhi |
| `konsekuen` | `str` | Kesimpulan (bagian MAKA) |
| `prioritas` | `int` | Aturan berprioritas lebih tinggi dievaluasi lebih dulu |
| `nama` | `str` | Nama aturan, dipakai pada penjelasan dan jejak |

### Class `MesinRantaiMaju`

| Method | Fungsi |
|---|---|
| `tegaskan_fakta(awal)` | Memasukkan fakta awal ke working memory |
| `bisa_dijalankan(aturan)` | `True` jika semua anteseden ada di fakta **dan** konsekuen belum diketahui |
| `jalankan()` | Loop forward chaining sampai tidak ada aturan baru yang bisa dijalankan |
| `kesimpulan()` | Memisahkan hasil menjadi rekomendasi, spesifikasi, dan fakta lain |

### Konvensi penamaan fakta
- `rekomendasi:<nama>` untuk hasil rekomendasi akhir.
- `spesifikasi:<nama>` untuk saran spesifikasi.
- Fakta tanpa awalan adalah fakta masukan atau fakta antara, misalnya `portabel` dan `butuh_ringan`.

---

## 6. Basis Pengetahuan

### Fakta masukan (dari jawaban pengguna)

| Fakta | Arti |
|---|---|
| `portabel` | Portabilitas penting |
| `baterai_awet` | Butuh baterai awet |
| `anggaran_tinggi` / `anggaran_sedang` / `anggaran_rendah` | Tingkat anggaran (pilih satu) |
| `os_windows` / `os_macos` / `os_linux` | Preferensi sistem operasi (pilih satu) |
| `gaming` | Bermain game |
| `kerja_kreatif` | Pekerjaan kreatif (desain, video, dsb.) |
| `hanya_kantor` | Hanya untuk tugas kantor |
| `butuh_akselerasi_ai` | Butuh akselerasi AI |
| `layar_besar` | Ingin layar besar |
| `sering_bepergian` | Sering bepergian |

### Daftar aturan

| No | Nama aturan | JIKA | MAKA | Prioritas |
|---|---|---|---|---|
| 1 | Ultrabook Premium | `portabel` ∧ `baterai_awet` ∧ `anggaran_tinggi` | `rekomendasi:ultrabook_premium` | 5 |
| 2 | Gaming High-End | `gaming` ∧ `anggaran_tinggi` | `rekomendasi:laptop_gaming_high_end` | 5 |
| 3 | Gaming Menengah | `gaming` ∧ `anggaran_sedang` | `rekomendasi:laptop_gaming_menengah` | 4 |
| 4 | MacBook untuk Kreator | `kerja_kreatif` ∧ `os_macos` ∧ `anggaran_tinggi` | `rekomendasi:macbook_pro` | 5 |
| 5 | Kreator Windows | `kerja_kreatif` ∧ `os_windows` ∧ `anggaran_tinggi` | `rekomendasi:laptop_kreator_windows` | 4 |
| 6 | Kantor Hemat | `hanya_kantor` ∧ `anggaran_rendah` | `rekomendasi:laptop_kantor_hemat` | 3 |
| 7 | Ultrabook Menengah | `hanya_kantor` ∧ `portabel` ∧ `anggaran_sedang` | `rekomendasi:ultrabook_menengah` | 3 |
| 8 | Workstation AI | `butuh_akselerasi_ai` ∧ `anggaran_tinggi` | `rekomendasi:workstation_ai` | 4 |
| 9 | Butuh Bobot Ringan | `sering_bepergian` ∧ `portabel` | `butuh_ringan` *(fakta antara)* | 9 |
| 10 | Spesifikasi Bobot Ringan | `butuh_ringan` | `spesifikasi:bobot_di_bawah_1_5_kg` | 2 |
| 11 | Spesifikasi Baterai | `baterai_awet` | `spesifikasi:baterai_minimal_60wh` | 2 |
| 12 | Spesifikasi GPU Gaming | `gaming` | `spesifikasi:gpu_dedicated` | 2 |
| 13 | Spesifikasi Kreator | `kerja_kreatif` | `spesifikasi:ram_16gb_dan_layar_akurat_warna` | 2 |
| 14 | Spesifikasi Akselerasi AI | `butuh_akselerasi_ai` | `spesifikasi:npu_atau_gpu_dedicated` | 2 |
| 15 | Spesifikasi Layar Besar | `layar_besar` | `spesifikasi:layar_15_inci_atau_lebih` | 1 |

### Aturan berantai (*chaining*)
Aturan 9 dan 10 menunjukkan inti forward chaining. Aturan 9 menghasilkan **fakta antara** `butuh_ringan`, lalu fakta itu dipakai aturan 10 sebagai kondisi:

```
sering_bepergian ∧ portabel  ──►  butuh_ringan  ──►  spesifikasi:bobot_di_bawah_1_5_kg
        (aturan 9)                                        (aturan 10)
```

---

## 7. Cara Kerja Mesin Inferensi

Inti algoritma ada di method `jalankan()`:

```python
ada_aturan_jalan = True
while ada_aturan_jalan:
    ada_aturan_jalan = False
    for aturan in sorted(self.aturan, key=lambda r: (-r.prioritas, r.nama)):
        if self.bisa_dijalankan(aturan):
            self.fakta.add(aturan.konsekuen)      # tambah fakta baru
            self.jejak.append({...})              # catat untuk penjelasan
            ada_aturan_jalan = True               # ada perubahan → ulangi
```

**Langkah-langkahnya:**

1. Urutkan aturan berdasarkan prioritas (tinggi ke rendah), lalu nama.
2. Untuk tiap aturan, periksa apakah **semua anteseden** ada di working memory dan konsekuennya **belum** ada (agar tidak berulang tanpa akhir).
3. Jika terpenuhi, tambahkan konsekuen sebagai fakta baru dan catat ke jejak.
4. Karena fakta baru bisa membuka aturan lain, ulangi dari langkah 1.
5. Berhenti ketika satu putaran penuh tidak menjalankan aturan apa pun (kondisi *fixed point*).

Karena tiap aturan hanya dijalankan paling banyak sekali, proses ini selalu berhenti.

---

## 8. Cara Menjalankan

**Kebutuhan:** Python 3.7 atau lebih baru. Tidak perlu menginstal library apa pun.

```bash
python main.py
```

Jawab setiap pertanyaan dengan `y` (ya) atau `t` (tidak). Untuk pertanyaan anggaran dan sistem operasi, sistem hanya menanyakan opsi berikutnya jika jawaban sebelumnya `t`.

---

## 9. Contoh Eksekusi

Jawaban: portabilitas `y`, baterai `y`, anggaran tinggi `y`, Windows `y`, game `t`, kreatif `t`, kantor saja `t`, akselerasi AI `t`, layar besar `t`, sering bepergian `y`.

```
=== SISTEM PAKAR REKOMENDASI LAPTOP ===
Jawab dengan y (ya) atau t (tidak)

Apakah portabilitas penting? (y/t): y
Apakah butuh baterai yang awet? (y/t): y
Apakah anggaran Anda tinggi? (y/t): y
Apakah Anda lebih suka Windows? (y/t): y
Apakah Anda bermain game? (y/t): t
Apakah Anda melakukan pekerjaan kreatif? (y/t): t
Apakah untuk tugas kantor saja? (y/t): t
Apakah butuh akselerasi AI? (y/t): t
Apakah ingin layar yang besar? (y/t): t
Apakah Anda sering bepergian? (y/t): y

> Rekomendasi: ultrabook_premium
> Penjelasan : diturunkan dari aturan 'Ultrabook Premium'

> Spesifikasi: baterai_minimal_60wh
> Penjelasan : diturunkan dari aturan 'Spesifikasi Baterai'

> Spesifikasi: bobot_di_bawah_1_5_kg
> Penjelasan : diturunkan dari aturan 'Spesifikasi Bobot Ringan'

--- Jejak penalaran (urutan aturan yang dijalankan) ---
1. [Butuh Bobot Ringan] JIKA sering_bepergian DAN portabel MAKA butuh_ringan
2. [Ultrabook Premium] JIKA portabel DAN baterai_awet DAN anggaran_tinggi MAKA rekomendasi:ultrabook_premium
3. [Spesifikasi Baterai] JIKA baterai_awet MAKA spesifikasi:baterai_minimal_60wh
4. [Spesifikasi Bobot Ringan] JIKA butuh_ringan MAKA spesifikasi:bobot_di_bawah_1_5_kg
```

Perhatikan bahwa aturan 1 pada jejak (prioritas 9) dijalankan paling awal, dan fakta antara `butuh_ringan` yang dihasilkannya baru dipakai pada langkah 4.

---

## 10. Cara Menambah Aturan

Tambahkan satu baris baru pada list `ATURAN_LAPTOP` di `main.py`:

```python
Aturan(["hanya_kantor", "layar_besar", "anggaran_sedang"],
       "rekomendasi:laptop_kantor_layar_besar", 3, "Kantor Layar Besar"),
```

Format: `Aturan([daftar_kondisi], "konsekuen", prioritas, "nama aturan")`.

Kalau ingin menambah pertanyaan baru, tambahkan juga pemeriksaan di fungsi `kumpulkan_fakta_awal()` yang menambahkan fakta barunya, misalnya `fakta.append("butuh_port_lengkap")`.

---

## 11. Kelebihan dan Keterbatasan

**Kelebihan**
- Keputusan **transparan dan dapat dijelaskan** lewat jejak penalaran.
- Pengetahuan mudah ditambah atau diubah tanpa mengubah mesin inferensi.
- Ringan, tidak butuh data latih maupun library eksternal.
- Aturan berantai memungkinkan penalaran bertahap.

**Keterbatasan**
- Pengetahuan harus ditulis manual oleh manusia dan terbatas pada aturan yang ada.
- Tidak menangani ketidakpastian: fakta hanya bernilai benar atau tidak ada.
- Tidak belajar dari pengalaman atau data baru.
- Tidak ada resolusi konflik canggih. Jika beberapa rekomendasi terpenuhi sekaligus, semuanya ditampilkan.
- Jika jawaban tidak cocok dengan aturan mana pun, sistem tidak memberi rekomendasi.

---

## 12. Pengembangan Lanjutan

- **Certainty Factor**: memberi bobot keyakinan pada fakta dan aturan agar sistem bisa menangani ketidakpastian.
- **Backward chaining**: mode verifikasi hipotesis, misalnya "apakah laptop X cocok untuk saya?".
- **Resolusi konflik**: memilih satu rekomendasi terbaik berdasarkan skor atau spesifisitas aturan.
- **Basis pengetahuan eksternal**: memuat aturan dari file JSON atau database.
- **Antarmuka**: GUI (Tkinter) atau web (Flask/Streamlit).
- **Fasilitas penjelasan "Mengapa"**: menjelaskan alasan sebuah pertanyaan diajukan.
- **Pengujian otomatis**: unit test untuk setiap aturan.

---

## 13. Referensi

- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*. Pearson.
- Giarratano, J. & Riley, G. *Expert Systems: Principles and Programming*. Course Technology.
- Template tugas: [vwang99/429assignment4](https://github.com/vwang99/429assignment4) (GitHub).
- Library expert system Python sebagai pembanding: [Experta](https://github.com/nilp0inter/experta).
