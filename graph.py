class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.edges_dict = {}

        for start, end in self.edges:
            if start in self.edges_dict:
                self.edges_dict[start].append(end)
            else:
                self.edges_dict[start] = [end]

        print(self.edges_dict)

    def get_path(self, start, end, path = []):
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.edges_dict:
            return []

        all_paths = []
        for destination in self.edges_dict[start]:
            if destination not in path:
                new_paths = self.get_path(destination, end, path)
                for p in new_paths:
                    all_paths.append(p)

        return all_paths


routes = [
    ("London","Paris"),
    ("London","Rome"),
    # ("London","Ljubljana"),
    ("Rome","Paris"),
    ("Rome","Ljubljana"),
    ("Paris","Ljubljana"),
    # ("Ljubljana","Berlin"),
    # ("Berlin","Doha"),
]

route_graph = Graph(routes)
start = "London"
end = "Ljubljana"
print(route_graph.get_path(start, end))
