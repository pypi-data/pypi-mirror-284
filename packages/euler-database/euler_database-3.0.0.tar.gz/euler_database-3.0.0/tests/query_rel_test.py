class Node:
    def __init__(self, node_id, label, properties):
        self.node_id = node_id
        self.label = label
        self.properties = properties

    def to_dict(self):
        return {"id": self.node_id, "label": self.label, "properties": self.properties}

class Edge:
    def __init__(self, edge_id, source, target, label, properties):
        self.edge_id = edge_id
        self.source = source
        self.target = target
        self.label = label
        self.properties = properties

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def add_node(self, node):
        print(f"Adding node: {node.to_dict()}")
        self.nodes[node.node_id] = node

    def add_edge(self, edge):
        print(f"Adding edge: {edge.__dict__}")
        self.edges[edge.edge_id] = edge

    def get_node(self, node_id):
        return self.nodes.get(node_id)

    def get_edges_by_type(self, edge_type):
        return [edge for edge in self.edges.values() if edge.label == edge_type]

    def to_dict(self):
        return {
            "nodes": [node.to_dict() for node in self.nodes.values()],
            "edges": [{"id": edge.edge_id, "source": edge.source, "target": edge.target, "label": edge.label, "properties": edge.properties} for edge in self.edges.values()]
        }

class QueryParser:
    def __init__(self, graph):
        self.graph = graph

    def parse(self, query):
        queries = query.split(';')
        results = []
        for single_query in queries:
            single_query = single_query.strip()
            if single_query.startswith("CREATE"):
                if "->" in single_query:
                    self._parse_create_relationship_query(single_query)
                else:
                    self._parse_create_node_query(single_query)
            elif single_query.startswith("MATCH"):
                results.append(self._parse_match_query(single_query))
        return results

    def _parse_create_node_query(self, query):
        import re
        node_pattern = re.compile(r'CREATE \((\w+):(\w+) \{([^}]+)\}\)')
        match = node_pattern.match(query)
        if match:
            node_id, label, properties = match.groups()
            properties_dict = self._parse_properties(properties)
            self.graph.add_node(Node(node_id, label, properties_dict))

    def _parse_create_relationship_query(self, query):
        import re
        relationship_pattern = re.compile(r'CREATE \((\w+)\)-\[:(\w+) \{([^}]+)\}\]->\((\w+)\)')
        match = relationship_pattern.match(query)
        if match:
            source, label, properties, target = match.groups()
            properties_dict = self._parse_properties(properties)
            edge_id = f"{source}_{target}_{label}"
            self.graph.add_edge(Edge(edge_id, source, target, label, properties_dict))

    def _parse_match_query(self, query):
        import re
        match_pattern = re.compile(r'MATCH \((\w+):(\w+)\)-\[:(\w+)\]->\((\w+):(\w+)\) RETURN (.+)')
        match = match_pattern.match(query)
        if match:
            return match.groups()
        return None

    def _parse_properties(self, properties_str):
        properties = {}
        for prop in properties_str.split(','):
            key, value = prop.split(':')
            properties[key.strip()] = value.strip().strip('"')
        return properties

class QueryExecutor:
    def __init__(self, graph):
        self.graph = graph

    def execute_query(self, query):
        parser = QueryParser(self.graph)
        parsed_queries = parser.parse(query)
        results = []
        for parsed_query in parsed_queries:
            if parsed_query and isinstance(parsed_query, tuple):
                results.extend(self._execute_match_query(parsed_query))
        return results

    def _execute_match_query(self, parsed_query):
        node1_id, node1_label, rel_label, node2_id, node2_label, return_statement = parsed_query
        print(f"Parsed MATCH query: node1_id={node1_id}, node1_label={node1_label}, rel_label={rel_label}, node2_id={node2_id}, node2_label={node2_label}, return_statement={return_statement}")
        result = []
        for edge in self.graph.get_edges_by_type(rel_label):
            print(f"Evaluating edge: {edge.__dict__}")
            node1 = self.graph.get_node(edge.source)
            node2 = self.graph.get_node(edge.target)
            print(f"node1: {node1.to_dict() if node1 else 'None'}, node2: {node2.to_dict() if node2 else 'None'}")
            if node1 and node2 and node1.label == node1_label and node2.label == node2_label:
                result.append({return_statement: (node1.to_dict(), node2.to_dict())})
        print(f"Result: {result}")
        return result

