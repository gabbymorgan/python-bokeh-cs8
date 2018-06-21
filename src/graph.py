class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, color, **pos):
        self.value = value
        self.color = color
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex(0, 'red', x=40, y=40)
        debug_vertex_2 = Vertex(1, 'blue', x=140, y=140)
        debug_vertex_3 = Vertex(2, 'green', x = 300, y = 400)
        debug_vertex_4 = Vertex(3, 'orange', x = 400, y = 450)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_edge_2 = Edge(debug_vertex_3)
        debug_edge_3 = Edge(debug_vertex_4)
        debug_edge_4 = Edge(debug_vertex_1)

        debug_vertex_1.edges.append(debug_edge_1)
        debug_vertex_2.edges.append(debug_edge_2)
        debug_vertex_3.edges.append(debug_edge_3)
        debug_vertex_4.edges.append(debug_edge_4)
        
        self.vertexes += [debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4]