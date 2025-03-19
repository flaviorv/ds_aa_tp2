from random import sample

class WeightedGraph:
    def __init__(self):
        self.vertices = {}

    def add(self, neighborhood):
        if neighborhood not in self.vertices:
            self.vertices[neighborhood] = {}

    def connect(self, neighborhood1, neighborhood2, distance):
        self.vertices[neighborhood1][neighborhood2] = distance
        self.vertices[neighborhood2][neighborhood1] = distance 

    def dijkstra(self, origin, destination):
        unvisited = list(self.vertices.keys())
        distances = {neighbohood: float("inf") for neighbohood in self.vertices}
        distances[origin] = 0
        predecessors = {}
        while unvisited:
            current_neighborhood = min(unvisited, key=lambda neighbohood: distances[neighbohood])
            if distances[current_neighborhood] == float("inf"):
                break
            for adjacent, distance in self.vertices[current_neighborhood].items():
                new_distance = distances[current_neighborhood] + distance
                if new_distance < distances[adjacent]:
                    distances[adjacent] = new_distance
                    predecessors[adjacent] = current_neighborhood
            unvisited.remove(current_neighborhood)
        path = []
        current_neighborhood = destination
        while current_neighborhood in predecessors:
            path.append(current_neighborhood)
            current_neighborhood = predecessors[current_neighborhood]
        path.append(origin)
        path.reverse()
        return path, distances[destination]

if __name__ == "__main__":
    graph = WeightedGraph()
    neighborhoods = ["São José", "Santa Rita", "Três Marias", "São Sebastião", "Dona Lalá", "Alto dos Ypês"]
    for neighborhood in neighborhoods:
        graph.add(neighborhood)
    roads = [
        ("São José", "Alto dos Ypês", 6), ("São José", "Santa Rita", 4),
        ("Dona Lalá", "São José", 9), ("São Sebastião", "São José", 11),
        ("Três Marias", "Dona Lalá", 10), ("Três Marias", "São Sebastião", 5),
        ("São Sebastião", "Alto dos Ypês", 4)
    ]
    for neighborhood1, neighborhood2, distance in roads:
        graph.connect(neighborhood1, neighborhood2, distance)
    for _ in range(5):
        s = sample(neighborhoods, 2)
        origin = s[0]
        destination = s[1]
        path, distance = graph.dijkstra(origin, destination)
        print(f"Best path from {origin} to {destination}: ({' => '.join(path)}) Distance: {distance} km")
