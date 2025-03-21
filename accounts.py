class Graph:
    def __init__(self):
        self.transfers = {}
    
    def add_transfer(self, origin, destination, value):
        if origin not in self.transfers:
            self.transfers[origin] = {}
        self.transfers[origin][destination] = value
        
    def _dfs(self, node, visited, stack, path):
        visited[node] = True
        stack[node] = True
        path.append(node)
        for neighbor in self.transfers.get(node, []):
            if not visited.get(neighbor, False):
                self._dfs(neighbor, visited, stack, path)
            elif stack.get(neighbor, False):
                path.append(neighbor)
                print("Cycle found:", " -> ".join(path))
                self._check_values(path)
        stack[node] = False
        path.pop()
    
    def _check_values(self, path, tolerance=0.2, high_value_threshold=100000):
        cycle_values = []
        for i in range(len(path) - 1):
            origin, destination = path[i], path[i + 1]
            if origin in self.transfers and destination in self.transfers[origin]:
                cycle_values.append(self.transfers[origin][destination])
        if cycle_values:
            avg_value = sum(cycle_values) / len(cycle_values)
            values_similar = all(abs(val - avg_value) <= avg_value * tolerance for val in cycle_values)
            high_value = avg_value > high_value_threshold
            print(f"Similar values: {values_similar}  High Value: {high_value}")    
            
    def search_cycles(self):
        visited = {}
        stack = {}
        for node in self.transfers:
            if not visited.get(node, False):
                self._dfs(node, visited, stack, [])
            
if __name__ == "__main__":
    graph = Graph()
    graph.add_transfer("A", "B", 100000)
    graph.add_transfer("B", "C", 120000)
    graph.add_transfer("C", "D", 1230)
    graph.add_transfer("C", "E", 132000)
    graph.add_transfer("E", "F", 113000)
    graph.add_transfer("F", "G", 112000)
    graph.add_transfer("G", "C", 110000)
    graph.search_cycles()
