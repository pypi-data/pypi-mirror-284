"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
from euler.path_finding.base_pathfinding import BasePathFinder

class DijkstraPathFinder(BasePathFinder):
    def find_path(self, start_node, end_node):
        if self.library == 'networkx':
            return nx.dijkstra_path(self.graph, start_node, end_node)
        elif self.library == 'igraph':
            start_idx = self.graph.vs.find(name=start_node).index
            end_idx = self.graph.vs.find(name=end_node).index
            path = self.graph.get_shortest_paths(start_idx, to=end_idx, weights='weight', mode=ig.OUT)
            return [self.graph.vs[idx]['name'] for idx in path[0]]
        elif self.library == 'graph_tool':
            start_idx = int(start_node)
            end_idx = int(end_node)
            weight_map = self.graph.ep['weight']
            _, pred_map = gt.shortest_path(self.graph, source=self.graph.vertex(start_idx), target=self.graph.vertex(end_idx), weights=weight_map)
            path = []
            v = self.graph.vertex(end_idx)
            while v is not None:
                path.append(int(v))
                v = pred_map[v]
            return path[::-1]
        else:
            raise ValueError("Unsupported library. Choose from 'networkx', 'igraph', or 'graph_tool'.")
