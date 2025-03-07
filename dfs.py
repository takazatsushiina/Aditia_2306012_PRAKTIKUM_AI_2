from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited.add(v)
        print(v, end=' ')  # Tambahkan spasi untuk output yang lebih rapi

        for neighbour in self.graph[v]:  # Perbaiki `self.grph` menjadi `self.graph`
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)

    def DFS(self, v):
        visited = set()
        self.DFSUtil(v, visited)

if __name__ == "__main__":  # Perbaiki kesalahan penulisan
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)  # Perbaiki kesalahan pemanggilan `addEdge`
    g.addEdge(1, 2)  # Perbaiki typo `addEgde`
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Berikut adalah penelusuran Depth First Search (dimulai dari node 2):")
    g.DFS(2)
