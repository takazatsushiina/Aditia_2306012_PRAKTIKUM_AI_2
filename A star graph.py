from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    g_cost = {start: 0}

    while not frontier.empty():
        current_cost, current_node = frontier.get()

        if current_node == goal:
            print("Simpul tujuan ditemukan!")
            return True

        explored.add(current_node)

        for neighbour in graph[current_node]:
            cost = graph[current_node][neighbour]
            new_g_cost = g_cost[current_node] + cost

            if neighbour not in explored or new_g_cost < g_cost.get(neighbour, float('inf')):
                g_cost[neighbour] = new_g_cost
                total_cost = new_g_cost + heuristic[neighbour]
                frontier.put((total_cost, neighbour))

    print("Simpul tujuan tidak ditemukan!")
    return False

# Contoh data uji
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 2},
    'C': {'D': 4},
    'D': {}
}

heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 0
}

# Memanggil fungsi A* Search
a_star_search(graph, 'A', 'D', heuristic)
