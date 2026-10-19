# Expert System: Diagnosa Kerusakan Laptop

Proyek sederhana untuk memahami **expert system (sistem pakar)** lewat contoh nyata: program Python yang mendiagnosa kerusakan laptop berdasarkan gejala yang dijawab pengguna.

---

## Daftar Isi

1. [Apa itu Expert System?](#1-apa-itu-expert-system)
2. [Komponen Expert System](#2-komponen-expert-system)
3. [Cara Kerja Expert System](#3-cara-kerja-expert-system)
4. [Metode Penalaran: Forward vs Backward Chaining](#4-metode-penalaran-forward-vs-backward-chaining)
5. [Contoh Penerapan Expert System](#5-contoh-penerapan-expert-system)
6. [Kelebihan dan Kekurangan](#6-kelebihan-dan-kekurangan)
7. [Penjelasan Kode `expert_system_laptop.py`](#7-penjelasan-kode-expert_system_laptoppy)
8. [Cara Menjalankan](#8-cara-menjalankan)
9. [Contoh Simulasi](#9-contoh-simulasi)
10. [Cara Mengembangkan](#10-cara-mengembangkan)

---

## 1. Apa itu Expert System?

**Expert system (sistem pakar)** adalah program komputer yang meniru cara seorang **pakar** (ahli) dalam menyelesaikan masalah di bidang tertentu. Pengetahuan sang pakar ditulis dalam bentuk **aturan** (rules), lalu komputer memakai aturan tersebut untuk mengambil kesimpulan atau memberi rekomendasi.

Analogi sederhananya: bayangkan kamu datang ke teknisi laptop. Teknisi akan bertanya, "Laptopnya nyala nggak? Lampu charger hidup nggak?", lalu menyimpulkan, "Kemungkinan chargernya rusak." Expert system melakukan hal yang sama, tetapi dalam bentuk program.

Ciri khas expert system:

- Fokus pada **satu bidang** tertentu (misalnya kesehatan, otomotif, perangkat elektronik).
- Pengetahuannya **terpisah dari program utama**, sehingga mudah ditambah atau diubah.
- Bisa **menjelaskan alasan** di balik kesimpulannya (explanation facility).

---

## 2. Komponen Expert System

| Komponen | Fungsi | Di kode ini |
|---|---|---|
| **Knowledge Base** (basis pengetahuan) | Menyimpan pengetahuan pakar berupa aturan IF-THEN | List `ATURAN`, `PERTANYAAN`, `SOLUSI` |
| **Working Memory** (memori kerja) | Menyimpan fakta yang diketahui saat ini | Variabel `fakta` (berupa `set`) |
| **Inference Engine** (mesin inferensi) | "Otak" yang mencocokkan fakta dengan aturan untuk menarik kesimpulan | Fungsi `inference_engine()` |
| **User Interface** | Tempat pengguna menjawab pertanyaan dan melihat hasil | Fungsi `tanya_ya_tidak()` dan `main()` |
| **Explanation Facility** | Menjelaskan bagaimana kesimpulan didapat | Bagian "Penjelasan" di akhir `main()` |

---

## 3. Cara Kerja Expert System

Secara umum alurnya seperti ini:

```
   Pengguna menjawab pertanyaan
              |
              v
   Jawaban disimpan sebagai FAKTA
              |
              v
   Inference engine mencocokkan fakta
   dengan aturan di knowledge base
              |
              v
   Ada aturan yang cocok? --ya--> tambahkan kesimpulan sebagai fakta baru
              |                              |
              |                              v
              |                    ulangi pencocokan
              |
             tidak
              v
   Tampilkan kesimpulan + penjelasan
```

**Aturan** ditulis dalam bentuk:

```
JIKA  <kondisi 1> DAN <kondisi 2>
MAKA  <kesimpulan>
```

Contoh dari kode:

```
JIKA  laptop_tidak_menyala DAN lampu_charger_mati
MAKA  charger_bermasalah
```

---

## 4. Metode Penalaran: Forward vs Backward Chaining

Ada dua cara utama inference engine bekerja.

### Forward Chaining (dipakai di kode ini)

Mulai dari **fakta** yang sudah diketahui, lalu cari aturan yang cocok untuk menghasilkan kesimpulan. Cocok jika kita punya banyak data awal dan ingin tahu "apa kesimpulannya?"

```
Fakta -> Aturan -> Fakta baru -> Aturan -> ... -> Kesimpulan
```

### Backward Chaining

Mulai dari **dugaan kesimpulan (hipotesis)**, lalu dicek mundur apakah kondisi-kondisinya terpenuhi. Cocok jika kita ingin membuktikan satu dugaan tertentu, misalnya "benarkah ini overheat?"

```
Hipotesis -> Cari aturan yang menghasilkannya -> Cek kondisinya -> Tanya fakta yang kurang
```

| | Forward Chaining | Backward Chaining |
|---|---|---|
| Titik mulai | Fakta | Hipotesis/tujuan |
| Arah | Data ke kesimpulan | Kesimpulan ke data |
| Cocok untuk | Diagnosa, monitoring | Verifikasi, konsultasi terarah |

---

## 5. Contoh Penerapan Expert System

- **Kesehatan:** diagnosa awal penyakit berdasarkan gejala (contoh klasik: MYCIN untuk infeksi bakteri).
- **Otomotif:** menentukan kerusakan mobil atau motor dari gejala yang dirasakan.
- **Pertanian:** diagnosa hama dan penyakit tanaman.
- **Pendidikan:** rekomendasi jurusan atau gaya belajar.
- **Keuangan:** penilaian kelayakan kredit.
- **Teknologi:** troubleshooting komputer, jaringan, dan perangkat elektronik (seperti contoh di proyek ini).

---

## 6. Kelebihan dan Kekurangan

**Kelebihan**

- Pengetahuan pakar bisa disimpan dan dipakai berulang kali.
- Konsisten: input yang sama selalu menghasilkan jawaban yang sama.
- Bisa menjelaskan alasan kesimpulannya.
- Aturan mudah ditambah tanpa mengubah mesin inferensinya.

**Kekurangan**

- Hanya sepintar aturan yang dimasukkan. Kasus di luar aturan tidak bisa dijawab.
- Pengumpulan pengetahuan dari pakar memakan waktu.
- Tidak belajar sendiri seperti machine learning.
- Sulit menangani ketidakpastian jika hanya memakai aturan ya/tidak.

---

## 7. Penjelasan Kode `expert_system_laptop.py`

### 7.1 Knowledge Base

```python
ATURAN = [
    {
        "id": "R1",
        "jika": ["laptop_tidak_menyala", "lampu_charger_mati"],
        "maka": "charger_bermasalah",
    },
    ...
]
```

Setiap aturan punya tiga bagian:

- `id`: nama aturan (R1, R2, dst.) untuk keperluan penjelasan.
- `jika`: daftar kondisi yang **semuanya** harus terpenuhi.
- `maka`: kesimpulan jika semua kondisi terpenuhi.

Daftar aturan di kode ini:

| ID | JIKA | MAKA |
|---|---|---|
| R1 | laptop tidak menyala + lampu charger mati | charger bermasalah |
| R2 | laptop tidak menyala + lampu charger nyala | baterai atau motherboard bermasalah |
| R3 | laptop menyala + layar hitam + ada suara kipas | layar atau kabel layar bermasalah |
| R4 | laptop menyala + sangat lambat + HDD berbunyi | harddisk bermasalah |
| R5 | laptop menyala + sangat lambat + sering panas | overheat |
| R6 | overheat + kipas berisik | kipas kotor perlu dibersihkan |

Perhatikan **R5 dan R6**: kesimpulan R5 (`overheat`) dipakai sebagai kondisi di R6. Inilah yang disebut **chaining** (rantai penalaran).

Dua kamus lainnya:

- `PERTANYAAN`: pertanyaan yang diajukan ke pengguna untuk tiap gejala.
- `SOLUSI`: saran perbaikan untuk tiap kesimpulan akhir.

### 7.2 Working Memory

```python
fakta = set()
for kode, teks in PERTANYAAN.items():
    if tanya_ya_tidak(teks):
        fakta.add(kode)
```

Setiap pertanyaan yang dijawab **ya** akan dimasukkan ke `fakta`. Memakai `set` agar tidak ada fakta ganda dan pengecekan `in` cepat.

### 7.3 Inference Engine

```python
def inference_engine(fakta):
    riwayat = []
    ada_perubahan = True

    while ada_perubahan:
        ada_perubahan = False
        for aturan in ATURAN:
            kondisi_terpenuhi = all(k in fakta for k in aturan["jika"])
            if kondisi_terpenuhi and aturan["maka"] not in fakta:
                fakta.add(aturan["maka"])
                riwayat.append(aturan)
                ada_perubahan = True

    return fakta, riwayat
```

Langkah demi langkah:

1. `while ada_perubahan`: terus mengulang selama masih ada fakta baru yang dihasilkan.
2. `for aturan in ATURAN`: periksa setiap aturan satu per satu.
3. `all(k in fakta for k in aturan["jika"])`: cek apakah **semua** kondisi aturan ada di fakta.
4. `aturan["maka"] not in fakta`: pastikan kesimpulan belum pernah dihasilkan, agar tidak berulang tanpa henti.
5. Jika cocok, kesimpulan ditambahkan ke `fakta`, aturannya dicatat di `riwayat`, dan `ada_perubahan = True` supaya satu putaran lagi dijalankan (siapa tahu fakta baru itu memicu aturan lain).
6. Jika satu putaran penuh tidak menghasilkan apa-apa, perulangan berhenti.

### 7.4 Menampilkan Hasil

```python
kesimpulan = [a["maka"] for a in riwayat]
hasil_akhir = [k for k in kesimpulan if k in SOLUSI]
```

Semua kesimpulan yang dihasilkan diambil dari `riwayat`, lalu disaring dengan `SOLUSI` supaya hanya kesimpulan yang punya saran perbaikan yang ditampilkan. Jika kosong, program menyarankan konsultasi ke teknisi.

### 7.5 Explanation Facility

```python
for a in riwayat:
    kondisi = " DAN ".join(a["jika"])
    print(f"[{a['id']}] JIKA {kondisi}")
    print(f"       MAKA {a['maka']}")
```

Karena `riwayat` mencatat aturan yang terpakai, program bisa menjelaskan **kenapa** ia sampai pada kesimpulan tertentu. Ini pembeda utama expert system dari program tanya-jawab biasa.

---

## 8. Cara Menjalankan

Kebutuhan: **Python 3** (tidak perlu library tambahan).

```bash
python expert_system_laptop.py
```

Jawab setiap pertanyaan dengan `y` (ya) atau `t` (tidak).

---

## 9. Contoh Simulasi

**Jawaban pengguna** (selain yang tercantum dijawab `t`):

- Laptop bisa menyala: **y**
- Laptop sangat lambat: **y**
- Laptop sering panas: **y**
- Kipas sangat berisik: **y**

**Proses di inference engine:**

| Putaran | Aturan dicek | Hasil |
|---|---|---|
| 1 | R1 sampai R4 | Tidak cocok |
| 1 | R5 (menyala + lambat + panas) | **Cocok**, fakta baru: `overheat` |
| 1 | R6 (overheat + kipas berisik) | **Cocok**, fakta baru: `kipas_kotor_perlu_dibersihkan` |
| 2 | Semua aturan | Tidak ada fakta baru, selesai |

**Output program:**

```
Diagnosa : Overheat
Solusi   : Pastikan ventilasi tidak tertutup dan gunakan cooling pad.

Diagnosa : Kipas Kotor Perlu Dibersihkan
Solusi   : Bersihkan debu pada kipas dan ganti thermal paste.

--- Penjelasan (bagaimana sistem sampai ke kesimpulan) ---
[R5] JIKA laptop_menyala DAN sangat_lambat DAN sering_panas
       MAKA overheat
[R6] JIKA overheat DAN kipas_berisik
       MAKA kipas_kotor_perlu_dibersihkan
```

---

## 10. Cara Mengembangkan

**Menambah aturan baru.** Cukup tambahkan satu blok di `ATURAN`, lalu tambahkan pertanyaan di `PERTANYAAN` dan saran di `SOLUSI` jika perlu. Mesin inferensinya tidak perlu diubah:

```python
{
    "id": "R7",
    "jika": ["laptop_menyala", "baterai_cepat_habis"],
    "maka": "baterai_aus",
},
```

**Ide pengembangan lanjutan:**

- Hanya menanyakan pertanyaan yang relevan (misalnya, jika laptop menyala, tidak perlu menanyakan lampu charger).
- Menambahkan **backward chaining** untuk memverifikasi satu dugaan.
- Menambahkan **tingkat keyakinan** (certainty factor) agar tidak hanya ya/tidak.
- Membuat antarmuka GUI atau web (Tkinter, Flask, Streamlit).
- Memisahkan knowledge base ke file JSON supaya bisa diedit tanpa menyentuh kode.

**Keterbatasan kode saat ini:** semua pertanyaan diajukan berurutan, termasuk yang saling bertentangan (misalnya "laptop tidak menyala" dan "laptop menyala"). Ini sengaja dibuat sederhana agar mudah dipahami. Pada sistem sungguhan, pertanyaan akan disesuaikan dengan jawaban sebelumnya.

---

## Ringkasan

> Expert system = **pengetahuan pakar (aturan IF-THEN)** + **mesin penalaran** + **antarmuka**.
> Pengguna memberi fakta, mesin mencocokkan dengan aturan, lalu keluar kesimpulan beserta alasannya.
