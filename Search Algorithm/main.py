"""
Visualisasi Search Algorithm (BFS & DFS) pada grid / maze.

Cara pakai:
  - Pilih mode: Tembok / Start / Finish
  - Klik / drag kiri di grid  -> pasang (tembok / start / finish)
  - Klik / drag kanan         -> hapus tembok
  - Klik tombol BFS atau DFS  -> lihat animasi pencariannya
"""

import random
import tkinter as tk
from collections import deque

# ---------- Pengaturan grid ----------
ROWS, COLS, CELL = 22, 38, 26

# ---------- Warna ----------
C_EMPTY = "#ffffff"
C_WALL = "#2d3142"
C_START = "#2ecc71"
C_END = "#e74c3c"
C_FRONTIER = "#f9e79f"   # sudah masuk antrian / stack, belum dikunjungi
C_VISITED = "#85c1e9"    # sudah dikunjungi
C_PATH = "#f5b041"       # jalur hasil
C_GRID = "#d0d3d4"

DIRS = ((-1, 0), (0, 1), (1, 0), (0, -1))  # atas, kanan, bawah, kiri


# =====================================================================
#  ALGORITMA (ditulis sebagai generator supaya bisa dianimasikan)
#  Tiap yield  -> (node_yang_dikunjungi, [node_baru_masuk_frontier])
#  Yield terakhir -> ("done", path)  ; path = None kalau tidak ketemu
# =====================================================================
def neighbors(cell, walls):
    r, c = cell
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in walls:
            yield (nr, nc)


def build_path(parent, end):
    path, cur = [], end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    return path[::-1]


def bfs(start, end, walls):
    """Breadth-First Search: pakai QUEUE (FIFO) -> menjamin jalur terpendek."""
    queue = deque([start])
    parent = {start: None}
    while queue:
        cur = queue.popleft()
        new_nodes = []
        if cur == end:
            yield ("done", build_path(parent, end))
            return
        for nb in neighbors(cur, walls):
            if nb not in parent:
                parent[nb] = cur
                queue.append(nb)
                new_nodes.append(nb)
        yield (cur, new_nodes)
    yield ("done", None)


def dfs(start, end, walls):
    """Depth-First Search: pakai STACK (LIFO) -> masuk sedalam mungkin dulu."""
    stack = [(start, None)]
    parent, visited = {}, set()
    while stack:
        cur, par = stack.pop()
        if cur in visited:
            continue
        visited.add(cur)
        parent[cur] = par
        if cur == end:
            yield ("done", build_path(parent, end))
            return
        new_nodes = []
        for nb in reversed(list(neighbors(cur, walls))):
            if nb not in visited:
                stack.append((nb, cur))
                new_nodes.append(nb)
        yield (cur, new_nodes)
    yield ("done", None)


