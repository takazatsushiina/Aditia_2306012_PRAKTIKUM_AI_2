from posixpath import curdir
from queue import PriorityQueue

def a_star_search(graph, start, goal, heuristic):
  frontier = PriorityQueue()
  frontier.put((0, start))
  explored = set()

  while not frontier.empty():
    current_node = frontier.get()

    if current_node == goal:
      print("Simpul tujuan ditemukan!")
      return True

    explored.add(current_node)

    for neighbour in graph[current_node]:
      cost = graph[current_node][neighbour]
      heuristic_cost = heuristic[neighbour]
      total_cost = cost + heuristic_cost

      if neighbour not in explored:
        frontier.put((total_cost, neighbour))

  print("Simpul tujuan tidak ditemukan!")
  return False
