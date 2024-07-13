import re
from euler.relationship import RelationshipManager
from euler.functional_tools.aggregation import AggregationManager
from euler.functional_tools.where_statement import WhereStatement
from euler.edge_node import Node, Edge
from euler.similarity.node_similarity import NodeSimilarity

class QueryParser:
    def __init__(self, graph):
        self.graph = graph
        self.relationship_manager = RelationshipManager(graph)
        self.aggregation_manager = AggregationManager(graph)
        self.where_statement = WhereStatement(graph)
        self.node_similarity = NodeSimilarity(graph)

    def parse(self, query):
        queries = [q.strip() for q in query.split(';') if q.strip()]
        results = []
        for q in queries:
            print(f"Parsing query: {q}")  
            if q.startswith("CREATE"):
                results.append(self.parse_create(q))
            elif q.startswith("MATCH"):
                results.append(self.parse_match(q))
            else:
                results.append("Error: Unsupported query type.")
        return results

    def parse_create(self, query):
        node_pattern = r"CREATE\s+\((\w+):(\w+)\s*{\s*(.+?)\s*}\)"
        edge_pattern = r"CREATE\s+\((\w+)\)-\[:(\w+)\s*{\s*(.+?)\s*}\]->\((\w+)\)"
        
        if re.match(node_pattern, query):
            match = re.match(node_pattern, query)
            if match:
                node_id, label, properties_str = match.groups()
                properties = self.parse_properties(properties_str)
                self.graph.add_node(Node(node_id, label, properties))
                print("queryParser --", self.graph, node_id, label, properties_str)
                return f"Node ({node_id}:{label}) created successfully."
            else:
                return "Error: Invalid CREATE query format."
        elif re.match(edge_pattern, query):
            match = re.match(edge_pattern, query)
            if match:
                source, label, properties_str, target = match.groups()
                properties = self.parse_properties(properties_str)
                return self.relationship_manager.create_relationship(source, target, label, properties)
            else:
                return "Error: Invalid CREATE query format."
        else:
            return "Error: Invalid CREATE query format."
    

    def parse_match(self, query):
        match_pattern = r"MATCH\s+\((\w+):(\w+)\s*\)\s*-\[:(\w+)\s*\]\s*->\s*\((\w+):(\w+)\s*\)\s*RETURN\s+(.+)"
        match = re.match(match_pattern, query)
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
            print("edges ---- \n", edges)
            results = {
                source_var: [self.graph.get_node(edge.source) for edge in filtered_edges],
                target_var: [self.graph.get_node(edge.target) for edge in filtered_edges],
                "edges": filtered_edges
            }

            print(f"Parsing MATCH query: {results}")

            if return_clause:
                if results[source_var] or results[target_var] or results["edges"]:
                    return self.parse_return_clause(return_clause, results)
                else:
                    return "No matching nodes or edges found."
            else:
                return results
        else:
            aggregation_pattern = r"MATCH\s+\((\w+):(\w+)\)\s*RETURN\s+(.+)"
            match = re.match(aggregation_pattern, query)
            if match:
                source_var, source_label, return_clause = match.groups()
                source_nodes = self.graph.get_nodes_by_label(source_label)
                
                filtered_results = {"nodes": source_nodes}

                print(f"Parsing MATCH aggregation query: {filtered_results}")

                if return_clause:
                    return self.parse_return_clause(return_clause, filtered_results)
                else:
                    return filtered_results
            else:
                return "Error: Invalid MATCH query format."

    def parse_return_clause(self, return_clause, results):
        return_parts = return_clause.split(",")
        final_results = {}

        for part in return_parts:
            part = part.strip()
            if part == "*":
                final_results.update(results)
            elif part.startswith("COUNT("):
                alias = part[6:-1].strip()
                if alias == 'n':
                    final_results['count'] = self.aggregation_manager.count(results['nodes'])
                else:
                    return f"Error: Invalid RETURN clause. Alias '{alias}' not found in results."
            elif any(part.startswith(f"{func}(") for func in ["SUM", "AVG", "MAX", "MIN"]):
                func, alias_with_parenthesis = part.split("(")
                alias = alias_with_parenthesis[:-1].strip() 
                if '.' in alias:
                    node_alias, property_name = alias.split(".")
                    if node_alias == 'n' and 'nodes' in results:
                        if func == "SUM":
                            final_results[f"SUM({alias})"] = self.aggregation_manager.sum(results['nodes'], property_name)
                        elif func == "AVG":
                            final_results[f"AVG({alias})"] = self.aggregation_manager.avg(results['nodes'], property_name)
                        elif func == "MIN":
                            final_results[f"MIN({alias})"] = self.aggregation_manager.min(results['nodes'], property_name)
                        elif func == "MAX":
                            final_results[f"MAX({alias})"] = self.aggregation_manager.max(results['nodes'], property_name)
                    else:
                        return f"Error: Invalid RETURN clause. Alias '{node_alias}' not found in results."
                else:
                    return f"Error: Invalid RETURN clause. Property '{alias}' not correctly specified."
            else:
                if part in results:
                    final_results[part] = results[part]
                else:
                    return f"Error: Invalid RETURN clause. Alias '{part}' not found in results."

        return final_results

    def parse_properties(self, properties_str):
        if not properties_str:
            return {}
        properties = {}
        pairs = properties_str.split(",")
        for pair in pairs:
            key, value = pair.split(":")
            properties[key.strip()] = value.strip().strip('"')
        return properties
  
    def match_properties(self, node_properties, query_properties):
        print("112 Match - Properties --", node_properties, query_properties)
        if not query_properties:
            return True
        for key, value in query_properties.items():
            if key not in node_properties or node_properties[key] != value:
                return False
        return True
    
    def parse_similarity_query(self, query):
        try:
            _, node_id, method = query.split()
            similarities = self.node_similarity.most_similar_nodes(node_id, method=method)
            return similarities
        except ValueError as ve:
            return f"Error: {str(ve)}"
        except Exception as e:
            return "Error: Invalid similarity query format."

if __name__ == "__main__":
    from knowlegde_graphy import KnowledgeGraph, Node, Edge

    graph = KnowledgeGraph()
    parser = QueryParser(graph)


    create_node_query1 = 'CREATE (n1:Person {name: "Rajesh", age: "30"})'
    create_node_query2 = 'CREATE (n2:Person {name: "Vinod", age: "35"})'
    create_node_query3 = 'CREATE (n3:City {name: "New York"})'
    print(parser.parse(create_node_query1)) 
    print(parser.parse(create_node_query2))  
    print(parser.parse(create_node_query3))  

    create_relationship_query = 'CREATE (n1)-[:knows {since: "2020"}]->(n2)'
    print(parser.parse(create_relationship_query))  
    match_query_1 = 'MATCH (n1:Person)-[:knows]->(n2:Person) RETURN n1, n2'
    print(parser.parse(match_query_1))  

    match_query_2 = 'MATCH (n1:Person {name: "Rajesh"})-[rel:knows]->(n2:Person {name: "Vinod"}) RETURN rel'
    print(parser.parse(match_query_2)) 

    match_query_count = 'MATCH (n:Person) RETURN COUNT(n)'
    print(parser.parse(match_query_count)) 

    match_query_sum = 'MATCH (n:Person) RETURN SUM(n.age)'
    print(parser.parse(match_query_sum)) 

    match_query_avg = 'MATCH (n:Person) RETURN AVG(n.age)'
    print(parser.parse(match_query_avg))  
