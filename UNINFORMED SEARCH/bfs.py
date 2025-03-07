import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Tambahkan spasi agar output lebih rapi

        for neighbour in graph[vertex]:  # Cek hanya yang belum dikunjungi
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}  # Graph tetap sama
    print("Following is Breadth First Traversal:")
    bfs(graph, 0)
