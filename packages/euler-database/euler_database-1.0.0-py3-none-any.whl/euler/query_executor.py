"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
import re
class QueryExecutor:
    def __init__(self, graph):
        self.graph = graph

    def execute_query(self, query):
        """
        Execute a query to extract relations from the graph data.
        Args:
            query (str): The query string.
        Returns:
            list: A list of relations extracted from the graph data based on the query.
        """
        query_parts = query.split()
        if query_parts[0].lower() == "find":
            # Extract the node or relation to find
            if len(query_parts) >= 4 and query_parts[1].lower() == "all" and query_parts[2].lower() == "relations" and query_parts[3].lower() == "related":
                if len(query_parts) >= 5:
                    node_id = query_parts[4]
                    # Query the graph to find all relations related to the specified node
                    if node_id in self.graph.node_index:
                        return self.graph.get_edges_by_node(node_id)
                    else:
                        return f"Error: Node with ID {node_id} not found in the graph."
                else:
                    return "Error: Node ID not provided in the query."
            elif len(query_parts) >= 8 and query_parts[1].lower() == "all" and query_parts[2].lower() == "relations" and query_parts[3].lower() == "where" and query_parts[4].lower() == "a":
                if len(query_parts) >= 9:
                    source_label = query_parts[5].capitalize()
                    relation_label = query_parts[6]
                    target_label = query_parts[7].capitalize()
                    # Query the graph to find all relations based on source and target labels
                    edges = []
                    for edge in self.graph.edges.values():
                        source_node = self.graph.get_node(edge.source)
                        target_node = self.graph.get_node(edge.target)
                        if source_node and target_node and source_node.label == source_label and target_node.label == target_label and edge.label == relation_label:
                            edges.append(edge)
                    return edges
                else:
                    return "Error: Incomplete query format. Example of a valid query: 'Find all relations where a person lives in a city'"
            else:
                return "Error: Invalid query format. Example of a valid query: 'Find all relations related to node with ID 3'"
        else:
            return "Error: Unsupported query type. Currently, only 'find' queries are supported."



    