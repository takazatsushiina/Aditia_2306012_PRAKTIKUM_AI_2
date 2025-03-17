from queue import PriorityQueue

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)
    path.reverse()
    return path

def greedy_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))
    came_from = {}
    explored = set()

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("simpul tujuan ditemukan!")
            path = reconstruct_path(came_from, start, goal)
            print("jalur terpendek:", path)
            return path

        explored.add(current_node)

        for neighbor in graph.get(current_node, []):
            if neighbor not in explored:
                frontier.put((heuristic[neighbor], neighbor))
                came_from[neighbor] = current_node

    print("simpul tujuan tidak ditemukabn.")
    return None

heuristic = {
    'A': 4, 'B': 3, 'C': 3, 'D': 1, 'S': 6, 'G': 0
}

graph = {
    'S': {'A': 3, 'B': 2},
    'A': {'D': 5, 'B': 1},
    'B': {'C': 2, 'D': 3},
    'C': {'D': 3, 'G': 4},
    'D': {'G': 1}
}

start_node = 'S'
goal_state = 'G'

greedy_search(graph, start_node, goal_state, heuristic)
