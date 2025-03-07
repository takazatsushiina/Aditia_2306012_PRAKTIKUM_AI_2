from queue import PriorityQueue

def greedy_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))  # Memasukkan start node dengan prioritas heuristik
    explored = set()

    while not frontier.empty():
        _, current_node = frontier.get()  # Mengambil node dengan prioritas terendah

        print(f"Memeriksa simpul: {current_node}")  # Untuk tracking jalannya algoritma

        if current_node == goal:
            print("Simpul tujuan sudah ditemukan!")
            return True 

        explored.add(current_node)

        for neighbour in graph.get(current_node, []):  # Menghindari error jika tidak ada tetangga
            if neighbour not in explored:
                priority = heuristic[neighbour]
                frontier.put((priority, neighbour))

    print("Simpul tujuan tidak ditemukan!")
    return False


# Definisi heuristik untuk setiap simpul
heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}  

# Representasi graf dengan adjacency list
graph = {
    'S': ['A', 'E'],
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['G'],
    'D': ['G'],
    'E': ['D']
}

# Simpul awal dan tujuan
start_node = 'S'
goal_node = 'G'

# Menjalankan pencarian
greedy_search(graph, start_node, goal_node)