# =====================================================================
#  GUI
# =====================================================================
class App:
    def __init__(self, root):
        self.root = root
        root.title("Visualisasi Search Algorithm - BFS & DFS")
        root.resizable(False, False)

        self.walls = set()
        self.start = (ROWS // 2, 3)
        self.end = (ROWS // 2, COLS - 4)
        self.gen = None
        self.running = False
        self.job = None
        self.mode = tk.StringVar(value="wall")

        self._build_ui()
        self.draw_all()

    # ---------- UI ----------
    def _build_ui(self):
        bar = tk.Frame(self.root, padx=8, pady=6)
        bar.pack(fill="x")

        tk.Label(bar, text="Mode:").pack(side="left")
        for text, val in (("Tembok", "wall"), ("Start", "start"), ("Finish", "end")):
            tk.Radiobutton(bar, text=text, variable=self.mode, value=val).pack(side="left")

        tk.Button(bar, text="▶ BFS", width=8, bg="#aed6f1",
                  command=lambda: self.run(bfs, "BFS")).pack(side="left", padx=(14, 3))
        tk.Button(bar, text="▶ DFS", width=8, bg="#abebc6",
                  command=lambda: self.run(dfs, "DFS")).pack(side="left", padx=3)
        tk.Button(bar, text="Maze Acak", command=self.random_maze).pack(side="left", padx=(14, 3))
        tk.Button(bar, text="Reset Jalur", command=self.reset_search).pack(side="left", padx=3)
        tk.Button(bar, text="Hapus Semua", command=self.clear_all).pack(side="left", padx=3)

        tk.Label(bar, text="Kecepatan:").pack(side="left", padx=(14, 0))
        self.speed = tk.Scale(bar, from_=1, to=100, orient="horizontal", length=110)
        self.speed.set(60)
        self.speed.pack(side="left")

        self.canvas = tk.Canvas(self.root, width=COLS * CELL, height=ROWS * CELL,
                                bg=C_EMPTY, highlightthickness=0)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_left)
        self.canvas.bind("<B1-Motion>", self.on_left)
        self.canvas.bind("<Button-3>", self.on_right)
        self.canvas.bind("<B3-Motion>", self.on_right)

        self.info = tk.Label(self.root, anchor="w", padx=8, pady=5,
                             text="Gambar tembok dengan klik/drag, lalu pilih BFS atau DFS.")
        self.info.pack(fill="x")

        legend = tk.Frame(self.root, padx=8)
        legend.pack(fill="x", pady=(0, 6))
        for color, text in ((C_START, "Start"), (C_END, "Finish"), (C_WALL, "Tembok"),
                            (C_FRONTIER, "Frontier"), (C_VISITED, "Dikunjungi"), (C_PATH, "Jalur")):
            tk.Label(legend, bg=color, width=2, relief="solid", bd=1).pack(side="left")
            tk.Label(legend, text=text).pack(side="left", padx=(2, 10))

    # ---------- Gambar ----------
    def draw_cell(self, cell, color):
        r, c = cell
        x, y = c * CELL, r * CELL
        self.canvas.create_rectangle(x, y, x + CELL, y + CELL, fill=color, outline=C_GRID)

    def color_of(self, cell):
        if cell == self.start:
            return C_START
        if cell == self.end:
            return C_END
        if cell in self.walls:
            return C_WALL
        return C_EMPTY

    def draw_all(self):
        self.canvas.delete("all")
        for r in range(ROWS):
            for c in range(COLS):
                self.draw_cell((r, c), self.color_of((r, c)))

    def paint(self, cell, color):
        """Warnai sel pencarian, tapi jangan timpa start / finish."""
        if cell != self.start and cell != self.end:
            self.draw_cell(cell, color)

    # ---------- Input mouse ----------
    def cell_at(self, event):
        c, r = event.x // CELL, event.y // CELL
        if 0 <= r < ROWS and 0 <= c < COLS:
            return (r, c)
        return None

    def on_left(self, event):
        if self.running:
            return
        cell = self.cell_at(event)
        if cell is None:
            return
        mode = self.mode.get()
        if mode == "wall":
            if cell not in (self.start, self.end) and cell not in self.walls:
                self.walls.add(cell)
                self.draw_cell(cell, C_WALL)
        elif mode == "start" and cell != self.end:
            self.start = cell
            self.walls.discard(cell)
            self.draw_all()
        elif mode == "end" and cell != self.start:
            self.end = cell
            self.walls.discard(cell)
            self.draw_all()

    def on_right(self, event):
        if self.running:
            return
        cell = self.cell_at(event)
        if cell in self.walls:
            self.walls.discard(cell)
            self.draw_cell(cell, C_EMPTY)

    # ---------- Kontrol ----------
    def stop(self):
        self.running = False
        if self.job:
            self.root.after_cancel(self.job)
            self.job = None

    def reset_search(self):
        self.stop()
        self.draw_all()
        self.info.config(text="Jalur direset.")

    def clear_all(self):
        self.stop()
        self.walls.clear()
        self.draw_all()
        self.info.config(text="Grid dikosongkan.")

    def random_maze(self):
        self.stop()
        self.walls = {(r, c) for r in range(ROWS) for c in range(COLS)
                      if random.random() < 0.28} - {self.start, self.end}
        self.draw_all()
        self.info.config(text="Maze acak dibuat. Pilih BFS atau DFS.")

    # ---------- Jalanin algoritma ----------
    def run(self, algo, name):
        self.stop()
        self.draw_all()
        self.name = name
        self.gen = algo(self.start, self.end, self.walls)
        self.visited_count = 0
        self.running = True
        self.info.config(text=f"{name} berjalan...")
        self.step()

    def step(self):
        if not self.running:
            return
        try:
            first, second = next(self.gen)
        except StopIteration:
            self.running = False
            return

        if first == "done":
            self.finish(second)
            return

        self.visited_count += 1
        for nb in second:
            self.paint(nb, C_FRONTIER)
        self.paint(first, C_VISITED)
        self.info.config(text=f"{self.name} berjalan... node dikunjungi: {self.visited_count}")

        delay = max(1, int(400 / self.speed.get() ** 1.0) - 3)
        self.job = self.root.after(delay, self.step)

    def finish(self, path):
        if path is None:
            self.running = False
            self.info.config(text=f"{self.name}: jalur TIDAK ditemukan. "
                                  f"Node dikunjungi: {self.visited_count}")
            return
        self.animate_path(path, 0)

    def animate_path(self, path, i):
        if i < len(path):
            self.paint(path[i], C_PATH)
            self.job = self.root.after(25, lambda: self.animate_path(path, i + 1))
        else:
            self.running = False
            self.info.config(text=f"{self.name}: selesai! Node dikunjungi: "
                                  f"{self.visited_count} | Panjang jalur: {len(path) - 1} langkah")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
