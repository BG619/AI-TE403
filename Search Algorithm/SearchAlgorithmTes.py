from tkinter import *
import time
from queue import Queue
import heapq


""" ------------------------------------ Kelas titik (dari point.py) --------------------------------- """

class aStarPoint:

    def __init__(self, x, y, current_cost, heuristic_cost):
        self.x = x
        self.y = y
        self.current_cost = current_cost
        self.heuristic_cost = heuristic_cost

    def __lt__(self, other):
        return (self.current_cost + self.heuristic_cost) < (other.current_cost + other.heuristic_cost)


class bestFitSearchPoint:

    def __init__(self, x, y, heuristic_cost):
        self.x = x
        self.y = y
        self.heuristic_cost = heuristic_cost

    def __lt__(self, other):
        return self.heuristic_cost < other.heuristic_cost


""" ------------------------------------ Fungsi bantu (dari utils.py) --------------------------------- """

def getCellColor(grid, rowIndex, columnIndex):
    cell = grid[rowIndex][columnIndex]
    if (cell == 0):
        return "white"
    elif (cell == 1):
        return "black"
    elif (cell == 2):
        return "green"
    else:
        return "blue"


def getDistance(x, y):
    return abs(x[0]-y[0]) + abs(x[1]-y[1])


""" ------------------------------------ Variabel global --------------------------------- """

grid_rows = 30
grid_columns = 30
cell_size = 20
current_source = [0, 0]
current_destination = [grid_rows-1, grid_columns-1]
movement_time = 0.05

heading_text = "Path Finding Visualizer"
grid = [[0]*grid_columns for i in range(grid_rows)]
visited = [[0]*grid_columns for i in range(grid_rows)]

grid[current_source[0]][current_source[1]] = 2
grid[current_destination[0]][current_destination[1]] = 3
visited[current_source[0]][current_source[1]] = 1


def draw(event, grid_view, point_options):

    global current_source, current_destination

    i = event.x // cell_size
    j = event.y // cell_size
    x1 = i * cell_size
    y1 = j * cell_size
    x2 = x1 + cell_size
    y2 = y1 + cell_size

    if (i>=0 and j>=0 and i<grid_rows and j<grid_columns):
        current_option = point_options.get()
        if (current_option == "Wall" and grid[i][j] != 2 and grid[i][j] != 3):
            grid[i][j] = 1
            grid_view.create_rectangle(x1, y1, x2, y2, fill="black", outline="black")
        elif (current_option == "Free Space" and grid[i][j] != 2 and grid[i][j] != 3):
            grid[i][j] = 0
            grid_view.create_rectangle(x1, y1, x2, y2, fill="white", outline="black")
        elif (current_option == "Source" and grid[i][j] != 3):
            grid[current_source[0]][current_source[1]] = 0
            grid_view.create_rectangle(current_source[0]*cell_size, current_source[1]*cell_size, current_source[0]*cell_size+cell_size, current_source[1]*cell_size+cell_size, fill="white", outline="black")
            grid[i][j] = 2
            grid_view.create_rectangle(x1, y1, x2, y2, fill="green", outline="black")
            current_source = [i, j]
        elif (current_option == "Destination" and grid[i][j] != 2):
            grid[current_destination[0]][current_destination[1]] = 0
            grid_view.create_rectangle(current_destination[0]*cell_size, current_destination[1]*cell_size, current_destination[0]*cell_size+cell_size, current_destination[1]*cell_size+cell_size, fill="white", outline="black")
            grid[i][j] = 3
            grid_view.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
            current_destination = [i, j]


def create_grid(grid_view):
    for i in range(grid_rows):
        for j in range(grid_columns):
            x1 = cell_size*i
            y1 = cell_size*j
            x2 = x1+cell_size
            y2 = y1+cell_size
            color = getCellColor(grid, i, j)
            grid_view.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")


def dfs_search(grid_view, current):

    if current == current_destination:
        return True

    if current != current_source:
        grid_view.create_rectangle(current[0]*cell_size, current[1]*cell_size, current[0]*cell_size+cell_size, current[1]*cell_size+cell_size, fill="orange", outline="black")
        grid_view.update_idletasks()

    neighbors = [[current[0]-1,current[1]], [current[0],current[1]+1], [current[0]+1,current[1]], [current[0],current[1]-1]]
    for neighbor in neighbors:
        x, y = neighbor
        if x>=0 and y>=0 and x<grid_rows and y<grid_columns and grid[x][y]!=1 and not(visited[x][y]):
            visited[x][y] = 1
            time.sleep(movement_time)
            result = dfs_search(grid_view, neighbor)
            if result:
                if current != current_source:
                    grid_view.create_rectangle(current[0]*cell_size, current[1]*cell_size, current[0]*cell_size+cell_size, current[1]*cell_size+cell_size, fill="yellow", outline="black")
                    grid_view.update_idletasks()
                return True

    return False


