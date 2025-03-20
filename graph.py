from random import sample
import sys
class DirectedGraph():
    def __init__(self, len=1000):
        self.vertices = [str(f"Vertex {i}") for i in range(len)]
        self.adjacency_list = {}
        self.adjacency_matrix = [[0 for _ in range(len)] for _ in range(len)]
   
    def random_edges(self, edges):
        count = 0
        while count < edges:
            s = sample(self.vertices, 2)
            vertex1, vertex2 = s[0], s[1]
            if vertex1 > vertex2:
                vertex1, vertex2 = vertex2, vertex1
            self.add_edge(vertex1, vertex2)
            count += 1

    def add_edge(self, origin, destination):
        if origin not in self.adjacency_list:
            self.adjacency_list[origin] = {}
        if destination not in self.adjacency_list[origin]:
            self.adjacency_list[origin][destination] = f"{origin} => {destination}"
            index1, index2 = self.vertices.index(origin), self.vertices.index(destination)
            self.adjacency_matrix[index1][index2] = 1
            
    def show_edges(self):
        print("Adjacency list")
        [print(neighbors) for neighbors in self.adjacency_list.items()]
        print("\nAjacency matrix")
        [print(list) for list in self.adjacency_matrix]

    def find_all_matrix_edges(self):
        edges = []
        iterations = 0
        vertices = self.vertices
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                iterations += 1
                if self.adjacency_matrix[i][j] == 1:
                    edges.append([i,j])
        if edges:
            print(f"All matrix edges: {[f"{vertices[indexes[0]]} => {vertices[indexes[1]]}" for indexes in edges]} Iterations = {iterations}")
        else:
            print("No edges")

    def find_all_list_edges(self):
        iterations = 0
        edges = []
        for vertex in self.adjacency_list:
            for neighbor in self.adjacency_list[vertex]:
                edges.append([vertex, neighbor])
                iterations +=1
        print(f"All list edges: {[f"{indexes[0]} => {indexes[1]}" for indexes in edges]} Iterations = {iterations}")

    def search_matrix_edge(self, origin, destination):
        iterations = 0
        response = f"Is edge ({origin} => {destination}) in the adjacency matrix? "
        origin_index, destination_index = -1, -1
        for i in range(len(self.vertices)):
            iterations += 1
            if self.vertices[i] == origin:
                origin_index = i
            if self.vertices[i] == destination:
                destination_index = i
            if origin_index != -1 and destination_index != -1:
                break
        if self.adjacency_matrix[origin_index][destination_index] == 1:
            response += f"True - Iterations {iterations}"
            print(response)
        else:
            response += f"False - Iterations {iterations}"
            print(response)

    def search_list_edge(self, origin, destination):
        response = f"Is edge ({origin} => {destination}) in the adjacency list? "
        try:
            self.adjacency_list[origin][destination]
            response += f"True - Iterations 1"   
            print(response)     
        except:
            response += f"False - Iterations 1"
            print(response)
    
    def elements_size(self):
        print("Edge size:")
        element = self.adjacency_matrix[0][0]
        print(f"Element matriz {element}: {sys.getsizeof(element)} bytes Type: {type(element)}")
        element = list(self.adjacency_list.keys())[0]
        print(f"Element list {element}: {sys.getsizeof(element)} bytes Type: {type(element)}")

if __name__ == "__main__":
    graph = DirectedGraph(1000)
    graph.add_edge("Vertex 0", "Vertex 999")
    graph.add_edge("Vertex 7", "Vertex 3")
    # graph.show_edges()
    # graph.elements_size()
    graph.find_all_matrix_edges()
    graph.find_all_list_edges()
    graph.search_matrix_edge("Vertex 0", "Vertex 999")
    graph.search_matrix_edge("Vertex 7", "Vertex 3")
    graph.search_list_edge("Vertex 0", "Vertex 999")
    graph.search_list_edge("Vertex 7", "Vertex 3")
    graph.search_matrix_edge("Vertex 1", "Vertex 999")
    graph.search_list_edge("Vertex 1", "Vertex 999")