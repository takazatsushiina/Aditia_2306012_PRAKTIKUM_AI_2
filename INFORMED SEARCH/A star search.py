
from os import path
from queue import PriorityQueue

def a_star_tree_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    path = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Simpul tujuan ditemukan!")
            route = reconstruct_path(path, start, goal)
            print("Jalur optimal:", route)
            return True

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            cost_so_far[neighbor] = new_cost
            priority = new_cost + heuristic[neighbor]
            frontier.put((priority, neighbor))
            path[neighbor] = current_node

    print("Simpul tujuan tidak ditemukan.")
    return False

def a_star_graph_search(graph, start, goal, heuristic):
    frontier = PriorityQueue()
    frontier.put((0, start))
    explored = set()
    path = {}
    cost_so_far = {start: 0}

    while not frontier.empty():
        _, current_node = frontier.get()

        if current_node == goal:
            print("Simpul tujuan ditemukan!")
            route = reconstruct_path(path, start, goal)
            print("Jalur optimal:", route)
            return True

        explored.add(current_node)

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if neighbor not in explored or new_cost < cost_so_far.get(neighbor, float('inf')):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                frontier.put((priority, neighbor))
                path[neighbor] = current_node

    print("Simpul tujuan tidak ditemukan.")
    return False

def reconstruct_path(path, start, goal):
    current = goal
    route = [current]
    while current != start:
        current = path[current]
        route.append(current)
    route.reverse()
    return route

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

a_star_tree_search(graph, start_node, goal_state, heuristic)
a_star_graph_search(graph, start_node, goal_state, heuristic)
