class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add(self, city):
        if city not in self.adjacency_list:
            self.adjacency_list[city] = {}

    def connect(self, city1, city2, distance):
        if city1 not in self.adjacency_list:
            self.adjacency_list[city1] = {}
        if city2 not in self.adjacency_list:
            self.adjacency_list[city2] = {}
        self.adjacency_list[city1][city2] = distance
        self.adjacency_list[city2][city1] = distance 

    def bfs(self, start):
        print("BFS")
        visiteds = set()
        queue = [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visiteds:
                print(vertex, end=" ")
                visiteds.add(vertex)
                queue.extend(self.adjacency_list[vertex])
        print() 

if __name__ == "__main__":
    from random import randint
    graph = Graph()
    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "E"),
        ("D", "F"),
        ("E", "F")
    ]
    roads = [(city1, city2, randint(10, 100)) for city1, city2 in edges]
    for c1, c2, km in roads:
        graph.connect(c1, c2, km)
    print("Adjacency List")
    [print(city, neighbors)  for city, neighbors in graph.adjacency_list.items()]
    graph.bfs("A")