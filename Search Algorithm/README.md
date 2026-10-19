# Visualisasi Search Algorithm (BFS & DFS) pada Grid / Maze

Aplikasi desktop berbasis **Python + Tkinter** untuk memvisualisasikan cara kerja algoritma pencarian (*search algorithm*) **Breadth-First Search (BFS)** dan **Depth-First Search (DFS)** pada sebuah grid/maze secara animasi.

**Penulis:** Moh. Fathirochman Yasin (NIM 101022400093) - S1 Teknik Elektro, Telkom University

---

## Daftar Isi

1. [Apa itu Search Algorithm?](#1-apa-itu-search-algorithm)
2. [Istilah Penting](#2-istilah-penting)
3. [Macam-macam Search Algorithm](#3-macam-macam-search-algorithm)
4. [Penjelasan Tiap Algoritma](#4-penjelasan-tiap-algoritma)
5. [Perbandingan Algoritma](#5-perbandingan-algoritma)
6. [Tentang Program Ini](#6-tentang-program-ini)
7. [Cara Menjalankan Program](#7-cara-menjalankan-program)
8. [Cara Menggunakan Aplikasi](#8-cara-menggunakan-aplikasi)
9. [Output / Hasil Run](#9-output--hasil-run)
10. [Penjelasan Kode](#10-penjelasan-kode)
11. [Kesimpulan](#11-kesimpulan)

---

## 1. Apa itu Search Algorithm?

**Search algorithm** (algoritma pencarian) adalah algoritma yang dipakai untuk **mencari solusi** dari sebuah masalah dengan menelusuri **ruang keadaan (state space)** dari kondisi awal (*initial state*) sampai mencapai kondisi tujuan (*goal state*).

Contoh penerapannya:

- Mencari rute terpendek di Google Maps
- Pathfinding karakter NPC pada game
- Navigasi robot (misalnya robot line follower atau robot maze)
- Menyelesaikan puzzle (8-puzzle, Rubik, sudoku)
- Routing paket pada jaringan komputer

Pada project ini, masalahnya adalah: **mencari jalur dari sel Start ke sel Finish pada grid yang berisi tembok**.

## 2. Istilah Penting

| Istilah | Arti |
|---|---|
| **State / Node** | Satu kondisi/posisi dalam pencarian (pada project ini: satu sel di grid) |
| **Initial state** | Posisi awal (Start) |
| **Goal state** | Posisi tujuan (Finish) |
| **Frontier / Open list** | Kumpulan node yang sudah ditemukan tetapi belum dikunjungi |
| **Visited / Closed list** | Kumpulan node yang sudah dikunjungi |
| **Parent** | Node asal yang membawa kita ke node saat ini (dipakai untuk menyusun jalur) |
| **Completeness** | Apakah algoritma pasti menemukan solusi jika solusi ada |
| **Optimality** | Apakah solusi yang ditemukan pasti yang terbaik (terpendek / berbiaya terkecil) |
| **Time complexity** | Banyaknya node yang diproses |
| **Space complexity** | Banyaknya memori yang dibutuhkan |

Notasi kompleksitas: `b` = branching factor (jumlah cabang tiap node), `d` = kedalaman solusi terdekat, `m` = kedalaman maksimum, `V` = jumlah vertex, `E` = jumlah edge.

## 3. Macam-macam Search Algorithm

Search algorithm secara umum dibagi menjadi dua kelompok besar:

```
Search Algorithm
|
+-- Uninformed Search (Blind Search)      -> tidak punya informasi tentang letak goal
|     +-- Breadth-First Search (BFS)
|     +-- Depth-First Search (DFS)
|     +-- Depth-Limited Search (DLS)
|     +-- Iterative Deepening Search (IDS / IDDFS)
|     +-- Uniform Cost Search (UCS)
|     +-- Bidirectional Search
|
+-- Informed Search (Heuristic Search)    -> memakai fungsi heuristik h(n)
      +-- Greedy Best-First Search
      +-- A* (A-Star)
      +-- IDA* (Iterative Deepening A*)
      +-- (Hill Climbing, Beam Search, Simulated Annealing, dll.)
```

- **Uninformed search**: hanya tahu struktur masalah, menelusuri secara "buta" tanpa petunjuk arah ke tujuan.
- **Informed search**: memakai **heuristik** (perkiraan jarak ke tujuan) untuk mengarahkan pencarian sehingga biasanya lebih cepat.

## 4. Penjelasan Tiap Algoritma

### 4.1 Breadth-First Search (BFS)

- **Jenis:** Uninformed
- **Struktur data:** **Queue (FIFO)** - masuk pertama, keluar pertama
- **Cara kerja:** menelusuri graf **level per level**. Semua tetangga dari node awal dikunjungi dulu, lalu tetangga dari tetangga, dan seterusnya, melebar seperti riak air.
- **Langkah:**
  1. Masukkan node Start ke queue.
  2. Ambil node paling depan dari queue.
  3. Jika node itu adalah Finish, selesai. Susun jalur dari `parent`.
  4. Jika bukan, masukkan semua tetangga yang belum dikunjungi ke belakang queue (catat parent-nya).
  5. Ulangi langkah 2-4 sampai queue kosong.
- **Complete:** Ya
- **Optimal:** Ya, **menjamin jalur terpendek** jika tiap langkah berbiaya sama
- **Time:** O(V + E) atau O(b^d)
- **Space:** O(V) atau O(b^d) (boros memori)
- **Kelebihan:** pasti menemukan jalur terpendek, cocok untuk grid tanpa bobot
- **Kekurangan:** memori besar karena menyimpan seluruh frontier

### 4.2 Depth-First Search (DFS)

- **Jenis:** Uninformed
- **Struktur data:** **Stack (LIFO)** - masuk terakhir, keluar pertama (atau rekursi)
- **Cara kerja:** masuk **sedalam mungkin** pada satu cabang dulu. Jika buntu, mundur (*backtrack*) lalu coba cabang lain.
- **Langkah:**
  1. Masukkan node Start ke stack.
  2. Ambil (pop) node paling atas dari stack.
  3. Jika sudah pernah dikunjungi, lewati. Jika belum, tandai dikunjungi.
  4. Jika node itu Finish, selesai.
  5. Jika bukan, push semua tetangga yang belum dikunjungi ke stack.
  6. Ulangi sampai stack kosong.
- **Complete:** Ya pada graf berhingga dengan pengecekan visited (tidak complete jika ruang tak hingga atau tanpa cek visited)
- **Optimal:** **Tidak**, jalur yang ditemukan bisa jauh lebih panjang dari jalur terpendek
- **Time:** O(V + E) atau O(b^m)
- **Space:** O(b*m) (hemat memori dibanding BFS)
- **Kelebihan:** hemat memori, bisa cepat jika solusi berada jauh di dalam
- **Kekurangan:** jalur belum tentu terpendek, bisa "tersesat" di cabang yang dalam

### 4.3 Depth-Limited Search (DLS)

DFS yang dibatasi sampai kedalaman tertentu `L`. Mencegah DFS masuk terlalu dalam atau berputar tanpa akhir. Kekurangannya, jika solusi berada lebih dalam dari `L`, solusi tidak akan ditemukan (tidak complete). Time O(b^L), space O(b*L).

### 4.4 Iterative Deepening Search (IDS / IDDFS)

Menjalankan DLS berulang kali dengan batas kedalaman yang dinaikkan bertahap (0, 1, 2, ...). Menggabungkan **kelebihan BFS** (complete dan optimal untuk biaya seragam) dengan **kelebihan DFS** (memori hemat, O(b*d)). Walaupun node level atas dikunjungi berulang, total biayanya tetap O(b^d).

### 4.5 Uniform Cost Search (UCS)

- **Struktur data:** **Priority Queue** berdasarkan biaya jalur `g(n)`
- **Cara kerja:** selalu memperluas node dengan **total biaya dari Start paling kecil**. Pada dasarnya BFS yang mendukung bobot/biaya berbeda tiap langkah (identik dengan algoritma Dijkstra).
- **Complete:** Ya (biaya langkah > 0) | **Optimal:** Ya
- **Time/Space:** O(b^(1 + C*/e)), dengan C* = biaya solusi optimal dan e = biaya langkah minimum
- **Kekurangan:** tidak punya arah ke goal, sehingga menyebar ke segala arah

### 4.6 Bidirectional Search

Menjalankan **dua pencarian sekaligus**: satu maju dari Start, satu mundur dari Goal, sampai keduanya bertemu di tengah. Kompleksitas turun dari O(b^d) menjadi sekitar O(b^(d/2)). Syarat: goal harus diketahui jelas dan operasi mundur harus bisa dilakukan.

### 4.7 Greedy Best-First Search

- **Jenis:** Informed
- **Struktur data:** Priority Queue berdasarkan heuristik `h(n)` saja
- **Cara kerja:** selalu memilih node yang **tampak paling dekat ke goal** menurut heuristik, tanpa memperhitungkan biaya yang sudah ditempuh.
- **Complete:** Tidak selalu | **Optimal:** **Tidak**
- **Kelebihan:** sangat cepat dalam banyak kasus
- **Kekurangan:** bisa terjebak di jalan buntu dan hasilnya belum tentu terpendek

### 4.8 A* (A-Star)

- **Jenis:** Informed
- **Struktur data:** Priority Queue berdasarkan `f(n) = g(n) + h(n)`
  - `g(n)` = biaya nyata dari Start ke node `n`
  - `h(n)` = estimasi (heuristik) biaya dari `n` ke Goal
  - `f(n)` = estimasi total biaya jalur yang melewati `n`
- **Heuristik umum pada grid:**
  - **Manhattan distance** (gerak 4 arah): `h = |x1 - x2| + |y1 - y2|`
  - **Euclidean distance** (gerak bebas): `h = sqrt((x1 - x2)^2 + (y1 - y2)^2)`
  - **Diagonal / Chebyshev distance** (gerak 8 arah)
- **Cara kerja:** menggabungkan UCS (memperhitungkan biaya yang sudah ditempuh) dengan Greedy (memperkirakan sisa jarak). Selalu mengambil node dengan `f(n)` terkecil.
- **Complete:** Ya | **Optimal:** Ya, **asalkan heuristik admissible** (tidak pernah melebih-lebihkan biaya sebenarnya, `h(n) <= h*(n)`)
- **Time:** tergantung kualitas heuristik, biasanya jauh lebih sedikit node dibanding BFS/UCS
- **Space:** O(b^d), menyimpan semua node di memori
- **Kelebihan:** cepat dan optimal, standar industri untuk pathfinding
- **Kekurangan:** boros memori, hasil sangat bergantung pada pemilihan heuristik

Contoh pseudocode:

```text
open_list  <- {start}
g[start]   <- 0
f[start]   <- h(start)
while open_list tidak kosong:
    n <- node pada open_list dengan f terkecil
    if n == goal: return susun_jalur(n)
    pindahkan n ke closed_list
    for setiap tetangga m dari n:
        g_baru <- g[n] + biaya(n, m)
        if m belum pernah dikunjungi atau g_baru < g[m]:
            parent[m] <- n
            g[m] <- g_baru
            f[m] <- g_baru + h(m)
            masukkan m ke open_list
return gagal
```

### 4.9 IDA* (Iterative Deepening A*)

Gabungan IDS dan A*. Pencarian DFS dibatasi oleh nilai `f(n)` (bukan kedalaman), dan batas itu dinaikkan bertahap. Tetap optimal seperti A* tetapi memori jauh lebih hemat, O(b*d).

### 4.10 Algoritma Lokal (singkat)

Mencari solusi dengan memperbaiki satu kondisi saat ini tanpa menyimpan jalur:

- **Hill Climbing**: selalu pindah ke tetangga yang lebih baik, bisa terjebak di *local maximum*.
- **Simulated Annealing**: kadang menerima langkah yang lebih buruk agar bisa lolos dari local maximum.
- **Beam Search**: hanya menyimpan `k` node terbaik di tiap level.
- **Genetic Algorithm**: pencarian berbasis populasi dan seleksi alam.

## 5. Perbandingan Algoritma

| Algoritma | Jenis | Struktur Data | Complete | Optimal | Time | Space |
|---|---|---|---|---|---|---|
| BFS | Uninformed | Queue (FIFO) | Ya | Ya (biaya seragam) | O(b^d) | O(b^d) |
| DFS | Uninformed | Stack (LIFO) | Ya* | Tidak | O(b^m) | O(b*m) |
| DLS | Uninformed | Stack | Tidak | Tidak | O(b^L) | O(b*L) |
| IDS | Uninformed | Stack | Ya | Ya (biaya seragam) | O(b^d) | O(b*d) |
| UCS | Uninformed | Priority Queue (g) | Ya | Ya | O(b^(1+C*/e)) | O(b^(1+C*/e)) |
| Bidirectional | Uninformed | 2 Queue | Ya | Ya (biaya seragam) | O(b^(d/2)) | O(b^(d/2)) |
| Greedy Best-First | Informed | Priority Queue (h) | Tidak | Tidak | O(b^m) | O(b^m) |
| A* | Informed | Priority Queue (g+h) | Ya | Ya (heuristik admissible) | tergantung h | O(b^d) |
| IDA* | Informed | Stack | Ya | Ya (heuristik admissible) | tergantung h | O(b*d) |

\* pada graf berhingga dengan pengecekan visited.

**Algoritma yang diimplementasikan di project ini: BFS dan DFS.**

## 6. Tentang Program Ini

Program memvisualisasikan **BFS** dan **DFS** pada grid berukuran **22 baris x 38 kolom**. Pengguna bebas menggambar tembok, memindahkan Start dan Finish, atau membuat maze acak, lalu membandingkan perilaku kedua algoritma secara animasi.

**Fitur:**

- Menggambar dan menghapus tembok dengan klik/drag mouse
- Memindahkan posisi Start dan Finish
- Generate maze acak
- Animasi pencarian BFS dan DFS
- Pengaturan kecepatan animasi
- Menampilkan jumlah node yang dikunjungi dan panjang jalur

**Legenda warna:**

| Warna | Arti |
|---|---|
| Hijau | Start |
| Merah | Finish |
| Biru tua keabu-abuan | Tembok |
| Kuning muda | Frontier (node yang masuk antrian/stack) |
| Biru muda | Node yang sudah dikunjungi |
| Oranye | Jalur hasil pencarian |

## 7. Cara Menjalankan Program

### Prasyarat

- **Python 3.8 atau lebih baru**
- **Tkinter** (sudah bawaan Python di Windows dan macOS)
- Tidak perlu install library tambahan (hanya memakai library standar: `tkinter`, `random`, `collections`)

> Program ini adalah **aplikasi GUI desktop**, jadi harus dijalankan di komputer lokal. Tidak bisa dijalankan di Google Colab, Jupyter Notebook, atau langsung di GitHub karena membutuhkan jendela layar.

### Langkah-langkah

**1. Cek versi Python**

```bash
python --version
```

(Di Linux/macOS bisa jadi perintahnya `python3 --version`.)

**2. Cek Tkinter**

```bash
python -m tkinter
```

Jika muncul jendela kecil bertuliskan "This is Tcl/Tk version ...", berarti Tkinter sudah siap. Jika error di Linux (Ubuntu/Debian), install dengan:

```bash
sudo apt update
sudo apt install python3-tk
```

**3. Dapatkan source code**

```bash
git clone https://github.com/<username>/<nama-repo>.git
cd <nama-repo>
```

Atau download file `main.py` langsung lalu buka terminal di folder tersebut.

**4. Jalankan program**

```bash
# Windows
python main.py

# Linux / macOS
python3 main.py
```

Jendela aplikasi **"Visualisasi Search Algorithm - BFS & DFS"** akan muncul.

**5. (Opsional) Menjalankan lewat VS Code**

Buka folder project di VS Code, buka `main.py`, lalu klik tombol **Run Python File** (segitiga di kanan atas) atau tekan `F5`.

## 8. Cara Menggunakan Aplikasi

1. Pilih **Mode** di bagian atas: **Tembok**, **Start**, atau **Finish**.
2. **Klik / drag kiri** di grid untuk memasang tembok, atau memindahkan Start/Finish sesuai mode.
3. **Klik / drag kanan** untuk menghapus tembok.
4. Tekan **Maze Acak** jika ingin tembok dibuat otomatis.
5. Atur slider **Kecepatan** sesuai keinginan.
6. Tekan **▶ BFS** atau **▶ DFS** untuk memulai animasi pencarian.
7. Gunakan **Reset Jalur** untuk menghapus hasil pencarian (tembok tetap), atau **Hapus Semua** untuk mengosongkan grid.

## 9. Output / Hasil Run

Bagian ini menampilkan hasil eksekusi program yang diambil langsung dari aplikasi (screenshot asli) untuk algoritma BFS dan DFS. Keduanya dijalankan pada grid 22 x 38 dengan kecepatan animasi 60, Start di sisi kiri (hijau) dan Finish di sisi kanan (merah).

### 9.1 Output BFS

![Hasil BFS](images/hasil_bfs.png)

```text
BFS: selesai! Node dikunjungi: 550 | Panjang jalur: 43 langkah
```

Pengamatan:

- Area biru (node dikunjungi) menyebar **merata ke hampir seluruh grid**, karena BFS menelusuri level demi level ke segala arah.
- Jalur oranye relatif **lurus dan efisien** dari Start ke Finish.
- Masih tersisa beberapa sel kuning (frontier) dan putih (belum dikunjungi) di sisi kanan, karena pencarian berhenti begitu Finish ditemukan.

### 9.2 Output DFS

![Hasil DFS](images/hasil_dfs.png)

```text
DFS: selesai! Node dikunjungi: 144 | Panjang jalur: 127 langkah
```

Pengamatan:

- Node yang dikunjungi **tidak menyebar merata**, melainkan masuk dalam satu arah ke area atas dan kanan grid terlebih dahulu.
- Jalur oranye **berkelok-kelok dan sangat panjang**, karena DFS mengikuti satu cabang sedalam mungkin dan berhenti begitu menemukan Finish, tanpa mencari jalur yang lebih pendek.
- Sebagian besar area kiri bawah grid tidak tersentuh sama sekali.

### 9.3 Tabel Perbandingan Hasil

| Algoritma | Node Dikunjungi | Panjang Jalur | Keterangan |
|---|---|---|---|
| BFS | 550 | 43 langkah | Jalur **terpendek**, tetapi menjelajah banyak node (melebar) |
| DFS | 144 | 127 langkah | Node yang dikunjungi lebih sedikit, tetapi jalur **jauh lebih panjang** (tidak optimal) |

> **Catatan:** kedua screenshot diambil dari maze acak yang **berbeda** (tombol **Maze Acak** ditekan sebelum masing-masing run), sehingga jumlah node yang dikunjungi tidak bisa dibandingkan secara langsung. Yang bisa diambil sebagai kesimpulan adalah **karakteristik** masing-masing algoritma: BFS menghasilkan jalur pendek dengan eksplorasi luas, sedangkan DFS menghasilkan jalur panjang yang berkelok. Untuk perbandingan yang adil, jalankan BFS lalu klik **Reset Jalur** (jangan tekan Maze Acak), kemudian jalankan DFS pada maze yang sama.

### 9.4 Analisis Hasil

- **BFS** menemukan jalur sepanjang **43 langkah**. Karena BFS memakai **queue (FIFO)** dan memperluas pencarian level demi level, Finish pasti ditemukan lewat jalur dengan langkah paling sedikit. Harganya, BFS harus mengunjungi banyak node (550) dan menyimpan frontier yang besar di memori.
- **DFS** menemukan jalur sepanjang **127 langkah**, hampir **3 kali lebih panjang** daripada jalur BFS. Karena DFS memakai **stack (LIFO)**, ia masuk sedalam mungkin ke satu arah dan berhenti begitu Finish ketemu, tanpa peduli apakah itu jalur terbaik.
- Jumlah node yang dikunjungi DFS bisa lebih sedikit maupun lebih banyak dari BFS, tergantung bentuk maze dan posisi Finish. Yang konsisten adalah: **BFS selalu menghasilkan jalur terpendek, DFS tidak**.

## 10. Penjelasan Kode

Struktur file:

```
.
├── main.py
├── README.md
├── hasil_bfs.png
└── hasil_dfs.png
```

### Pengaturan

```python
ROWS, COLS, CELL = 22, 38, 26   # jumlah baris, kolom, ukuran 1 sel (piksel)
DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))   # atas, kanan, bawah, kiri
```

### Algoritma sebagai Generator

`bfs()` dan `dfs()` ditulis sebagai **generator** (memakai `yield`). Tiap `yield` mengembalikan `(node_yang_dikunjungi, [node_baru_masuk_frontier])`, sehingga GUI bisa menggambar **satu langkah per frame** dan terlihat seperti animasi. Yield terakhir bernilai `("done", path)`, dengan `path = None` jika jalur tidak ditemukan.

| Fungsi | Peran |
|---|---|
| `neighbors(cell, walls)` | Mengembalikan tetangga valid (4 arah, di dalam grid, bukan tembok) |
| `build_path(parent, end)` | Menyusun jalur dari Finish mundur ke Start lewat dictionary `parent`, lalu dibalik |
| `bfs(start, end, walls)` | BFS dengan `deque` sebagai **queue** (`popleft()` = FIFO) |
| `dfs(start, end, walls)` | DFS dengan `list` sebagai **stack** (`pop()` = LIFO) |

### Inti BFS

```python
queue = deque([start])
parent = {start: None}
while queue:
    cur = queue.popleft()          # ambil dari depan (FIFO)
    if cur == end: ...             # ketemu, susun jalur
    for nb in neighbors(cur, walls):
        if nb not in parent:       # belum pernah ditemukan
            parent[nb] = cur
            queue.append(nb)       # masuk belakang antrian
```

### Inti DFS

```python
stack = [(start, None)]
while stack:
    cur, par = stack.pop()         # ambil dari atas (LIFO)
    if cur in visited: continue
    visited.add(cur)
    parent[cur] = par
    if cur == end: ...             # ketemu, susun jalur
    for nb in reversed(list(neighbors(cur, walls))):
        if nb not in visited:
            stack.append((nb, cur))
```

### Class `App` (GUI)

| Method | Fungsi |
|---|---|
| `_build_ui()` | Membuat toolbar, canvas, label info, dan legenda |
| `draw_all()`, `draw_cell()`, `paint()` | Menggambar grid dan mewarnai sel |
| `on_left()`, `on_right()` | Menangani klik/drag mouse |
| `random_maze()` | Membuat tembok acak (kepadatan 28%) |
| `run()` | Memulai algoritma yang dipilih |
| `step()` | Mengambil satu langkah dari generator dan menjadwalkan langkah berikutnya dengan `root.after()` |
| `animate_path()` | Menganimasikan jalur akhir berwarna oranye |

## 11. Kesimpulan

- Search algorithm adalah dasar dalam menyelesaikan masalah pencarian pada AI, game, robotika, dan jaringan.
- **BFS** cocok jika membutuhkan **jalur terpendek** pada grid tanpa bobot, dengan konsekuensi memori lebih besar.
- **DFS** cocok jika memori terbatas atau yang dibutuhkan hanya **ada/tidaknya jalur**, bukan jalur terpendek.
- **A\*** adalah pengembangan lanjutan yang menggabungkan keunggulan UCS dan heuristik, sehingga **optimal sekaligus efisien**, dan menjadi pilihan utama untuk pathfinding nyata.
- Pemilihan algoritma bergantung pada kebutuhan: optimalitas, kecepatan, dan batasan memori.

## Referensi

- Russell, S. & Norvig, P. *Artificial Intelligence: A Modern Approach*. Pearson.
- Cormen, T. H. et al. *Introduction to Algorithms*. MIT Press.
- Dokumentasi Python: <https://docs.python.org/3/library/tkinter.html>
