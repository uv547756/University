import sys

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.V):
            print(node, "\t", dist[node])

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1

        for u in range(self.V):
            if dist[u] < min and not sptSet[u]:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and not sptSet[y] and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]

        self.printSolution(dist)


if __name__ == "__main__":
    # Taking number of vertices as input
    vertices = int(input("Enter the number of vertices in the graph: "))
    g = Graph(vertices)

    # Taking adjacency matrix as input
    print("Enter the adjacency matrix row by row (enter 0 if there is no edge between vertices):")
    for i in range(vertices):
        g.graph[i] = list(map(int, input().split()))

    # Taking source vertex as input
    src = int(input("Enter the source vertex: "))

    g.dijkstra(src)
