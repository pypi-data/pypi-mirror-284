"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import networkx as nx
import igraph as ig
import graph_tool.all as gt

class BasePathFinder:
    def __init__(self, library='networkx'):
        self.library = library
        if library == 'networkx':
            self.graph = nx.Graph()
        elif library == 'igraph':
            self.graph = ig.Graph()
        elif library == 'graph_tool':
            self.graph = gt.Graph()
        else:
            raise ValueError("Unsupported library. Choose from 'networkx', 'igraph', or 'graph_tool'.")

    def add_node(self, node):
        if self.library == 'networkx':
            self.graph.add_node(node)
        elif self.library == 'igraph':
            self.graph.add_vertex(name=node)
        elif self.library == 'graph_tool':
            self.graph.add_vertex()

    def add_edge(self, node1, node2, weight=1):
        if self.library == 'networkx':
            self.graph.add_edge(node1, node2, weight=weight)
        elif self.library == 'igraph':
            self.graph.add_edge(self.graph.vs.find(name=node1).index, self.graph.vs.find(name=node2).index, weight=weight)
        elif self.library == 'graph_tool':
            edge = self.graph.add_edge(node1, node2)
            self.graph.ep['weight'][edge] = weight
