# Multi-Agent System (MAS) pada Kecerdasan Buatan (AI)

Dokumentasi lengkap tentang **Multi-Agent System (MAS)**: apa itu, bagaimana cara kerjanya, arsitektur, komunikasi dan koordinasi antar agen, implementasi, hingga penerapannya di dunia nyata.

---

## Daftar Isi

1. [Pengantar](#1-pengantar)
2. [Konsep Dasar: Apa Itu Agen?](#2-konsep-dasar-apa-itu-agen)
3. [Apa Itu Multi-Agent System?](#3-apa-itu-multi-agent-system)
4. [Karakteristik MAS](#4-karakteristik-mas)
5. [Jenis-Jenis Agen](#5-jenis-jenis-agen)
6. [Arsitektur Internal Agen](#6-arsitektur-internal-agen)
7. [Arsitektur Organisasi MAS](#7-arsitektur-organisasi-mas)
8. [Cara Kerja MAS](#8-cara-kerja-mas)
9. [Komunikasi Antar Agen](#9-komunikasi-antar-agen)
10. [Koordinasi, Kolaborasi, dan Negosiasi](#10-koordinasi-kolaborasi-dan-negosiasi)
11. [Pembelajaran pada MAS (MARL)](#11-pembelajaran-pada-mas-marl)
12. [Penerapan MAS](#12-penerapan-mas)
13. [Implementasi](#13-implementasi)
14. [Contoh Kode Python](#14-contoh-kode-python)
15. [MAS Berbasis LLM](#15-mas-berbasis-llm)
16. [Kelebihan dan Tantangan](#16-kelebihan-dan-tantangan)
17. [Evaluasi Kinerja MAS](#17-evaluasi-kinerja-mas)
18. [MAS vs Pendekatan Lain](#18-mas-vs-pendekatan-lain)
19. [Praktik Terbaik](#19-praktik-terbaik)
20. [Glosarium](#20-glosarium)
21. [Referensi dan Bacaan Lanjut](#21-referensi-dan-bacaan-lanjut)

---

## 1. Pengantar

Banyak masalah dunia nyata terlalu besar, terlalu tersebar, atau terlalu dinamis untuk diselesaikan oleh satu program tunggal. Contohnya mengatur lalu lintas satu kota, menyeimbangkan pasokan dan permintaan listrik dari ribuan sumber, atau mengoordinasikan puluhan robot gudang.

**Multi-Agent System (MAS)** menjawab masalah ini dengan membagi pekerjaan ke banyak **agen cerdas** yang masing-masing punya kemampuan mengambil keputusan sendiri, lalu saling berinteraksi untuk mencapai tujuan individual maupun tujuan bersama.

---

## 2. Konsep Dasar: Apa Itu Agen?

**Agen** adalah entitas (perangkat lunak, robot, atau komponen sistem) yang berada dalam suatu **lingkungan**, dapat **mengamati** lingkungan tersebut lewat sensor/persepsi, dan **bertindak** terhadapnya lewat aktuator untuk mencapai tujuan tertentu.

```
          +------------------------------+
          |           AGEN               |
 Persepsi |   +----------------------+   |  Aksi
 -------->|   | Keputusan / Program  |   |-------->
          |   +----------------------+   |
          +------------------------------+
                      ^        |
                      |        v
          +------------------------------+
          |         LINGKUNGAN           |
          +------------------------------+
```

### Kerangka PEAS

Untuk mendeskripsikan sebuah agen, biasa dipakai kerangka **PEAS**:

| Komponen | Arti | Contoh (robot vacuum) |
|---|---|---|
| **P**erformance | Ukuran keberhasilan | Luas area bersih, waktu, baterai |
| **E**nvironment | Lingkungan | Ruangan, furnitur, debu |
| **A**ctuators | Alat bertindak | Roda, sikat, pengisap |
| **S**ensors | Alat mengamati | Kamera, sensor tabrakan, sensor tebing |

### Sifat Lingkungan

Lingkungan agen dapat dikategorikan berdasarkan:

- **Observable**: sepenuhnya atau sebagian dapat diamati
- **Deterministik vs stokastik**: hasil aksi pasti atau mengandung ketidakpastian
- **Episodik vs sekuensial**: keputusan berdiri sendiri atau saling memengaruhi
- **Statis vs dinamis**: lingkungan berubah atau tidak saat agen berpikir
- **Diskret vs kontinu**: jumlah keadaan terbatas atau tak terbatas
- **Agen tunggal vs multi-agen**: ada atau tidaknya agen lain yang memengaruhi

MAS beroperasi pada lingkungan **multi-agen**, yang umumnya **parsial-observable, dinamis, dan stokastik**.

---

## 3. Apa Itu Multi-Agent System?

**Multi-Agent System (MAS)** adalah sistem yang terdiri dari **beberapa agen otonom yang berinteraksi** dalam satu lingkungan bersama untuk menyelesaikan masalah yang sulit atau mustahil diselesaikan oleh satu agen sendirian.

Elemen utama sebuah MAS:

| Elemen | Penjelasan |
|---|---|
| **Agen** | Entitas otonom dengan tujuan, pengetahuan, dan kemampuan bertindak |
| **Lingkungan** | Ruang tempat agen berada dan bertindak (fisik atau virtual) |
| **Interaksi** | Komunikasi dan pengaruh antar agen |
| **Organisasi** | Struktur peran, hubungan, dan aturan antar agen |
| **Protokol** | Aturan komunikasi dan koordinasi |

---

## 4. Karakteristik MAS

1. **Otonomi**: tiap agen mengambil keputusan sendiri tanpa kendali langsung manusia atau agen lain.
2. **Pandangan lokal**: tidak ada agen yang punya gambaran global penuh.
3. **Desentralisasi**: tidak ada satu pengendali pusat (atau pengendali pusat dibatasi).
4. **Interaksi sosial**: agen berkomunikasi, bernegosiasi, dan berkoordinasi.
5. **Reaktivitas**: agen merespons perubahan lingkungan tepat waktu.
6. **Proaktivitas**: agen mengambil inisiatif demi tujuannya, bukan sekadar bereaksi.
7. **Kemampuan sosial**: agen mampu berinteraksi dengan agen lain.
8. **Heterogenitas** (opsional): agen bisa berbeda desain, tujuan, dan kemampuan.
9. **Emergensi**: perilaku kompleks tingkat sistem muncul dari interaksi sederhana antar agen.

---

## 5. Jenis-Jenis Agen

Berdasarkan cara mengambil keputusan:

| Jenis | Cara kerja | Kelebihan | Keterbatasan |
|---|---|---|---|
| **Simple reflex** | Aturan kondisi-aksi dari persepsi saat ini | Cepat, sederhana | Tidak punya memori, gagal di lingkungan parsial |
| **Model-based reflex** | Menyimpan model internal keadaan dunia | Bisa menangani observasi parsial | Model harus akurat |
| **Goal-based** | Memilih aksi yang mendekatkan ke tujuan | Fleksibel, bisa merencanakan | Perencanaan bisa mahal |
| **Utility-based** | Memaksimalkan fungsi utilitas | Mampu menimbang trade-off | Fungsi utilitas sulit dirancang |
| **Learning agent** | Belajar dari pengalaman | Beradaptasi | Butuh data dan waktu belajar |

Berdasarkan hubungan dengan agen lain:

- **Kooperatif**: bekerja menuju tujuan bersama.
- **Kompetitif / self-interested**: memaksimalkan keuntungan sendiri.
- **Campuran**: kerja sama pada sebagian hal, bersaing pada hal lain.

---

## 6. Arsitektur Internal Agen

### 6.1 Reaktif

Memetakan persepsi langsung ke aksi tanpa representasi simbolik atau perencanaan panjang. Contoh: **Subsumption Architecture** (Brooks), tempat perilaku disusun berlapis dan lapisan yang lebih rendah (misalnya menghindari tabrakan) dapat menimpa lapisan yang lebih tinggi.

- Cocok untuk respons cepat dan lingkungan dinamis
- Sulit untuk tugas yang butuh perencanaan jangka panjang

### 6.2 Deliberatif

Memiliki model simbolik dunia dan melakukan penalaran serta perencanaan sebelum bertindak.

- Mampu merencanakan tujuan kompleks
- Lambat jika lingkungan cepat berubah

### 6.3 BDI (Belief-Desire-Intention)

Model yang sangat populer, terinspirasi dari penalaran praktis manusia:

| Komponen | Arti |
|---|---|
| **Beliefs** | Apa yang dipercaya agen tentang dunia |
| **Desires** | Apa yang ingin dicapai agen |
| **Intentions** | Tujuan yang dipilih dan sedang dikejar agen |
| **Plans** | Rangkaian aksi untuk memenuhi intention |

Siklus BDI secara umum:

```
loop:
    perceive()          -> perbarui Beliefs
    options()           -> hasilkan Desires dari Beliefs & Intentions
    filter()            -> pilih Intentions dari Desires
    plan()              -> susun rencana untuk Intentions
    execute()           -> jalankan aksi
```

### 6.4 Hybrid / Berlapis (Layered)

Menggabungkan lapisan reaktif (cepat) dan deliberatif (terencana). Contoh: **TouringMachines**, **InteRRaP**.

```
+---------------------------+
| Lapisan Kooperatif (sosial)|   <- koordinasi dengan agen lain
+---------------------------+
| Lapisan Perencanaan        |   <- tujuan jangka menengah/panjang
+---------------------------+
| Lapisan Reaktif            |   <- respons cepat/refleks
+---------------------------+
```

---

## 7. Arsitektur Organisasi MAS

Bagaimana agen diatur satu sama lain:

| Struktur | Deskripsi | Contoh | Catatan |
|---|---|---|---|
| **Terpusat (centralized)** | Satu koordinator mengatur semua agen | Dispatcher armada taksi | Sederhana, tapi *single point of failure* |
| **Hierarkis** | Agen tersusun bertingkat (atasan-bawahan) | Struktur komando | Terstruktur, kurang fleksibel |
| **Heterarki / peer-to-peer** | Semua agen setara | Swarm robot | Tangguh, koordinasi lebih rumit |
| **Holonik** | Agen tersusun dari sub-agen (holon) secara rekursif | Manufaktur | Skalabel dan modular |
| **Koalisi** | Agen membentuk kelompok sementara | Tugas yang butuh kerja sama | Dinamis |
| **Tim** | Kelompok dengan tujuan bersama dan peran jelas | Tim robot sepak bola | Peran terdefinisi |
| **Pasar (market-based)** | Agen berdagang tugas/sumber daya lewat lelang | Alokasi tugas | Efisien, perlu desain mekanisme |
| **Blackboard** | Agen berbagi ruang pengetahuan bersama | Pengenalan suara/pola | Komunikasi tidak langsung |

---

## 8. Cara Kerja MAS

### 8.1 Siklus Umum Tiap Agen

```
        +-----------+
        |  Persepsi |  <- amati lingkungan & terima pesan
        +-----+-----+
              v
        +-----------+
        |  Update   |  <- perbarui keyakinan/model internal
        |  Keadaan  |
        +-----+-----+
              v
        +-----------+
        | Keputusan |  <- pilih tujuan & aksi (reaktif/deliberatif)
        +-----+-----+
              v
        +-----------+
        |   Aksi    |  <- ubah lingkungan / kirim pesan
        +-----+-----+
              |
              +----> kembali ke Persepsi
```

### 8.2 Alur Kerja Sistem Secara Keseluruhan

1. **Dekomposisi tugas**: masalah besar dipecah menjadi sub-tugas.
2. **Alokasi tugas**: sub-tugas diberikan ke agen yang sesuai (lewat penugasan, lelang, atau negosiasi).
3. **Eksekusi paralel**: tiap agen bekerja pada bagiannya secara bersamaan.
4. **Komunikasi dan koordinasi**: agen berbagi informasi, menyelaraskan rencana, dan menyelesaikan konflik.
5. **Sintesis hasil**: hasil tiap agen digabung menjadi solusi akhir.
6. **Adaptasi**: bila lingkungan atau agen berubah (misalnya ada agen gagal), tugas dialokasikan ulang.

### 8.3 Contoh Ilustrasi: Gudang Robot

```
Pesanan masuk
     |
     v
[Agen Penjadwal] --CFP--> [Robot A] [Robot B] [Robot C]
                              |         |         |
                          propose   propose   propose  (biaya/jarak masing-masing)
                              \         |         /
                               v        v        v
                          [Agen Penjadwal memilih terbaik]
                                       |
                                    accept --> Robot B mengambil barang
                                       |
                                    inform  <-- "selesai"
```

Pada saat yang sama, setiap robot menjalankan **agen penghindar tabrakan** (reaktif) yang berkoordinasi lokal dengan robot terdekat untuk menghindari kemacetan di lorong.

---

## 9. Komunikasi Antar Agen

### 9.1 Mode Komunikasi

| Mode | Penjelasan |
|---|---|
| **Langsung (message passing)** | Agen saling mengirim pesan eksplisit |
| **Tidak langsung (stigmergy)** | Agen berkomunikasi lewat perubahan lingkungan (misalnya jejak feromon semut) |
| **Blackboard / shared memory** | Agen membaca dan menulis di ruang bersama |
| **Broadcast / multicast** | Satu pesan dikirim ke banyak agen |

### 9.2 Teori Speech Act

Pesan antar agen dipandang sebagai **tindak tutur (speech act)**: tidak hanya membawa informasi tetapi juga **maksud (performative)**, misalnya meminta, memberi tahu, menawar, atau menolak.

### 9.3 FIPA-ACL

**FIPA-ACL** (Agent Communication Language dari *Foundation for Intelligent Physical Agents*) adalah standar komunikasi agen. Performative umum:

| Performative | Makna |
|---|---|
| `inform` | Memberi tahu suatu fakta |
| `request` | Meminta agen lain melakukan aksi |
| `query-if` / `query-ref` | Bertanya |
| `cfp` | *Call for proposal*, meminta penawaran |
| `propose` | Mengajukan penawaran |
| `accept-proposal` | Menerima penawaran |
| `reject-proposal` | Menolak penawaran |
| `agree` / `refuse` | Menyetujui / menolak permintaan |
| `failure` | Melaporkan kegagalan |

Contoh pesan (notasi S-expression ala FIPA-ACL):

```lisp
(request
  :sender   (agent-identifier :name penjadwal)
  :receiver (set (agent-identifier :name robot-b))
  :content  "((action robot-b (ambil-barang rak-12)))"
  :language fipa-sl
  :ontology gudang
  :protocol fipa-request
  :conversation-id order-0042)
```

### 9.4 Ontologi

Agen perlu **kosakata bersama** agar maksud pesan dipahami sama. Ontologi mendefinisikan konsep dan relasi yang disepakati (misalnya apa itu "rak", "lorong", "prioritas").

---

## 10. Koordinasi, Kolaborasi, dan Negosiasi

### 10.1 Contract Net Protocol (CNP)

Protokol alokasi tugas klasik:

1. **Manager** mengumumkan tugas (`cfp`).
2. **Contractor** yang mampu mengirim penawaran (`propose`).
3. Manager memilih penawaran terbaik (`accept-proposal`) dan menolak lainnya (`reject-proposal`).
4. Contractor terpilih mengerjakan dan melapor (`inform`).

### 10.2 Lelang (Auction)

| Jenis | Cara kerja |
|---|---|
| **English** | Harga naik terbuka hingga tersisa satu penawar |
| **Dutch** | Harga turun hingga ada yang menerima |
| **First-price sealed-bid** | Penawaran tertutup, pemenang membayar harganya sendiri |
| **Vickrey (second-price)** | Penawaran tertutup, pemenang membayar harga tertinggi kedua |

### 10.3 Voting dan Konsensus

Agen memilih keputusan bersama lewat pemungutan suara (mayoritas, Borda count, dll.) atau algoritma konsensus (misalnya *average consensus* pada jaringan sensor).

### 10.4 Negosiasi

Agen yang tujuannya berbeda mencari kesepakatan lewat tawar-menawar bergantian (*alternating offers*) dengan strategi konsesi. Dipelajari dengan teori permainan (*game theory*).

### 10.5 Koordinasi Terdistribusi

- **Distributed Constraint Optimization (DCOP)**: agen mengoptimalkan variabel lokal di bawah batasan bersama.
- **Perencanaan multi-agen**: rencana tiap agen disinkronkan agar tidak konflik.
- **Konvensi sosial dan norma**: aturan umum (misalnya "kendaraan dari kiri didahulukan") mengurangi kebutuhan negosiasi.

### 10.6 Stigmergy dan Swarm Intelligence

Agen sederhana meninggalkan tanda di lingkungan, dan agen lain bereaksi terhadapnya. Contoh algoritma: **Ant Colony Optimization (ACO)** dan **Particle Swarm Optimization (PSO)**.

### 10.7 Konflik dan Resolusi

Konflik dapat berupa rebutan sumber daya, tujuan bertentangan, atau informasi tidak konsisten. Cara penyelesaian: prioritas/peran, negosiasi, mediator, voting, atau pembagian waktu.

---

## 11. Pembelajaran pada MAS (MARL)

**Multi-Agent Reinforcement Learning (MARL)** melatih beberapa agen belajar lewat percobaan dan hadiah (*reward*).

### Tantangan Khusus

- **Non-stasioner**: lingkungan terus berubah karena agen lain ikut belajar.
- **Credit assignment**: sulit menentukan kontribusi tiap agen pada hadiah bersama.
- **Skalabilitas**: ruang keadaan-aksi gabungan tumbuh eksponensial.
- **Observasi parsial**: tiap agen hanya melihat sebagian dunia.

### Paradigma Pelatihan

| Paradigma | Pelatihan | Eksekusi |
|---|---|---|
| **Independent learners** | Tiap agen belajar sendiri | Terdesentralisasi |
| **Centralized training, decentralized execution (CTDE)** | Pelatihan memakai informasi global | Tiap agen hanya memakai observasi lokal |
| **Fully centralized** | Satu pengendali untuk semua | Terpusat |

Contoh algoritma: **QMIX**, **VDN**, **MADDPG**, **MAPPO**.

### Setting Hadiah

- **Kooperatif penuh**: satu hadiah bersama
- **Kompetitif (zero-sum)**: keuntungan satu agen adalah kerugian lainnya
- **Campuran (general-sum)**: kombinasi keduanya

---

## 12. Penerapan MAS

### 12.1 Energi dan Kelistrikan

- **Smart grid**: agen mewakili pembangkit, beban, baterai, dan kendaraan listrik untuk menyeimbangkan pasokan-permintaan.
- **Microgrid**: pengelolaan sumber energi terdistribusi (surya, angin, baterai).
- **Demand response**: pengaturan konsumsi listrik pelanggan.
- **Pemulihan jaringan (self-healing)** setelah gangguan.

### 12.2 Transportasi dan Logistik

- Pengaturan lampu lalu lintas adaptif
- Manajemen armada taksi dan pengiriman
- Kendaraan otonom yang berkoordinasi (*platooning*, persimpangan)
- Lalu lintas udara dan drone

### 12.3 Robotika

- **Swarm robotics**: pencarian dan penyelamatan, pemetaan, pertanian presisi
- **Robot gudang**: koordinasi pengambilan barang
- **Robot sepak bola** (RoboCup)

### 12.4 Manufaktur dan Industri

- Penjadwalan produksi terdistribusi
- Holonic manufacturing
- Pemeliharaan prediktif dengan agen pada tiap mesin

### 12.5 Keuangan dan Ekonomi

- Simulasi pasar (*agent-based computational economics*)
- Trading algoritmik
- Mekanisme lelang dan negosiasi otomatis

### 12.6 Kesehatan

- Penjadwalan pasien dan sumber daya rumah sakit
- Pemantauan pasien terdistribusi
- Simulasi penyebaran penyakit berbasis agen

### 12.7 Telekomunikasi dan Jaringan

- Manajemen jaringan sensor nirkabel
- Alokasi spektrum dan routing
- Keamanan siber (agen deteksi dan respons terdistribusi)

### 12.8 Game dan Simulasi

- NPC dengan perilaku mandiri
- Simulasi kerumunan dan evakuasi
- Simulasi sosial dan perkotaan

### 12.9 Sistem Berbasis LLM

- Asisten pengembangan perangkat lunak (agen perencana, penulis kode, penguji)
- Riset otomatis dan analisis dokumen
- Layanan pelanggan dengan agen terspesialisasi

### 12.10 Militer dan Kebencanaan

- Simulasi dan perencanaan misi
- Koordinasi tim tanggap darurat

---

## 13. Implementasi

### 13.1 Langkah Merancang MAS

1. **Definisikan masalah dan tujuan sistem.**
2. **Identifikasi agen dan peran**: siapa yang menjadi agen, apa tanggung jawabnya.
3. **Rancang lingkungan**: apa yang bisa diamati dan diubah.
4. **Pilih arsitektur agen**: reaktif, BDI, hybrid, atau berbasis pembelajaran.
5. **Tentukan organisasi**: terpusat, hierarkis, atau peer-to-peer.
6. **Rancang komunikasi**: format pesan, protokol, ontologi.
7. **Pilih mekanisme koordinasi**: CNP, lelang, voting, dsb.
8. **Implementasi dan simulasi**.
9. **Evaluasi dan iterasi.**

### 13.2 Framework dan Pustaka

| Kategori | Alat | Bahasa | Keterangan |
|---|---|---|---|
| **Platform agen klasik** | **JADE** | Java | Mengikuti standar FIPA |
| | **SPADE** | Python | Agen berbasis XMPP dan asyncio |
| | **Jason** | AgentSpeak (Java) | Agen BDI |
| | **JaCaMo** | Java | Agen, lingkungan, dan organisasi |
| | **GAMA** | GAML | Simulasi berbasis agen spasial |
| **Simulasi berbasis agen** | **Mesa** | Python | Pemodelan agen dan visualisasi |
| | **NetLogo** | NetLogo | Populer untuk edukasi dan riset |
| | **Repast** | Java/Python | Simulasi skala besar |
| **MARL** | **PettingZoo** | Python | API lingkungan multi-agen |
| | **RLlib (Ray)** | Python | Pelatihan MARL terdistribusi |
| | **PyMARL / EPyMARL** | Python | Implementasi algoritma MARL |
| **LLM multi-agen** | **LangGraph** | Python | Alur agen berbasis graf |
| | **AutoGen** | Python | Percakapan multi-agen |
| | **CrewAI** | Python | Agen berbasis peran |
| **Robotika** | **ROS / ROS 2** | C++/Python | Komunikasi antar node robot |

> Fitur dan API framework terus berubah. Selalu rujuk dokumentasi resmi versi terbaru sebelum dipakai.

### 13.3 Pola Desain Umum

- **Agen + Message Bus**: semua pesan lewat perantara (broker).
- **Agen + Blackboard**: agen membaca dan menulis ke penyimpanan bersama.
- **Supervisor-Worker**: satu agen pengatur membagi tugas ke agen pekerja.
- **Pipeline**: agen disusun berurutan, keluaran satu menjadi masukan berikutnya.
- **Debate / Critic**: beberapa agen mengusulkan jawaban dan agen lain mengkritik.

---

## 14. Contoh Kode Python

Contoh berikut mensimulasikan **Contract Net Protocol** menggunakan `asyncio` murni (tanpa pustaka tambahan): satu `Manager` membagikan tugas ke beberapa `Worker` lewat lelang biaya.

Simpan sebagai `contract_net.py` dan jalankan dengan `python contract_net.py`.

```python
import asyncio
import random
from dataclasses import dataclass
from typing import Any


@dataclass
class Message:
    performative: str   # cfp, propose, accept, reject, inform, stop
    sender: str
    receiver: str
    content: Any = None


class Bus:
    """Perantara pesan sederhana antar agen."""

    def __init__(self):
        self.agents = {}

    def register(self, agent):
        self.agents[agent.name] = agent

    async def send(self, msg: Message):
        await self.agents[msg.receiver].inbox.put(msg)


class Agent:
    def __init__(self, name: str, bus: Bus):
        self.name = name
        self.bus = bus
        self.inbox: asyncio.Queue = asyncio.Queue()
        bus.register(self)

    async def send(self, receiver: str, performative: str, content: Any = None):
        await self.bus.send(Message(performative, self.name, receiver, content))


class Worker(Agent):
    """Contractor: memberi penawaran sesuai bebannya, lalu mengerjakan tugas."""

    def __init__(self, name: str, bus: Bus):
        super().__init__(name, bus)
        self.load = random.randint(0, 3)

    async def run(self):
        while True:
            msg = await self.inbox.get()

            if msg.performative == "cfp":
                # Semakin sibuk, semakin mahal penawarannya
                cost = self.load + random.random()
                await self.send(msg.sender, "propose",
                                {"task": msg.content, "cost": cost})

            elif msg.performative == "accept":
                await asyncio.sleep(0.1)          # simulasi mengerjakan tugas
                self.load += 1
                await self.send(msg.sender, "inform",
                                {"task": msg.content, "status": "selesai"})

            elif msg.performative == "reject":
                pass                              # penawaran tidak dipilih

            elif msg.performative == "stop":
                return


class Manager(Agent):
    """Initiator: mengumumkan tugas, memilih penawaran terbaik, memantau hasil."""

    def __init__(self, name: str, bus: Bus, worker_names: list):
        super().__init__(name, bus)
        self.workers = worker_names

    async def assign(self, task: str):
        # 1. Umumkan tugas ke semua worker (call for proposal)
        for w in self.workers:
            await self.send(w, "cfp", task)

        # 2. Kumpulkan penawaran
        proposals = []
        for _ in self.workers:
            proposals.append(await self.inbox.get())

        # 3. Pilih biaya terendah
        best = min(proposals, key=lambda m: m.content["cost"])
        print(f"[{self.name}] '{task}' -> {best.sender} "
              f"(biaya {best.content['cost']:.2f})")

        # 4. Kirim accept ke pemenang, reject ke lainnya
        for p in proposals:
            performative = "accept" if p is best else "reject"
            await self.send(p.sender, performative, task)

        # 5. Tunggu laporan penyelesaian
        report = await self.inbox.get()
        print(f"[{self.name}] laporan dari {report.sender}: "
              f"{report.content['task']} {report.content['status']}")


async def main():
    random.seed(42)
    bus = Bus()
    workers = [Worker(f"robot-{i}", bus) for i in range(1, 4)]
    manager = Manager("penjadwal", bus, [w.name for w in workers])

    worker_tasks = [asyncio.create_task(w.run()) for w in workers]

    for task in ["ambil-rak-1", "ambil-rak-2", "ambil-rak-3", "ambil-rak-4"]:
        await manager.assign(task)

    # Hentikan semua worker
    for w in workers:
        await manager.send(w.name, "stop")
    await asyncio.gather(*worker_tasks)


if __name__ == "__main__":
    asyncio.run(main())
```

### Penjelasan Singkat Kode

| Bagian | Peran |
|---|---|
| `Message` | Struktur pesan dengan `performative` (maksud pesan) |
| `Bus` | Menyampaikan pesan antar agen |
| `Worker` | Agen yang menawar tugas berdasarkan bebannya, lalu mengerjakannya |
| `Manager` | Agen yang mengumumkan tugas dan memilih pemenang |
| `asyncio` | Menjalankan semua agen secara konkuren |

### Ide Pengembangan

- Tambahkan **timeout** jika worker tidak merespons.
- Tambahkan **kegagalan worker** dan alokasi ulang tugas.
- Ganti fungsi biaya dengan **jarak tempuh** pada grid 2D.
- Visualisasikan dengan **Mesa** atau **matplotlib**.

---

## 15. MAS Berbasis LLM

Dengan hadirnya *Large Language Model*, muncul gaya MAS baru: tiap agen adalah LLM dengan **peran (system prompt)**, **alat (tools)**, dan **memori** sendiri.

### 15.1 Pola Umum

```
              +------------------+
   Tugas ---> |   Orchestrator   |  (agen perencana/supervisor)
              +--------+---------+
                       |  membagi sub-tugas
        +--------------+--------------+
        v              v              v
   [Agen Riset]   [Agen Penulis]  [Agen Pemeriksa]
        |              |              |
     tools:         tools:         tools:
     web search     editor         linter/tes
        \              |              /
         +-------> hasil digabung <---+
```

### 15.2 Kerangka Pseudo-code

```python
def call_llm(system_prompt: str, messages: list) -> str:
    """Ganti dengan pemanggilan API LLM pilihan Anda."""
    raise NotImplementedError

class LLMAgent:
    def __init__(self, name, role_prompt, tools=None):
        self.name = name
        self.role_prompt = role_prompt
        self.tools = tools or {}
        self.memory = []

    def act(self, incoming_message: str) -> str:
        self.memory.append({"role": "user", "content": incoming_message})
        reply = call_llm(self.role_prompt, self.memory)
        self.memory.append({"role": "assistant", "content": reply})
        return reply

planner  = LLMAgent("planner",  "Kamu perencana. Pecah tugas menjadi langkah-langkah.")
coder    = LLMAgent("coder",    "Kamu programmer. Tulis kode sesuai langkah.")
reviewer = LLMAgent("reviewer", "Kamu reviewer. Cari bug dan beri masukan.")

task  = "Buat fungsi untuk menghitung rata-rata dari daftar angka."
plan  = planner.act(task)
code  = coder.act(plan)
check = reviewer.act(code)
final = coder.act("Perbaiki berdasarkan review berikut:\n" + check)
```

### 15.3 Pola Kolaborasi LLM

| Pola | Penjelasan |
|---|---|
| **Supervisor-Worker** | Satu agen mendelegasikan ke agen spesialis |
| **Sequential / Pipeline** | Agen bekerja berurutan |
| **Debate** | Beberapa agen berargumen, lalu hasil disintesis |
| **Reflection / Critic** | Satu agen membuat, agen lain mengkritik |
| **Group chat** | Agen berdiskusi dalam satu percakapan bersama |
| **Hierarkis** | Supervisor memiliki sub-supervisor |

### 15.4 Hal yang Perlu Diwaspadai

- **Biaya dan latensi** bertambah seiring jumlah panggilan LLM.
- **Halusinasi berantai**: kesalahan satu agen bisa menyebar ke agen lain.
- **Loop tak berujung**: perlu batas iterasi dan kondisi berhenti.
- **Keamanan**: *prompt injection* pada konten yang dibaca agen, serta batas izin penggunaan alat.
- **Observabilitas**: catat semua pesan dan keputusan agar mudah di-*debug*.
- Tidak semua tugas butuh multi-agen. Agen tunggal dengan alat yang baik sering sudah cukup.

---

## 16. Kelebihan dan Tantangan

### Kelebihan

| Kelebihan | Penjelasan |
|---|---|
| **Skalabilitas** | Menambah agen untuk menangani beban lebih besar |
| **Ketahanan** | Kegagalan satu agen tidak mematikan seluruh sistem |
| **Paralelisme** | Tugas dikerjakan bersamaan, lebih cepat |
| **Modularitas** | Agen dapat dikembangkan dan diganti secara terpisah |
| **Fleksibilitas** | Mudah beradaptasi dengan perubahan lingkungan |
| **Distribusi alami** | Cocok untuk masalah yang memang tersebar (geografis, organisasi) |
| **Spesialisasi** | Tiap agen fokus pada keahliannya |

### Tantangan

| Tantangan | Penjelasan |
|---|---|
| **Koordinasi rumit** | Menyelaraskan banyak agen tidak sepele |
| **Overhead komunikasi** | Pesan berlebih dapat membebani jaringan dan waktu |
| **Konflik tujuan** | Agen self-interested dapat merugikan sistem |
| **Perilaku emergen** | Sulit diprediksi dan diverifikasi |
| **Debugging sulit** | Perilaku terdistribusi dan non-deterministik |
| **Kepercayaan dan keamanan** | Agen berbahaya atau salah fungsi dapat merusak sistem |
| **Standarisasi** | Interoperabilitas antar platform masih terbatas |
| **Non-stasioneritas (MARL)** | Lingkungan berubah karena agen lain juga belajar |

---

## 17. Evaluasi Kinerja MAS

| Aspek | Contoh Metrik |
|---|---|
| **Kualitas solusi** | Total reward, utilitas sosial, tingkat keberhasilan tugas |
| **Efisiensi** | Waktu penyelesaian (*makespan*), throughput |
| **Komunikasi** | Jumlah dan ukuran pesan, bandwidth |
| **Skalabilitas** | Perubahan kinerja saat jumlah agen bertambah |
| **Ketahanan** | Penurunan kinerja saat agen gagal |
| **Keadilan** | Pemerataan beban atau hasil antar agen |
| **Stabilitas** | Konvergensi, ada tidaknya osilasi |
| **Biaya** | Komputasi, energi, panggilan API (untuk LLM) |

Metode evaluasi: simulasi berulang dengan *seed* berbeda, perbandingan dengan *baseline* (agen tunggal atau terpusat), uji ketahanan (*fault injection*), dan analisis sensitivitas parameter.

---

## 18. MAS vs Pendekatan Lain

| Aspek | Agen Tunggal | MAS | Sistem Terdistribusi Biasa | Ensemble ML |
|---|---|---|---|---|
| Otonomi pengambilan keputusan | Satu agen | Banyak agen otonom | Umumnya node mengikuti perintah | Model tidak otonom |
| Kontrol | Terpusat | Terdesentralisasi | Bervariasi | Terpusat (penggabung) |
| Tujuan | Satu | Individual dan/atau bersama | Satu tujuan sistem | Satu prediksi |
| Interaksi | Dengan lingkungan | Dengan lingkungan dan antar agen | Antar proses | Minimal |
| Fokus | Keputusan optimal | Koordinasi, negosiasi | Konsistensi, ketersediaan | Akurasi prediksi |

---

## 19. Praktik Terbaik

1. **Mulai sederhana**: coba agen tunggal atau dua agen sebelum membangun sistem besar.
2. **Definisikan peran dengan jelas** agar tanggung jawab tidak tumpang tindih.
3. **Batasi komunikasi** hanya pada yang perlu untuk menekan overhead.
4. **Gunakan protokol standar** (misalnya CNP, FIPA) bila memungkinkan.
5. **Rancang untuk kegagalan**: timeout, retry, dan alokasi ulang tugas.
6. **Simulasikan dahulu** sebelum penerapan di dunia nyata.
7. **Log semua interaksi** untuk analisis dan debugging.
8. **Atur batas keamanan**: izin tiap agen, validasi pesan, dan pembatasan aksi berisiko.
9. **Ukur terhadap baseline** untuk memastikan multi-agen memang memberi nilai tambah.
10. **Libatkan manusia** pada keputusan berdampak tinggi (*human-in-the-loop*).

---

## 20. Glosarium

| Istilah | Arti |
|---|---|
| **Agen** | Entitas otonom yang mengamati dan bertindak di lingkungan |
| **MAS** | Multi-Agent System, sistem banyak agen yang berinteraksi |
| **BDI** | Belief-Desire-Intention, model penalaran agen |
| **FIPA-ACL** | Standar bahasa komunikasi antar agen |
| **Performative** | Jenis maksud sebuah pesan (inform, request, dll.) |
| **Ontologi** | Kosakata dan konsep bersama antar agen |
| **CNP** | Contract Net Protocol, protokol alokasi tugas |
| **DCOP** | Distributed Constraint Optimization Problem |
| **MARL** | Multi-Agent Reinforcement Learning |
| **CTDE** | Centralized Training, Decentralized Execution |
| **Stigmergy** | Koordinasi tidak langsung lewat perubahan lingkungan |
| **Swarm intelligence** | Perilaku cerdas kolektif dari agen sederhana |
| **Emergent behavior** | Perilaku tingkat sistem yang muncul dari interaksi antar agen |
| **Blackboard** | Ruang pengetahuan bersama antar agen |
| **Holon** | Entitas yang sekaligus bagian dan keseluruhan |
| **Nash equilibrium** | Kondisi tempat tak ada agen yang untung bila mengubah strategi sendiri |
| **Human-in-the-loop** | Manusia terlibat dalam pengambilan keputusan sistem |

---

## 21. Referensi dan Bacaan Lanjut

**Buku**

- Michael Wooldridge, *An Introduction to MultiAgent Systems*
- Stuart Russell dan Peter Norvig, *Artificial Intelligence: A Modern Approach*
- Yoav Shoham dan Kevin Leyton-Brown, *Multiagent Systems: Algorithmic, Game-Theoretic, and Logical Foundations*
- Gerhard Weiss (ed.), *Multiagent Systems: A Modern Approach to Distributed Artificial Intelligence*

**Standar dan Spesifikasi**

- FIPA (Foundation for Intelligent Physical Agents): spesifikasi ACL dan protokol interaksi

**Topik Lanjutan untuk Dipelajari**

- Teori permainan (*game theory*) dan *mechanism design*
- Multi-Agent Path Finding (MAPF)
- Distributed Constraint Optimization (DCOP)
- MARL: QMIX, MADDPG, MAPPO
- Agent-Based Modeling dan simulasi sosial
- Keamanan dan keselamatan MAS (*trust*, *reputation*, *robustness*)

---

## Lisensi

Dokumen ini bebas digunakan untuk keperluan belajar dan dokumentasi. Silakan ubah sesuai kebutuhan.
