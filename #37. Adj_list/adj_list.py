class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = { v:[] for v in range(vno)}

    def add_edge(self, u, v, weight=1):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print("Invalid Graph")

    def has(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v < self.vertex_count:
            return any(vertex == v for vertex, x in self.adj_list[u])

    def remove(self, u, v):
        if 0 <= u < self.vertex_count and 0 <= v.self.vertex_count:
            self.adj_list[u] = [(vertex, weight)
                                for vertex, weight in self.adj_list[u] if vertex != v]
            self.adj_list[v] = [(vertex, weight)
                                for vertex, weight in self.adj_list[v] if vertex != u]
        else:
            print("invalid graph")

    def print_list(self):
        for vertex, n in self.adj_list.items():
            print("v", vertex, ":", n)

g1=Graph(6)

g1.add_edge(0,1)
g1.add_edge(0,2)
g1.add_edge(0,4)
g1.add_edge(2,4)
g1.add_edge(4,5)
g1.add_edge(5,3)
g1.add_edge(3,1)
g1.add_edge(0,3)

g1.print_list()

print("cheack has vale in ",g1.has(4,5))