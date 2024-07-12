"""
Author: Prashant Verma
email: prashant27050@gmail.com
"""
class WhereStatement:
    def __init__(self, graph):
        self.graph = graph

    def parse_conditions(self, conditions_str):
        conditions = []
        for condition in conditions_str.split("AND"):
            condition = condition.strip()
            if "=" in condition:
                key, value = condition.split("=")
                conditions.append((key.strip(), value.strip().strip('"')))
        return conditions

    def apply_conditions(self, results, conditions_str):
        conditions = self.parse_conditions(conditions_str)
        filtered_results = {}
        for key in results:
            if key == "edges":
                filtered_items = self.filter_items(results[key], conditions)
                filtered_results[key] = filtered_items
            else:
                filtered_items = self.filter_items(results[key], conditions)
                filtered_results[key] = filtered_items
        return filtered_results

    def filter_items(self, items, conditions):
        filtered_items = []
        for item in items:
            match = True
            for key, value in conditions:
                if key in item.properties and item.properties[key] == value:
                    continue
                else:
                    match = False
                    break
            if match:
                filtered_items.append(item)
        return filtered_items