def bfs_search(grid_view, current):

    parent_to_children = {}
    q = Queue()
    q.put(current_source)

    while (not(q.empty())):

        current = q.get()
        if (current == current_destination):
            break

        if (current != current_source):
            grid_view.create_rectangle(current[0]*cell_size, current[1]*cell_size, current[0]*cell_size+cell_size, current[1]*cell_size+cell_size, fill="orange", outline="black")
            grid_view.update_idletasks()

        neighbors = [[current[0]-1,current[1]], [current[0],current[1]+1], [current[0]+1,current[1]], [current[0],current[1]-1]]
        for neighbor in neighbors:
            x, y = neighbor
            if x>=0 and y>=0 and x<grid_rows and y<grid_columns and grid[x][y]!=1 and not(visited[x][y]):
                q.put(neighbor)
                parent_to_children[neighbor[0]*grid_columns+neighbor[1]] = current[0]*grid_columns+current[1]
                visited[x][y] = 1
                time.sleep(movement_time)

        path_point = current_destination[0]*grid_columns + current_destination[1]
        while (parent_to_children.get(path_point)):
            parent = parent_to_children[path_point]
            if parent != current_source[0]*grid_columns + current_source[1]:
                grid_view.create_rectangle((parent//grid_columns)*cell_size, (parent%grid_columns)*cell_size, (parent//grid_columns)*cell_size+cell_size, (parent%grid_columns)*cell_size+cell_size, fill="yellow", outline="black")
                grid_view.update_idletasks()
            path_point = parent


def a_star_search(grid_view, current):

    parent_to_children = {}
    q = []
    heapq.heappush(q, aStarPoint(current_source[0], current_source[1], 0, getDistance(current_source, current_destination)))

    while (len(q)):

        current = heapq.heappop(q)
        if ([current.x, current.y] == current_destination):
            break

        if ([current.x, current.y] != current_source):
            grid_view.create_rectangle(current.x*cell_size, current.y*cell_size, current.x*cell_size+cell_size, current.y*cell_size+cell_size, fill="orange", outline="black")
            grid_view.update_idletasks()


        neighbors = [
            aStarPoint(current.x-1, current.y, current.current_cost+1, getDistance([current.x-1, current.y], current_destination)),
            aStarPoint(current.x, current.y+1, current.current_cost+1, getDistance([current.x, current.y+1], current_destination)),
            aStarPoint(current.x+1, current.y, current.current_cost+1, getDistance([current.x+1, current.y], current_destination)),
            aStarPoint(current.x, current.y-1, current.current_cost+1, getDistance([current.x, current.y-1], current_destination))
        ]

        for neighbor in neighbors:
            x, y = neighbor.x, neighbor.y
            if x>=0 and y>=0 and x<grid_rows and y<grid_columns and grid[x][y]!=1 and not(visited[x][y]):
                heapq.heappush(q, neighbor)
                parent_to_children[neighbor.x*grid_columns+neighbor.y] = current.x*grid_columns+current.y
                visited[x][y] = 1
                time.sleep(movement_time)

        path_point = current_destination[0]*grid_columns + current_destination[1]
        while (parent_to_children.get(path_point)):
            parent = parent_to_children[path_point]
            if parent != current_source[0]*grid_columns + current_source[1]:
                grid_view.create_rectangle((parent//grid_columns)*cell_size, (parent%grid_columns)*cell_size, (parent//grid_columns)*cell_size+cell_size, (parent%grid_columns)*cell_size+cell_size, fill="yellow", outline="black")
                grid_view.update_idletasks()
            path_point = parent


def best_first_search(grid_view, current):

    parent_to_children = {}
    q = []
    heapq.heappush(q, bestFitSearchPoint(current_source[0], current_source[1], getDistance(current_source, current_destination)))

    while (len(q)):

        current = heapq.heappop(q)
        if ([current.x, current.y] == current_destination):
            break

        if ([current.x, current.y] != current_source):
            grid_view.create_rectangle(current.x*cell_size, current.y*cell_size, current.x*cell_size+cell_size, current.y*cell_size+cell_size, fill="orange", outline="black")
            grid_view.update_idletasks()


        neighbors = [
            bestFitSearchPoint(current.x-1, current.y, getDistance([current.x-1, current.y], current_destination)),
            bestFitSearchPoint(current.x, current.y+1, getDistance([current.x, current.y+1], current_destination)),
            bestFitSearchPoint(current.x+1, current.y, getDistance([current.x+1, current.y], current_destination)),
            bestFitSearchPoint(current.x, current.y-1, getDistance([current.x, current.y-1], current_destination))
        ]

        for neighbor in neighbors:
            x, y = neighbor.x, neighbor.y
            if x>=0 and y>=0 and x<grid_rows and y<grid_columns and grid[x][y]!=1 and not(visited[x][y]):
                heapq.heappush(q, neighbor)
                parent_to_children[neighbor.x*grid_columns+neighbor.y] = current.x*grid_columns+current.y
                visited[x][y] = 1
                time.sleep(movement_time)

        path_point = current_destination[0]*grid_columns + current_destination[1]
        while (parent_to_children.get(path_point)):
            parent = parent_to_children[path_point]
            if parent != current_source[0]*grid_columns + current_source[1]:
                grid_view.create_rectangle((parent//grid_columns)*cell_size, (parent%grid_columns)*cell_size, (parent//grid_columns)*cell_size+cell_size, (parent%grid_columns)*cell_size+cell_size, fill="yellow", outline="black")
                grid_view.update_idletasks()
            path_point = parent


def start_visualization(algorithm_options, grid_view):

    searching_algorithm = algorithm_options.get()

    if (searching_algorithm == "DFS Search"):
        dfs_search(grid_view, current_source.copy())
    elif (searching_algorithm == "BFS Search"):
        bfs_search(grid_view, current_source.copy())
    elif (searching_algorithm == "A* Search"):
        a_star_search(grid_view, current_source.copy())
    else:
        best_first_search(grid_view, current_source.copy())


def reset(grid_view):

    global grid, visited

    for i in range(grid_rows):
        for j in range(grid_columns):
            visited[i][j] = 0

    visited[current_source[0]][current_source[1]] = 1

    create_grid(grid_view)


def main():

    """ ------------------------------------ Tkinter window variables --------------------------------- """
    root = Tk()

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.geometry("+50+50")

    """ ------------------------------- Heading of the visualizer -------------------------------- """
    heading = Label(root, text=heading_text, height=2, font=("Courier", 20, "bold"))
    heading.grid(row=0, column=0, sticky="nsew")

    """ ---------------- Menu to choose which algorithm we are going to run ------------------- """
    menu_bar = Frame(root, height=5, background="green")
    menu_bar.grid(row=1, column=0)

    algorithm_options = StringVar()
    algorithm_options.set("DFS Search")

    algorithm_option_values = ["DFS Search", "BFS Search", "A* Search", "Best First Search"]

    algorithm_dropdown = OptionMenu(menu_bar, algorithm_options, *algorithm_option_values)
    algorithm_dropdown.grid(row=0, column=0, sticky="nsew")

    point_options = StringVar()
    point_options.set("Wall")

    point_option_values = ["Source", "Destination", "Free Space", "Wall"]

    point_dropdown = OptionMenu(menu_bar, point_options, *point_option_values)
    point_dropdown.grid(row=0, column=1, sticky="nsew")

    """ -------------------------------------- Main Grid View --------------------------------------"""
    grid_view = Canvas(root, width=grid_columns*cell_size, height=grid_rows*cell_size)
    grid_view.grid(row=2, column=0, sticky="nsew")

    create_grid(grid_view)

    grid_view.bind("<Button-1>", lambda event: draw(event, grid_view, point_options))
    grid_view.bind("<B1-Motion>", lambda event: draw(event, grid_view, point_options))

    """ --------------------------------- Button container  ------------------------------------- """
    button_container = Frame(root, height=5)
    button_container.grid(row=3, column=0)

    start_button = Button(button_container, text="Start", width=10, bg="green", fg="white", font=("courier", 10, "bold"), command = lambda : start_visualization(algorithm_options, grid_view))
    start_button.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    reset_button = Button(button_container, text="Reset", width=10, bg="blue", fg="white", font=("courier", 10, "bold"), command = lambda : reset(grid_view))
    reset_button.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")

    root.mainloop()


if __name__=="__main__":
    main()
