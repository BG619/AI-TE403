from tkinter import *
from tkinter import ttk
from queue import PriorityQueue
from tkinter import messagebox
from collections import deque
import heapq
import random
import time
import math

# initialize main window
root = Tk()
root.title('Pathfinding Algorithm Visualisation')
root.maxsize(900, 900)
root.config(bg='black')

font = ("Helvetica", 11)

# Variables
selected_alg = StringVar()
selected_bld = StringVar()
WIDTH = 500
ROWS = 25
grid = []

# frame layout - for user interface
UI_frame = Frame(root, width=600, height=200, bg='black')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
    
# create canvas
canvas = Canvas(root, width=WIDTH, height=WIDTH, bg='white')
canvas.grid(row=0, column=1, padx=10, pady=5) 

# define class - spot
class Spot:
    
    start_point = None
    end_point = None
    
    __slots__ = ['button','row', 'col', 'width', 'neighbors', 'g', 'h', 'f',  
                 'parent', 'start', 'end', 'barrier', 'clicked', 'total_rows']
    
    def __init__(self, row, col, width, offset, total_rows):
        
        self.button = Button(canvas,
         command = lambda a=row, b=col: self.click(a, b),
         bg='white', bd=2, relief=GROOVE
        )
        
        self.row = row
        self.col = col
        self.width = width
        
        self.button.place(x=row * width + offset, y=col * width + offset, 
                          width=width, height=width)

        self.neighbors = []
        self.g = float('inf') 
        self.h = 0
        self.f = float('inf')
        self.parent = None
        self.start = False
        self.end = False
        self.barrier = False
        self.clicked = False
        self.total_rows = total_rows
    
    def make_start(self):
        self.button.config(bg = "DarkOrange2")
        self.start = True
        self.clicked = True
        Spot.start_point = (self.col, self.row)
        
    def make_end(self):
        self.button.config(bg = "lime green")
        self.end = True
        self.clicked = True
        Spot.end_point = (self.col, self.row)
        
    def make_barrier(self):
        self.button.config(bg = "black")
        self.barrier = True
        self.clicked = True
        
    def reset(self):
        self.button.config(bg = "white")
        self.clicked = False
        
    def make_path(self):
        self.button.config(bg = "gold")
        
    def make_to_visit(self):
        self.button.config(bg = "pink")

    def make_backtracking(self):
        self.button.config(bg = "SteelBlue1")
        
    def make_open(self):
        self.button.config(bg = "cornflower blue")
        
    def make_closed(self):
        self.button.config(bg = "LightSkyBlue2")
        
    def disable(self):
        self.button.config(state=DISABLED)
    
    def enable(self):
        self.button.config(state=NORMAL)
    
    def click(self, row, col):
        if self.clicked == False:
            if not Spot.start_point:   
                self.make_start()
            elif not Spot.end_point:
                self.make_end()
            else :
                self.make_barrier()
        else:
            self.reset()
            if self.start == True:   
                self.start = False
                Spot.start_point = None
            elif self.end == True:
                self.end = False
                Spot.end_point = None
            else :
                self.barrier = False
    
    def update_neighbors(self, grid):
        self.neighbors = []

        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].barrier:
            self.neighbors.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].barrier:
            self.neighbors.append(grid[self.row - 1][self.col])

        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].barrier:
            self.neighbors.append(grid[self.row][self.col + 1])

        if self.col > 0 and not grid[self.row][self.col - 1].barrier:
            self.neighbors.append(grid[self.row][self.col - 1])

def make_grid(width, rows):
    gap = width // rows
    offset = 2
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, offset, rows)
            grid[i].append(spot)
    return grid

def h(a, b):
    return abs(a.row - b.row) + abs(a.col - b.col)

def reconstruct_path(spot, tickTime):
    current = spot
    while current.start == False:
        parent = current.parent
            
        parent.make_path()
        root.update_idletasks()
        time.sleep(tickTime)

        current = parent

def Reset():
    global grid
        
    Spot.start_point = None
    Spot.end_point = None
    
    for row in grid:
        for spot in row:
            spot.reset()
            spot.neighbors = []
            spot.g = float('inf') 
            spot.h = 0
            spot.f = float('inf')
            spot.parent = None
            spot.start = False
            spot.end = False
            spot.barrier = False
            spot.enable()
            
def break_wall(current, new):
    if current.row == new.row:
        if current.col > new.col:
            wall = grid[current.row][current.col - 1]
        else:
            wall = grid[current.row][current.col + 1]
    else:
        if current.row > new.row:
            wall = grid[current.row - 1][current.col]
        else:
            wall = grid[current.row + 1][current.col]
    wall.reset()
    wall.barrier = False

def dijkstras(grid, tickTime):
    count = 0
    start = grid[Spot.start_point[1]][Spot.start_point[0]]
    end = grid[Spot.end_point[1]][Spot.end_point[0]]
    
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    start.g = 0
    
    open_set_hash = {start}
    
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(end, tickTime)
            end.make_end()
            start.make_start()
            
            for child in UI_frame.winfo_children():
                child.configure(state='normal')
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = current.g + 1
            
            if temp_g_score < neighbor.g:
                neighbor.parent = current
                neighbor.g = temp_g_score
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.g, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        root.update_idletasks()
        time.sleep(tickTime)
        
        if current != start:
            current.make_closed()
            
    messagebox.showinfo("No Solution", "There was no solution")
    return False