# Initialize graph
graph = KnowledgeGraph()
parser = QueryParser(graph)
executor = QueryExecutor(graph)

# Run creation queries
creation_queries = """
CREATE (n1:Person {name: "Rajesh", age: "30"});
CREATE (n2:Person {name: "Vinod", age: "35"});
CREATE (n3:Person {name: "Prashant", age: "35"});
CREATE (n1)-[:KNOWS {since: "2020"}]->(n2);
CREATE (n2)-[:KNOWS {since: "2019"}]->(n3);
CREATE (n3)-[:KNOWS {since: "2021"}]->(n1);
"""
parser.parse(creation_queries)

# Correct MATCH query to match two Person nodes
match_query = "MATCH (p1:Person)-[:KNOWS]->(p2:Person) RETURN p1, p2;"
result = executor.execute_query(match_query)
print(result)


match_query_1 = 'MATCH (Person)-[:knows]->(Friend) RETURN *'
result = executor.execute_query(match_query_1)
print(result)

# Print updated graph structure
# print(graph.to_dict())


def parse_match(self, query):
    # Pattern for MATCH without properties
    match_pattern_simple = r"MATCH\s+\((\w+):(\w+)\)\s*-\[:(\w+)\]->\s*\((\w+):(\w+)\)\s*RETURN\s+(.+)"

    # Pattern for MATCH with properties
    match_pattern_with_props = r"MATCH\s+\((\w+):(\w+)\s*{\s*(.*?)\s*}\)\s*-\[:(\w+)\s*{\s*(.*?)\s*}\]->\s*\((\w+):(\w+)\s*{\s*(.*?)\s*}\)\s*RETURN\s+(.+)"

    # Attempt to match using the pattern for MATCH without properties
    match = re.match(match_pattern_simple, query)
    if match:
        source_var, source_label, rel_type, target_var, target_label, return_clause = match.groups()
        source_nodes = self.graph.get_nodes_by_label(source_label)
        target_nodes = self.graph.get_nodes_by_label(target_label)
        edges = self.graph.get_edges_by_type(rel_type)

        filtered_edges = [
            edge for edge in edges
            if self.graph.get_node(edge.source) in source_nodes
            and self.graph.get_node(edge.target) in target_nodes
        ]

        results = {
            source_var: [self.graph.get_node(edge.source) for edge in filtered_edges],
            target_var: [self.graph.get_node(edge.target) for edge in filtered_edges],
            "edges": filtered_edges if return_clause == "edges" else None  # Using "e" as alias for edges
        }

        if return_clause:
            if results[source_var] or results[target_var] or results["edges"]:
                return self.parse_return_clause(return_clause, results)
            else:
                return "No matching nodes or edges found."
        else:
            return results

    # Attempt to match using the pattern for MATCH with properties
    match = re.match(match_pattern_with_props, query)
    if match:
        source_var, source_label, source_props, rel_type, rel_props, target_var, target_label, target_props, return_clause = match.groups()
        source_props = self.parse_properties(source_props)
        target_props = self.parse_properties(target_props)
        rel_props = self.parse_properties(rel_props)

        source_nodes = self.graph.get_nodes_by_label(source_label)
        target_nodes = self.graph.get_nodes_by_label(target_label)
        edges = self.graph.get_edges_by_type(rel_type)

        filtered_source_nodes = [node for node in source_nodes if self.match_properties(node.properties, source_props)]
        filtered_target_nodes = [node for node in target_nodes if self.match_properties(node.properties, target_props)]
        filtered_edges = [
            edge for edge in edges
            if self.match_properties(edge.properties, rel_props)
            and any(source_node.id == edge.source for source_node in filtered_source_nodes)
            and any(target_node.id == edge.target for target_node in filtered_target_nodes)
        ]

        results = {
            source_var: filtered_source_nodes,
            target_var: filtered_target_nodes,
            "e": filtered_edges if return_clause == "e" else None  # Using "e" as alias for edges
        }

        if return_clause:
            if results[source_var] or results[target_var] or results["e"]:
                return self.parse_return_clause(return_clause, results)
            else:
                return "No matching nodes or edges found."
        else:
            return results

    return "Error: Invalid MATCH query format."

