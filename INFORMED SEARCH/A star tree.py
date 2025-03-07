from queue import PriorityQueue

def a_star_search(graph, heuristic, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))  # Memasukkan start node dengan prioritas heuristik
    explored = set()

    while not frontier.empty():
       current_node = frontier.get()  # Ambil simpul dengan prioritas terendah

        if current_node == goal:
            print("Simpul tujuan ditemukan!")
            return True

        explored.add(current_node)

        for neighbour in graph[current_node]:
          if neighbour not in explored:
            priority = heuristic[neighbour] + graph[current_node][neighbour]
            frontier.put((priority, neighbour))

    print("Simpul tujuan tidak ditemukan!")
    return False


heuristic = {
    'A': 9,
    'B': 4,
    'C': 2,
    'D': 5,
    'E': 3,
    'S': 7,
    'G': 0
}

graph = {
    'S': {'A': 3, 'E': 2},
    'A': {'B': 3, 'C': 4},
    'B': {'D': 5},
    'C': {'G': 7},
    'D': {'G': 3},
    'E': {'D': 6}
}

start_node = 'S'
goal_node = 'G'

a_star_search(graph, heuristic, start_node, goal_node)
