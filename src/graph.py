import random
import math

class Edge:
    def __init__(self, destination, weight=0):
        self.destination = destination
        self.weight = weight

class Vertex:
    def __init__(self, value=0, color='#000000', x=0, y=0):
        self.value = value
        self.color = color
        self.pos = {'x':x, 'y':y}
        self.edges = []

class Graph:
    def __init__(self):
        self.vertices = []

    def create_test_data(self):
        vertex_1 = Vertex(0, 'red', 40, 40)
        vertex_2 = Vertex(1, 'blue', 140, 140)
        vertex_3 = Vertex(2, 'green', 300, 400)
        vertex_4 = Vertex(3, 'orange', 400, 450)

        edge_1 = Edge(vertex_2)
        edge_2 = Edge(vertex_3)
        edge_3 = Edge(vertex_4)
        edge_4 = Edge(vertex_1)

        vertex_1.edges.append(edge_1)
        vertex_1.edges.append(edge_3)
        vertex_2.edges.append(edge_2)
        vertex_3.edges.append(edge_3)
        vertex_4.edges.append(edge_4)
        
        self.vertices += [vertex_1, vertex_2, vertex_3, vertex_4]


    def randomize(self, width, height, px_box, probability=0.6):
        def connect_vertices(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        count = 0
        
        # Build a grid of vertices

        grid = []
        for y in range(height):
            row = []
            for x in range(width):
                vert = Vertex(count)
                count += 1
                row.append(vert)
            grid.append(row)
        
        #Go through the grid randomly hooking up edges
        for y in range(height):
            for x in range(width):
                #connect down
                if (y < height - 1):
                    if (random.random() < probability):
                        connect_vertices(grid[y][x], grid[y+1][x])
                if (x < width - 1):
                    if (random.random() < probability):
                        connect_vertices(grid[y][x], grid[y][x+1])
        box_buffer = 0.8
        box_inner = px_box * box_buffer
        box_inner_offset = (px_box - box_inner) / 2

        for y in range(height):
            for x in range(width):
                grid[y][x].pos = {
                'x': (x * px_box + box_inner_offset + random.random() * box_inner),
                'y': (y * px_box + box_inner_offset + random.random() * box_inner)
                }
        
        # Finally, add everything in our grid to the dddddd in this Graph
        for y in range(height):
            for x in range(width):
                self.vertices.append(grid[y][x])

    def bfs(self, start):
        random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])        
        queue = []
        found = []
        queue.append(start)
        found.append(start)

        start.color = random_color
        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            queue.pop(0)
            print([v.value for v in found])

    def get_connected_components(self):
        components = []
        for vertex in self.vertices:
            if vertex not in components:
                components.append(self.bfs(vertex))