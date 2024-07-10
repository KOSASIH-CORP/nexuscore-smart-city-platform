import networkx as nx

class NetworkArchitecture:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node_id):
        self.graph.add_node(node_id)

    def add_edge(self, node1_id, node2_id):
        self.graph.add_edge(node1_id, node2_id)

    def get_shortest_path(self, node1_id, node2_id):
        return nx.shortest_path(self.graph, node1_id, node2_id)
