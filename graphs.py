class Graph:
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            adj_vertices = self.adj_list[vertex]
            for adj_vertex in adj_vertices:
                self.adj_list[adj_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False


print("--------------------------Graphs ---------------------------------")
graph = Graph()
graph.print_graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.print_graph()
print("------------------------Add edge ops----------------------------------")
print(graph.add_edge('A', 'B'))
graph.print_graph()
print(graph.add_edge('A', 'C'))
graph.print_graph()
print("----------------------- Remove edge ops-----------------------------------")
print(graph.remove_edge('A', 'B'))
graph.print_graph()
print("---------------------------- Remove vertex ops-----------------------------")
print(graph.add_edge('A', 'B'))
graph.print_graph()
print(graph.remove_vertex('A'))
graph.print_graph()