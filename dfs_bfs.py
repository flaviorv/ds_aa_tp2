class DirectedGraph():
    def __init__(self):
        self.vertices = [i for i in range(1, 7)]
        self.adjacency_matrix = [[0 for _ in range(len(self.vertices))] for _ in range(len(self.vertices))]

    def add_edge(self, origin, destination):
        self.adjacency_matrix[origin-1][destination-1] = 1

    def dfs(self, vertex, visiteds=None):
        if visiteds is None:
            print("DFS", end=" ")
            visiteds = set()
        print(vertex, end=" ")
        visiteds.add(vertex)
        row = self.adjacency_matrix[vertex-1]
        for column in range(len(row)):
            if row[column] == 1 and column+1 not in visiteds:
                self.dfs(column+1, visiteds)

    def bfs(self, start):
        print("BFS", end=" ")
        visiteds = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visiteds:
                print(vertex, end=" ")
                visiteds.add(vertex)
                row = self.adjacency_matrix[vertex-1]
                queue.extend([column+1 for column in range(len(row)) if row[column] == 1])

if __name__ == "__main__":
    edges = [(1, 2), (1, 3), (2, 4), (3, 5), (4, 6), (5, 6)]
    graph = DirectedGraph()
    for origin, destination in edges:
        graph.add_edge(origin, destination)
    print("Adjacency Matrix")
    for row in graph.adjacency_matrix:
        print(row)
    graph.dfs(1)
    graph.bfs(1)
    print()