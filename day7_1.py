import pprint

class Node:
    def __init__(self, value):
        self.value = value
        self.dependencies = []
        self.children = []

    def __eq__(self, other):
        self.value == other.value

    def __str__(self):
        return '<v:%s c:%s d:%s>' % (self.value, self.children, self.dependencies)

    def __repr__(self):
        return '<v:%s c:%s d:%s>' % (self.value, self.children, self.dependencies)        

    def add_dependency(self, dependency):
        self.dependencies.append(dependency)
        self.dependencies = list(set(self.dependencies))
        self.dependencies.sort()
    
    def remove_dependency(self, dependency):
        try:
            self.dependencies.remove(dependency)
        except ValueError:
            pass
    
    def satisfy_dependencies(self, satisfied_dependencies):
        for dependency in satisfied_dependencies:
            self.remove_dependency(dependency)

    def add_child(self, child):
        self.children.append(child)
        self.children = list(set(self.children))
        self.children.sort()

    def remove_child(self, child):
        try:
            self.children.remove(child)
        except ValueError:
            pass


# Create the dependency graph
graph = {}
with open('day7.txt') as dependencies_file:
    for line in dependencies_file:
        split_line = line.split()
        node_1, node_2 = split_line[1], split_line[7]
        if node_1 not in graph:
            graph[node_1] = Node(node_1)
        if node_2 not in graph:
            graph[node_2] = Node(node_2)
        graph[node_1].add_child(node_2)
        graph[node_2].add_dependency(node_1)

# Determine the starting point
keys = set(graph.keys())
values = set()
for key in graph:
    for value in graph[key].children:
        values.add(value)
start = list(keys - values)

# Walk the graph
answer = ''
candidates = start
satisfied_dependencies = []

while len(candidates) > 0:
    # Get the current node to add
    current = None
    for candidate in candidates:
        # Remove all currently satisfied dependencies
        graph[candidate].satisfy_dependencies(satisfied_dependencies)
        # Check if it's clear to go
        if len(graph[candidate].dependencies) == 0:
            current = candidate
            break
    # Remove current from candidates
    candidates.remove(current)
    # Add the current node to the answer
    answer += current
    # Add current to satisfied dependencies
    satisfied_dependencies.append(current)
    # Generate new candidates
    new_candidates = list(set(graph[current].children + candidates))
    new_candidates.sort()
    candidates = new_candidates
print(answer)