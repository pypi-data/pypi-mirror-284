"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
class AggregationManager:

    def __init__(self, graph):
        self.graph = graph

    def count(self, nodes):
        return len(nodes)

    def sum(self, nodes, property_name):
        return sum(int(node.properties[property_name]) for node in nodes if property_name in node.properties)

    def avg(self, nodes, property_name):
        values = [int(node.properties[property_name]) for node in nodes if property_name in node.properties]
        return sum(values) / len(values) if values else 0
    
    def min(self, nodes, property_name):
        return min(int(node.properties[property_name]) for node in nodes if property_name in node.properties)
    
    def max(self, nodes, property_name):
        return max(int(node.properties[property_name]) for node in nodes if property_name in node.properties)
