class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)

    def dfs(self, vertex, visiteds=None):
        if visiteds is None:
            visiteds = set()
        print(vertex, end=" ")
        visiteds.add(vertex)
        for neighbor in self.adjacency_list[vertex]:
            if neighbor not in visiteds:
                self.dfs(neighbor, visiteds)

if __name__ == "__main__":
    graph = Graph()
    edges = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "E")]
    for v1, v2 in edges:
        graph.add_edge(v1,v2)
    print("DFS")
    graph.dfs("A")
    print()
