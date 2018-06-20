import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, LabelSet
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()
print(graph_data.vertexes)

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
    color_list.append(vertex.color)

values = [x.value for x in graph_data.vertexes]
print(values)

debug_pallete = Spectral8
debug_pallete.append('#ff0000')
debug_pallete.append('#0000ff')

plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.data_source.add(values, 'value')
graph.node_renderer.glyph = Oval(name='value', height=10, width=10, fill_color='color')

# labels = LabelSet(x='weight', y='height', text='names', level='glyph',
#               x_offset=5, y_offset=5, source=source, render_mode='canvas')

graph.edge_renderer.data_source.data = dict(
    start=node_indices,
    end=[graph_data.vertexes[x].edges[0].destination.value for x in node_indices])

### start of layout code
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)