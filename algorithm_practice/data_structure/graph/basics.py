# graph

# edge list
graph = [[0, 2], [2, 3], [2, 1], [1, 3]]

# adjacent list
graph = [[2], [2, 3], [0, 1, 3], [1, 2]]

# adjacent matrix
graph = [[0, 0, 1, 0],
        [0, 0, 1, 1],
        [1, 1, 0, 1],
        [0, 1, 1, 0]]

class Graph:
  def __init__(self):
    self.num_nodes = 0
    self.adj_list = {}
  
  def add_vertex(self, node):
    self.adj_list[node] = []
    self.num_nodes += 1
    
  def add_edge(self, node1, node2):
    self.adj_list[node1].append(node2)
    self.adj_list[node2].append(node1)

  def show_connections(self):
    for k, val in self.adj_list.items():
      print(k, '-->', val)


mygraph = Graph()
mygraph.add_vertex('0')
mygraph.add_vertex('1')
mygraph.add_vertex('2')
mygraph.add_vertex('3')
mygraph.add_vertex('4')
mygraph.add_vertex('5')
mygraph.add_vertex('6')
mygraph.add_edge('3', '1')
mygraph.add_edge('3', '4')
mygraph.add_edge('4', '2')
mygraph.add_edge('4', '5')
mygraph.add_edge('5', '6')
mygraph.add_edge('2', '1')
mygraph.add_edge('2', '0')
mygraph.add_edge('0', '1')
mygraph.show_connections()

