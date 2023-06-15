import time


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.not_visited = [x for x in range(num_vertices)]
        self.visited = []
        self.D = [float('inf') for _ in range(num_vertices)]
        self.P = [None for _ in range(num_vertices)]

    def add_edge(self, source, destination, weight):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices:
            self.adj_matrix[source][destination] = weight

    def remove_edge(self, source, destination):
        if 0 <= source < self.num_vertices and 0 <= destination < self.num_vertices and source != destination:
            self.adj_matrix[source][destination] = 0
            self.adj_matrix[destination][source] = 0

    def dijkstra(self, source):
        self.D[source] = 0
        while self.not_visited:
            min_cost = float('inf')
            min_cost_vertex_index = 0
            for vertex_index in self.not_visited:
                if self.D[vertex_index] < min_cost:
                    min_cost = self.D[vertex_index]
                    min_cost_vertex_index = vertex_index
            self.not_visited.remove(min_cost_vertex_index)
            self.visited.append(min_cost_vertex_index)

            for vertex_index in range(self.num_vertices):
                if self.adj_matrix[min_cost_vertex_index][vertex_index] > 0 and vertex_index in self.not_visited:
                    if self.D[vertex_index] > self.D[min_cost_vertex_index] + self.adj_matrix[min_cost_vertex_index][
                        vertex_index]:
                        self.D[vertex_index] = self.D[min_cost_vertex_index] + self.adj_matrix[min_cost_vertex_index][
                            vertex_index]
                        self.P[vertex_index] = min_cost_vertex_index

        return self.D, self.P


g = Graph(6)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 2)
g.add_edge(2, 1, 1)
g.add_edge(2, 3, 3)
g.add_edge(3, 4, 1)
g.add_edge(3, 5, 5)
g.add_edge(4, 5, 2)

start_time = time.time()
distances, predecessors = g.dijkstra(0)
end_time = time.time()


print("################ GRAF W POSTACI MACIERZY SĄSIEDZTWA ################")
print("Koszty dojścia:")
for v in range(g.num_vertices):
    print(f"Wierzchołek {v}: {distances[v]}")

print(f"\nCzas wykonania: {end_time - start_time} seconds")
print("Reprezentacja: ", g.adj_matrix)
