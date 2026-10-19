Search Algorithm (Algoritma Pencarian)
1. Pengertian

Search algorithm adalah prosedur sistematis untuk menemukan suatu elemen, solusi, atau jalur di dalam sekumpulan data atau ruang kemungkinan (search space). Algoritma ini dinilai dengan empat kriteria:

Completeness: apakah pasti menemukan solusi jika solusi ada?
Optimality: apakah solusi yang ditemukan adalah yang terbaik?
Time complexity: berapa lama waktu eksekusinya?
Space complexity: berapa banyak memori yang dibutuhkan?

Secara garis besar, algoritma pencarian dibagi menjadi beberapa kelompok.

2. Pencarian pada Struktur Data (Searching in Data)
a. Linear Search (Sequential Search)

Memeriksa elemen satu per satu dari awal sampai ketemu atau data habis.

Data tidak perlu terurut
Waktu: O(n), memori: O(1)
Cocok untuk data kecil atau tak terurut
b. Binary Search

Data harus terurut. Bandingkan nilai target dengan elemen tengah, lalu buang separuh data yang tidak mungkin berisi target, dan ulangi.

Waktu: O(log n), memori: O(1) (iteratif)
Contoh: mencari 23 di [2, 5, 8, 12, 16, 23, 38, 56] selesai dalam sekitar 3 langkah
python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
c. Jump Search

Melompat sebesar √n langkah pada data terurut, lalu melakukan linear search di blok yang tepat. Waktu: O(√n).

d. Interpolation Search

Mirip binary search, tetapi posisi tebakan dihitung dari nilai target (seperti mencari nama di buku telepon). Rata-rata O(log log n) untuk data terurut yang terdistribusi merata, tetapi terburuk O(n).

e. Exponential Search

Menggandakan rentang (1, 2, 4, 8, ...) sampai melewati target, lalu binary search di rentang itu. Berguna untuk data tak terbatas atau sangat besar. Waktu: O(log n).

f. Hash-based Search

Menggunakan fungsi hash untuk langsung menuju lokasi data.

Rata-rata O(1), terburuk O(n) jika banyak collision
Dipakai pada dictionary, hash table, dan database index
g. Tree Search

Pencarian pada struktur pohon seperti BST, AVL, atau B-Tree. Pada pohon seimbang waktunya O(log n). B-Tree banyak dipakai di database dan file system.

3. Pencarian pada Graf / State Space (AI Search)

Di sini masalah dimodelkan sebagai keadaan (state), aksi, dan tujuan (goal). Contohnya mencari rute terpendek, memecahkan puzzle, atau perencanaan robot.

A. Uninformed Search (Blind Search)

Tidak memakai informasi tambahan tentang seberapa dekat suatu state ke tujuan.

Algoritma	Cara kerja	Complete	Optimal	Waktu	Memori
BFS	Menjelajah level demi level (queue)	Ya	Ya (biaya langkah sama)	O(b^d)	O(b^d)
DFS	Menyelam sedalam mungkin dulu (stack/rekursi)	Tidak (bisa loop/tak hingga)	Tidak	O(b^m)	O(bm)
Uniform Cost Search	Memperluas node dengan biaya kumulatif terkecil	Ya	Ya	O(b^(1+C*/ε))	Besar
Depth-Limited Search	DFS dengan batas kedalaman	Tidak selalu	Tidak	O(b^l)	O(bl)
Iterative Deepening DFS (IDDFS)	DFS berulang dengan batas kedalaman naik bertahap	Ya	Ya (biaya sama)	O(b^d)	O(bd)
Bidirectional Search	Mencari dari awal dan dari tujuan sekaligus	Ya	Ya	O(b^(d/2))	O(b^(d/2))

Keterangan: b = branching factor, d = kedalaman solusi, m = kedalaman maksimum.

B. Informed Search (Heuristic Search)

