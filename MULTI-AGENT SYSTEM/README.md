# Multi-Agent System (MAS): Konsep & Contoh Implementasi Python

Repositori ini berisi contoh sederhana **Multi-Agent System** dengan Python murni (tanpa library tambahan), beserta penjelasan konsepnya.

## Daftar Isi

1. [Apa itu Multi-Agent System?](#1-apa-itu-multi-agent-system)
2. [Bagaimana cara kerjanya?](#2-bagaimana-cara-kerjanya)
3. [Implementasi di dunia nyata](#3-implementasi-di-dunia-nyata)
4. [Bagaimana cara mengimplementasikannya?](#4-bagaimana-cara-mengimplementasikannya)
5. [Penjelasan kode `multi_agent_simple.py`](#5-penjelasan-kode-multi_agent_simplepy)
6. [Cara menjalankan](#6-cara-menjalankan)
7. [Ide pengembangan](#7-ide-pengembangan)

---

## 1. Apa itu Multi-Agent System?

**Agent** adalah entitas (program, robot, atau model AI) yang bisa:

- **Mengamati** lingkungannya (*perceive*),
- **Mengambil keputusan** (*decide*),
- **Bertindak** untuk mencapai tujuannya (*act*).

**Multi-Agent System (MAS)** adalah sistem yang terdiri dari **banyak agent** yang saling berinteraksi di dalam lingkungan yang sama untuk menyelesaikan masalah. Satu agent saja sering tidak cukup. Masalah yang besar dipecah menjadi bagian-bagian kecil, lalu dikerjakan oleh agent yang berbeda.

Analogi mudahnya adalah **tim di perusahaan**. Ada peneliti, penulis, dan editor, dan masing-masing punya keahlian serta tugas sendiri. Hasil akhirnya bagus karena mereka berkolaborasi, bukan karena satu orang mengerjakan semuanya.

### Ciri-ciri agent

| Ciri | Arti |
|---|---|
| **Otonom** | Bisa bekerja sendiri tanpa dikendalikan manusia setiap saat. |
| **Reaktif** | Merespons perubahan di lingkungannya atau pesan dari agent lain. |
| **Proaktif** | Tidak hanya menunggu, tetapi mengejar tujuannya. |
| **Sosial** | Berkomunikasi, berkoordinasi, atau bernegosiasi dengan agent lain. |

### Single-agent vs Multi-agent

| | Single Agent | Multi-Agent |
|---|---|---|
| Struktur | Satu "otak" mengerjakan semuanya | Banyak agent dengan peran berbeda |
| Cocok untuk | Tugas sederhana dan terfokus | Tugas kompleks yang bisa dipecah |
| Kelebihan | Mudah dibuat dan di-debug | Spesialisasi, paralel, saling mengoreksi |
| Kekurangan | Kewalahan pada tugas besar | Koordinasi lebih rumit, biaya komunikasi |

---

## 2. Bagaimana cara kerjanya?

Setiap MAS punya empat elemen dasar.

```
          ┌──────────────── LINGKUNGAN (Environment) ────────────────┐
          │                                                          │
          │    ┌─────────┐   pesan   ┌─────────┐   pesan   ┌───────┐ │
          │    │ Agent A │◀─────────▶│ Agent B │◀─────────▶│Agent C│ │
          │    └─────────┘           └─────────┘           └───────┘ │
          │         ▲                     ▲                    ▲     │
          │         └──────── data/memori bersama ─────────────┘     │
          └──────────────────────────────────────────────────────────┘
```

### 2.1 Agent dengan peran jelas

Setiap agent punya tugas khusus. Misalnya Peneliti hanya mencari fakta, Penulis hanya menulis, dan Kritikus hanya menilai. Pembagian ini disebut **spesialisasi**.

### 2.2 Komunikasi

Agent bertukar informasi lewat **pesan**. Bentuknya bisa:

- **Pemanggilan langsung** (output satu agent menjadi input agent lain), seperti di contoh sederhana kita,
- **Message queue / message bus** (kotak surat bersama),
- **Shared memory / blackboard** (papan tulis bersama tempat semua agent menaruh dan membaca hasil kerja).

### 2.3 Koordinasi

Siapa mengerjakan apa, dan kapan? Ada beberapa pola umum:

| Pola | Cara kerja | Contoh |
|---|---|---|
| **Pipeline / berantai** | A → B → C, hasil mengalir ke agent berikutnya | Riset → Tulis → Edit |
| **Orchestrator (pusat)** | Satu agent "manajer" membagi tugas dan mengumpulkan hasil | Manajer proyek + tim |
| **Peer-to-peer** | Agent berunding langsung tanpa pemimpin | Kawanan drone |
| **Hierarkis** | Manajer → sub-manajer → pekerja | Perusahaan besar |
| **Debat / kompetisi** | Beberapa agent mengusulkan solusi, lalu dipilih yang terbaik | Voting atau debat antar-AI |

### 2.4 Feedback loop (umpan balik)

Salah satu kekuatan MAS adalah agent bisa **saling mengoreksi**. Satu agent membuat hasil, agent lain menilai, dan kalau belum bagus hasilnya dikembalikan untuk diperbaiki. Pola ini muncul di contoh kode kita.

```
   Pembuat ──hasil──▶ Penilai ──ok?──▶ Selesai
       ▲                 │
       └────saran────────┘ (jika ditolak)
```

---

## 3. Implementasi di dunia nyata

| Bidang | Contoh penerapan | Peran agent |
|---|---|---|
| **AI generatif / LLM** | Asisten coding, riset otomatis, customer service | Planner, coder, reviewer, tester, masing-masing berupa LLM dengan instruksi berbeda |
| **Robotika** | Kawanan drone, robot gudang (mis. armada robot pengangkut) | Setiap robot menjadi agent yang berkoordinasi menghindari tabrakan |
| **Lalu lintas** | Pengaturan lampu lalu lintas adaptif | Setiap persimpangan menjadi agent yang berbagi data kemacetan |
| **Keuangan** | Simulasi pasar, trading otomatis | Agent pembeli, penjual, dan pengawas risiko |
| **Game & simulasi** | NPC cerdas, simulasi kota atau epidemi | Setiap karakter atau warga menjadi agent |
| **Smart grid / energi** | Pembagian listrik antar rumah dan pembangkit | Agent konsumen dan produsen yang bernegosiasi |
| **Logistik** | Penjadwalan pengiriman dan rute | Agent kurir, gudang, dan pelanggan |

> **Contoh konkret di dunia LLM:** saat Anda meminta AI membuat aplikasi, di balik layar bisa ada beberapa agent: satu merencanakan, satu menulis kode, satu menjalankan tes, satu mereview. Hasilnya lebih andal daripada satu prompt tunggal.

---

## 4. Bagaimana cara mengimplementasikannya?

### 4.1 Langkah umum

1. **Pecah masalah** menjadi sub-tugas yang jelas.
2. **Tentukan peran** agent untuk tiap sub-tugas.
3. **Rancang komunikasi:** apa yang dikirim, ke siapa, dan dalam format apa.
4. **Pilih pola koordinasi** (pipeline, orchestrator, dan seterusnya).
5. **Tambahkan umpan balik dan batas** (maksimal ronde, timeout, retry) supaya sistem tidak berputar selamanya.
6. **Amati dan log** semua interaksi agar mudah di-debug.

### 4.2 Pilihan teknologi

| Kebutuhan | Pilihan |
|---|---|
| **Belajar konsep** | Python murni (seperti repo ini) |
| **Agent berbasis LLM** | LangGraph, AutoGen, CrewAI |
| **Simulasi berbasis agent** | Mesa (Python) |
| **MAS klasik / akademik** | SPADE (Python), JADE (Java) |
| **Eksekusi paralel** | `asyncio`, `threading`, atau message broker (Redis, RabbitMQ) |

---

## 5. Penjelasan kode `multi_agent_simple.py`

### 5.1 Gambaran besar

Tiga agent bekerja sama membuat artikel pendek tentang Python:

```
Peneliti ──(fakta)──▶ Penulis ──(draft)──▶ Kritikus
                         ▲                    │
                         └───(saran revisi)───┘
```

| Agent | Tugas | Input | Output |
|---|---|---|---|
| **Peneliti** | Mengumpulkan fakta tentang topik | Topik (`str`) | Daftar fakta (`list`) |
| **Penulis** | Menyusun dan merevisi draft | Fakta (+ saran revisi) | Draft artikel (`str`) |
| **Kritikus** | Menilai draft | Draft | `(disetujui: bool, saran: str)` |

### 5.2 Bagian-bagian kode

**a) Class dasar `Agent`**

```python
class Agent:
    def __init__(self, nama):
        self.nama = nama

    def bicara(self, teks):
        print(f"[{self.nama:<9}] {teks}")
        time.sleep(0.8)
```

Semua agent mewarisi class ini. Method `bicara()` mencetak aktivitas agent ke terminal dengan awalan `[Nama]`. `time.sleep(0.8)` hanya membuat tampilan terasa seperti agent sedang "berpikir".

**b) `Peneliti`: sumber informasi**

```python
class Peneliti(Agent):
    def kerja(self, topik):
        ...
        return fakta
```

Menerima topik dan mengembalikan daftar fakta. Di contoh ini faktanya ditulis langsung. Di sistem nyata, bagian ini bisa diganti dengan pencarian web atau panggilan ke LLM.

**c) `Penulis`: pembuat dan pereparasi draft**

```python
class Penulis(Agent):
    def kerja(self, fakta, saran=None):
        if saran is None:
            # draft pertama: gabungkan fakta
        else:
            # revisi: terapkan saran dari Kritikus
```

Method ini punya **dua mode** yang ditentukan oleh parameter `saran`:

- `saran is None`: menulis draft pertama (sengaja belum lengkap, tanpa kesimpulan),
- `saran` berisi teks: merevisi draft dengan menambahkan kesimpulan.

**d) `Kritikus`: penjaga kualitas**

```python
class Kritikus(Agent):
    def kerja(self, draft):
        if "Kesimpulan" not in draft:
            return False, "Tambahkan kesimpulan di akhir"
        return True, None
```

Aturan penilaiannya sederhana: draft harus mengandung kata *"Kesimpulan"*. Jika tidak, agent ini **menolak** dan memberi **saran**. Jika ya, draft **disetujui**.

**e) Fungsi `main()`: sang "koordinator"**

```python
fakta = peneliti.kerja("Bahasa Python")      # Langkah 1
draft = penulis.kerja(fakta)                 # Langkah 2

for ronde in range(1, 4):                    # Langkah 3: feedback loop
    disetujui, saran = kritikus.kerja(draft)
    if disetujui:
        break
    draft = penulis.kerja(fakta, saran)
```

Di sini terlihat pola **pipeline + feedback loop**:

1. Peneliti bekerja sekali.
2. Penulis membuat draft pertama.
3. Kritikus dan Penulis berbalas sampai draft disetujui. `range(1, 4)` membatasi maksimal **3 ronde**, supaya tidak terjadi loop tak berujung.

### 5.3 Contoh alur eksekusi

```
[Peneliti ] Mencari informasi tentang 'Bahasa Python'...
[Peneliti ] Ketemu 3 fakta. Kirim ke Penulis.
[Penulis  ] Menulis draft pertama...

--- Ronde review 1 ---
[Kritikus ] Memeriksa draft...
[Kritikus ] DITOLAK - belum ada kesimpulan.
[Penulis  ] Menerima saran: 'Tambahkan kesimpulan di akhir'. Merevisi draft...

--- Ronde review 2 ---
[Kritikus ] Memeriksa draft...
[Kritikus ] DISETUJUI - draft sudah bagus!
```

Ronde 1 ditolak karena draft awal sengaja dibuat kurang. Penulis memperbaikinya, dan di ronde 2 draft disetujui.

### 5.4 Konsep MAS yang terlihat di kode

| Konsep | Wujud di kode |
|---|---|
| **Spesialisasi peran** | Tiga class agent dengan method `kerja()` berbeda |
| **Komunikasi** | Return value satu agent menjadi argumen agent lain |
| **Koordinasi** | `main()` mengatur urutan kerja |
| **Feedback loop** | `for ronde ...` antara Kritikus dan Penulis |
| **Batas keamanan** | Maksimal 3 ronde |

### 5.5 Keterbatasan (disengaja demi kesederhanaan)

- Agent bekerja **berurutan**, belum paralel.
- Komunikasi lewat **pemanggilan fungsi langsung**, belum lewat message bus.
- Logika agent berupa **aturan tetap**, belum memakai LLM.

---

## 6. Cara menjalankan

Pastikan Python 3 sudah terpasang (`python --version`).

**Windows (PowerShell / CMD):**
```powershell
python multi_agent_simple.py
```
Jika `python` tidak dikenali, coba `py multi_agent_simple.py`.

**Linux / macOS:**
```bash
python3 multi_agent_simple.py
```

> **Catatan:** perintah `/usr/bin/env python3` hanya berlaku di Linux/macOS. Di Windows akan muncul error *"not recognized"*.

---

## 7. Ide pengembangan

Urutan belajar yang disarankan, dari mudah ke sulit:

1. **Ganti topik dan fakta:** ubah `Peneliti` agar membahas topik lain.
2. **Tambah aturan Kritikus:** misalnya artikel minimal 50 kata atau harus ada kata tertentu.
3. **Tambah agent baru:** misalnya `Penerjemah` yang menerjemahkan hasil akhir ke bahasa Inggris.
4. **Jalankan paralel:** pakai `asyncio` supaya beberapa Peneliti bekerja bersamaan.
5. **Pakai message bus:** ganti pemanggilan langsung dengan antrean pesan (`asyncio.Queue`).
6. **Sambungkan ke LLM:** isi method `kerja()` dengan panggilan ke API model bahasa, sehingga agent benar-benar "berpikir".

---

## Ringkasan

> **Multi-Agent System** = banyak agent dengan peran berbeda yang **berkomunikasi, berkoordinasi, dan saling mengoreksi** untuk menyelesaikan tugas yang terlalu besar bagi satu agent. Kode `multi_agent_simple.py` memperlihatkan inti idenya hanya dalam sekitar 90 baris: **peran → komunikasi → koordinasi → feedback loop**.
