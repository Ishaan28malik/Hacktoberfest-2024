class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \t Distance from source")
        for node in range(self.V):
            print(node, "\t", dist[node])


    def minDistance(self, dist, sptSet):
        minimum = float('inf')
        min_index = 0
        for v in range(self.V):
            if dist[v] < minimum and sptSet[v] == False:
                minimum = dist[v]
                min_index = v

        return min_index

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and sptSet[v] == False \
                   and dist[v] > dist[u] + self.graph[u][v]:
                        dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)

        
g = Graph(10)
g.graph = [[0, 4, 0, 0, 8, 0, 0, 0, 0, 0],
           [0, 0, 8, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 5, 0, 0, 0, 6, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 10, 0],
           [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 2, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 10, 0, 0, 5, 0],
           [0, 0, 0, 0, 0, 0, 4, 0, 0, 8],
           [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
g.dijkstra(0)
