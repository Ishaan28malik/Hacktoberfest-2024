import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        visited = [False] * self.V
        priority_queue = [(0, src)]

        while priority_queue:
            (dist_u, u) = heapq.heappop(priority_queue)

            if visited[u]:
                continue

            visited[u] = True

            for v, w in self.graph[u]:
                if not visited[v] and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(priority_queue, (dist[v], v))

        self.print_solution(dist)

    def print_solution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

g = Graph(10)
g.add_edge(0, 4, 8)
g.add_edge(1, 2, 8)
g.add_edge(2, 3, 5)
g.add_edge(3, 8, 10)
g.add_edge(4, 5, 1)
g.add_edge(5, 6, 2)
g.add_edge(7, 5, 10)
g.add_edge(8, 6, 4)
g.add_edge(9, 8, 8)

g.dijkstra(0)
