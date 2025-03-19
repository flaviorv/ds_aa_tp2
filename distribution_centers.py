class Graph:
    def __init__(self):
        self.distribution_centers = {}

    def add_center(self, center):
        if center not in self.distribution_centers:
            self.distribution_centers[center] = {}

    def add_route(self, center1, center2, average_time):
        if center1 not in self.distribution_centers:
            self.add_center(center1)
        if center2 not in self.distribution_centers:
            self.add_center(center2)
        self.distribution_centers[center1][center2] = average_time
        self.distribution_centers[center2][center1] = average_time

    def routes(self):
        for center in self.distribution_centers:
            path = self.distribution_centers[center]
            print(f"{center} routes: {[f"{destination}: {hours} hours" for destination, hours in path.items()]}")

    def bfs(self, origin, destination):
        result = f"Route: {origin}"
        total_time = 0
        visiteds = set()
        if origin not in self.distribution_centers:
            print(f"Origin {origin} not found")
            return
        while origin != destination:    
            visiteds.add(origin)
            min_time = None
            next_center = None
            for adjacent, time in self.distribution_centers[origin].items():
                if adjacent not in visiteds:
                    if not min_time:
                        min_time = time
                        next_center = adjacent
                    elif time < min_time:
                        min_time = time
                        next_center = adjacent
            if min_time == None:
                print(f"Destination {destination} not found")
                return
            total_time += min_time
            result += f" => {next_center}: {min_time} hours"
            origin = next_center
        result += f" Total time: {total_time} hours"
        print(result)

if __name__ == "__main__":
    routes = [("A", "B", 5), ("A", "C", 3), ("B", "D", 4), ("C", "E", 7), ("D", "E", 2)]
    graph = Graph()
    for center1, center2, average_time in routes:
        graph.add_route(center1, center2, average_time)
    graph.routes()
    graph.bfs("A", "B")
    graph.bfs("E", "A")
    graph.bfs("D", "F")
    graph.bfs("K", "B")
    