def a_star(grid, tickTime):
    count = 0
    start = grid[Spot.start_point[1]][Spot.start_point[0]]
    end = grid[Spot.end_point[1]][Spot.end_point[0]]
    
    open_set = PriorityQueue()
    open_set.put((0, count, start))

    start.g = 0
    start.f = h(start, end)
    
    open_set_hash = {start}
    
    while not open_set.empty():
        current = open_set.get()[2]
        open_set_hash.remove(current)
        
        if current == end:
            reconstruct_path(end, tickTime)
            end.make_end()
            start.make_start()
            
            for child in UI_frame.winfo_children():
                child.configure(state='normal')
            return True
        
        for neighbor in current.neighbors:
            temp_g_score = current.g + 1
            
            if temp_g_score < neighbor.g:
                neighbor.parent = current
                neighbor.g = temp_g_score
                neighbor.f = temp_g_score + h(neighbor, end)
                
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((neighbor.f, count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        
        root.update_idletasks()
        time.sleep(tickTime)
        
        if current != start:
            current.make_closed()
            
    messagebox.showinfo("No Solution", "There was no solution")
    return False

def StartAlgorithm():
    global grid
    if not grid: return
    if not Spot.start_point or not Spot.end_point: 
        messagebox.showinfo("No start/end", "Place starting and ending points")
        return
    
    for row in grid:
        for spot in row:
            spot.neighbors = []
            spot.g = float('inf') 
            spot.h = 0
            spot.f = float('inf')
            spot.parent = None
            spot.update_neighbors(grid)
            if spot.clicked == False:
                spot.reset()
            spot.disable()
    
    for child in UI_frame.winfo_children():
        child.configure(state='disable')
    
    if algMenu.get() == 'A* Algorithm':
        a_star(grid, speedScale.get())
    elif algMenu.get() == "Dijkstra's Algorithm":
        dijkstras(grid, speedScale.get())    
        
    for row in grid:
        for spot in row:
            spot.enable()
    
    for child in UI_frame.winfo_children():
        child.configure(state='normal')

def random_walls(grid):
    if not Spot.start_point:
        current = grid[random.randint(0, ROWS - 1)][random.randint(0, ROWS - 1)]
        if current.end == False:
            current.make_start()
    
    if not Spot.end_point:
        current = grid[random.randint(0, ROWS - 1)][random.randint(0, ROWS - 1)]
        if current.start == False:
            current.make_end()
            
    start = grid[Spot.start_point[1]][Spot.start_point[0]]
    end = grid[Spot.end_point[1]][Spot.end_point[0]]
    
    for row in grid:
        for spot in row:
            if spot != start and spot != end:
                spot.reset()
                spot.barrier = False
                spot.clicked = False
                if random.randint(0, 100) < wallsScale.get():
                    spot.make_barrier()
        
    root.update_idletasks()

def circ_maze(grid, rows):
    Reset()
    rings = []
    for n in range(rows // 2 + 1):
        set1 = set()
        set2 = set()
        for row in grid:    
            for spot in row:
                if spot.row in range(n, rows - n) and spot.col in range(n, rows - n):
                    set1.add(spot)
                if spot.row in range(n + 1, rows - n - 1) and spot.col in range(n + 1, rows - n - 1):
                    set2.add(spot)
        ring = list(set1 - set2)
        if len(ring) > 0:
            rings.append(ring)
    
    random.choice(rings[0]).make_start()
    for spot in rings[0]:
        if spot.start == True:
            rings[0].remove(spot)
    
    random.choice(rings[-1]).make_end()
    for spot in rings[-1]:
        if spot.end == True:
            rings[-1].remove(spot)

    for ring in rings[1::2]:
        if len(ring) > 0:
            min_row = min([spot.row for spot in ring])
            max_row = max([spot.row for spot in ring])
            tmp = []
            for spot in ring:
                if (spot.row, spot.col) in [(min_row, min_row), (min_row, max_row),
                                            (max_row, min_row), (max_row, max_row)]:
                    tmp.append(spot)
            for item in tmp:
                ring.remove(item)
        
        for spot in ring:
            spot.make_barrier()
        
        if len(ring) == 0:
            rings.remove(ring)
    
    for ring in rings[1::2]:
        for item in random.sample(ring, 2):
            item.reset()
            item.barrier = False
    
    for row in grid:
        for spot in row:
            spot.neighbors = []
            spot.update_neighbors(grid)
    
    for ring in rings[2::2]:
        tmp = []
        for spot in ring:
            if len(spot.neighbors) < 3:
                tmp.append(spot)
        if len(tmp) > 0:
            single_wall = random.choice(tmp)
            single_wall.make_barrier()        
        
    root.update_idletasks()
    
def carve_out(grid, rows, tickTime):
    Reset()
    to_visit = []
    for row in grid[::2]:
        for spot in row[::2]:
            to_visit.append(spot)
        
    for row in grid:
        for spot in row:
            if spot in to_visit:
                spot.make_to_visit()
            else:
                spot.make_barrier()
    
    to_visit[0].make_start()
    to_visit[-1].make_end()
    start = grid[Spot.start_point[1]][Spot.start_point[0]]
    end = grid[Spot.end_point[1]][Spot.end_point[0]]
    
    root.update_idletasks()
    time.sleep(tickTime)
    
    visited = []
    open_set = []
    current = start
    open_set.append(current)
    visited.append(current)
    
    while len(open_set) > 0:
        moves = []
        
        if current.col + 2 < rows:
            neighbor = grid[current.row][current.col + 2]
            if neighbor not in visited and neighbor in to_visit:
                moves.append(neighbor)

        if current.col - 2 >= 0:
            neighbor = grid[current.row][current.col - 2]
            if neighbor not in visited and neighbor in to_visit:
                moves.append(neighbor)
            
        if current.row + 2 < rows:
            neighbor = grid[current.row + 2][current.col]
            if neighbor not in visited and neighbor in to_visit:
                moves.append(neighbor)
            
        if current.row - 2 >= 0:
            neighbor = grid[current.row - 2][current.col]
            if neighbor not in visited and neighbor in to_visit:
                moves.append(neighbor)

        if len(moves) > 0:
            new = random.choice(moves)
            break_wall(current, new)
            if new != end:
                new.reset()
            current = new
            visited.append(current)
            open_set.append(current)
        else:
            current = open_set.pop()
            if current != start and current != end:
                current.make_backtracking()
                root.update_idletasks()
                time.sleep(tickTime)
                current.reset()
            
        root.update_idletasks()
        time.sleep(tickTime)
        
    root.update_idletasks()
    time.sleep(tickTime)
    
def build_maze():
    global grid
    if not grid: return

    for row in grid:
        for spot in row:
            spot.disable()
    
    for child in UI_frame.winfo_children():
        child.configure(state='disable')
    
    if bldMenu.get() == 'Random walls':
        random_walls(grid)
    elif bldMenu.get() == 'Circular maze':
        circ_maze(grid, ROWS) 
    elif bldMenu.get() == 'Carved out maze':
        carve_out(grid, ROWS, speedScale.get())
        
    for row in grid:
        for spot in row:
            spot.enable()
    
    for child in UI_frame.winfo_children():
        child.configure(state='normal')

def scale_action(event):
    if bldMenu.get() == 'Random walls':
        wallsScale.configure(state='normal')
    else:
        wallsScale.configure(state='disable')
        
def instructions():
    messagebox.showinfo("Instructions", "1. Create a maze by clicking on the grid or choose\n"
                                        "     one of the functions from the drop-down menu\n"
                                        "\n"
                                        "     You can always edit any generated mazes\n"
                                        "\n"
                                        "2. Choose one of two available algorithms to find the shortest\n"
                                        "     path and visualize the search with desired speed of animation\n"
                                        "\n"
                                        "3. Reset the grid!")

# User interface area
bldMenu = ttk.Combobox(UI_frame, textvariable=selected_bld, 
                       values=['Random walls', 'Circular maze', 'Carved out maze'], font = font)
bldMenu.grid(row=0, column=0, padx=5, pady=(10, 5))
bldMenu.current(0)
bldMenu.bind("<<ComboboxSelected>>", scale_action)

wallsScale = Scale(UI_frame, from_=10, to=40, resolution=5, orient=HORIZONTAL, 
                   label='Wall density', font = font, length=180)
wallsScale.grid(row=1, column=0, padx=5, pady=5, sticky=W)

Button(UI_frame, text='Build maze', command=build_maze, font = ("Helvetica", 14),
       bg='pale green').grid(row=2, column=0, padx=5, pady=(10, 20))

algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, 
                       values=['A* Algorithm', "Dijkstra's Algorithm"], font = font)
algMenu.grid(row=3, column=0, padx=5, pady=(20, 5), sticky=W)
algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.05, to=0.5, digits=2, resolution=0.05, 
                   orient=HORIZONTAL, label='Speed', font = font, length=180)
speedScale.grid(row=4, column=0, padx=5, pady=(5, 5), sticky=W)

Button(UI_frame, text='Start Search', command=StartAlgorithm, font = ("Helvetica", 14),
       bg='light salmon').grid(row=5, column=0, padx=5, pady=(10, 10))

Button(UI_frame, text='Reset', command=Reset, font = ("Helvetica", 14),
       bg='white').grid(row=6, column=0, padx=5, pady=(20, 30))

Button(UI_frame, text='Instructions', command=instructions, font = ("Helvetica", 9),
       bg='white').grid(row=7, column=0, padx=5, pady=(10, 10))

# Create grid
grid = make_grid(WIDTH, ROWS)
instructions()

# run loop 
root.mainloop()