Memakai fungsi heuristik h(n), yaitu estimasi biaya dari node n ke tujuan.

Greedy Best-First Search: selalu memilih node dengan h(n) terkecil. Cepat, tetapi tidak optimal dan tidak complete.
A* (A-star): algoritma yang paling populer. Memakai f(n) = g(n) + h(n), dengan g(n) biaya dari awal ke n dan h(n) estimasi ke tujuan. A* complete dan optimal jika heuristiknya admissible (tidak pernah melebihi biaya sebenarnya) dan consistent. Kelemahannya, memorinya bisa sangat besar.
IDA* (Iterative Deepening A*): gabungan IDDFS dan A*, hemat memori.
Dijkstra: kasus khusus A* dengan h(n) = 0, setara Uniform Cost Search untuk jalur terpendek dengan bobot non-negatif.

Contoh heuristik pada grid: Manhattan distance (untuk gerak 4 arah) atau Euclidean distance.

4. Local Search & Optimasi

Dipakai ketika jalurnya tidak penting, hanya solusi akhirnya (misalnya penjadwalan, desain, atau tuning parameter). Algoritma ini hanya menyimpan satu atau beberapa state saat ini, sehingga sangat hemat memori.

Hill Climbing: selalu pindah ke tetangga yang lebih baik. Rentan terjebak di local maximum, plateau, dan ridge. Variannya: steepest-ascent, stochastic, dan random-restart.
Simulated Annealing: sesekali menerima langkah yang lebih buruk dengan probabilitas yang menurun seiring “suhu” turun, sehingga bisa lolos dari local optimum.
Local Beam Search: menyimpan k state terbaik sekaligus.
Genetic Algorithm: populasi solusi yang berevolusi melalui seleksi, crossover, dan mutasi.
Tabu Search, Particle Swarm Optimization, Ant Colony Optimization: metode metaheuristic lainnya.
5. Adversarial Search (Permainan)

Untuk situasi dengan lawan, seperti catur atau tic-tac-toe.

Minimax: memaksimalkan hasil pemain sendiri dengan mengasumsikan lawan meminimalkannya.
Alpha-Beta Pruning: optimasi minimax yang memangkas cabang tak relevan. Hasilnya sama, tetapi jauh lebih cepat (dalam kasus terbaik O(b^(m/2))).
Monte Carlo Tree Search (MCTS): memakai simulasi acak, dipakai pada Go (AlphaGo).
6. String Searching (Pencarian Pola dalam Teks)
Naive: O(nm)
Knuth-Morris-Pratt (KMP): memakai tabel prefix agar tidak mengulang perbandingan, O(n+m)
Boyer-Moore: membandingkan dari kanan dan melompat, sangat cepat dalam praktik
Rabin-Karp: memakai rolling hash, bagus untuk pencarian banyak pola
7. Panduan Memilih Algoritma
Situasi	Pilihan
Data kecil / tak terurut	Linear search
Data terurut	Binary search
Lookup cepat berdasarkan key	Hash table
Jalur terpendek, bobot sama	BFS
Jalur terpendek, bobot berbeda	Dijkstra
Jalur terpendek + ada heuristik	A*
Memori terbatas, ruang sangat dalam	IDDFS / IDA*
Optimasi tanpa peduli jalur	Hill climbing / Simulated annealing / GA
Game dua pemain	Minimax + Alpha-Beta
Cari kata dalam teks	KMP / Boyer-Moore
8. Ringkasan Kompleksitas
Algoritma	Rata-rata / Umum	Terburuk
Linear Search	O(n)	O(n)
Binary Search	O(log n)	O(log n)
Jump Search	O(√n)	O(√n)
Interpolation Search	O(log log n)	O(n)
Hash Search	O(1)	O(n)
BFS / DFS (graf)	O(V + E)	O(V + E)
Dijkstra (heap)	O((V+E) log V)	O((V+E) log V)
A*	Bergantung heuristik	Eksponensial
