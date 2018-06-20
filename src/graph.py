class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos):
        self.value = value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex(0, x=40, y=40)
        debug_vertex_2 = Vertex(1, x=140, y=140)
        debug_vertex_3 = Vertex(2, x = 300, y = 400)
        debug_vertex_4 = Vertex(3, x = 400, y = 450)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_edge_2 = Edge(debug_vertex_3)
        debug_edge_3 = Edge(debug_vertex_4)
        debug_edge_4 = Edge(debug_vertex_1)

        debug_vertex_1.edges.append(debug_edge_2)
        debug_vertex_2.edges.append(debug_edge_4)
        debug_vertex_3.edges.append(debug_edge_3)
        debug_vertex_4.edges.append(debug_edge_1)
        
        self.vertexes += [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4]