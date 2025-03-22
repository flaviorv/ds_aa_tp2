class Graph():
    def __init__(self):
        self.adjacency_list = {}

    def connect(self, neighborhood1, neighborhood2):
        if neighborhood1 not in self.adjacency_list:
            self.adjacency_list[neighborhood1] = []
        if neighborhood2 not in self.adjacency_list:
            self.adjacency_list[neighborhood2] = []
        self.adjacency_list[neighborhood1].append(neighborhood2)
        self.adjacency_list[neighborhood2].append(neighborhood1)

    def bfs(self, start, target):
        queue = [start] 
        visited = set([start]) 
        predecessor = {start: None}
        while queue:
            vertex = queue.pop(0)
            if vertex == target:
                path = []
                while vertex is not None:
                    path.append(vertex)
                    vertex = predecessor[vertex]
                print("Shortest path is:", path[::-1])
                return
            for neighbor in self.adjacency_list[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    predecessor[neighbor] = vertex
                    queue.append(neighbor)    
        print("No path")

if __name__ == "__main__":
    edges = [
        ("A", "B"), ("A", "C"),
        ("B", "E"), 
        ("C", "G"), ("C", "H"),
        ("D", "I"), ("D", "J"),
        ("E", "K"), ("E", "L"),
        ("F", "M"), ("G", "I"),
        ("H", "J"), ("K", "M"),
        ("L", "M"), ("B", "D"),
        ("F", "H"), ("G", "K")
    ]   
    graph = Graph()
    for v1, v2 in edges:
        graph.connect(v1, v2) 
    print("Adjacency List")
    for vertex, neighbors in graph.adjacency_list.items():
        print(f"{vertex}: {neighbors}")
    graph.bfs("A", "F")