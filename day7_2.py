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

class Worker:
    def __init__(self):
        self.task = None
        self.busy = False
        self.time_left = 0

    @staticmethod
    def calc_task_time(task):
        return ord(task) - 64
    
    def give_task(self, task):
        self.task = task
        self.busy = True
        self.time_left = 60 + Worker.calc_task_time(task)

    def work(self):
        if not self.busy:
            return None
        self.time_left -= 1
        if self.time_left == 0:
            self.busy = False            
            return self.task
        return None
    
# Walk the graph
answer = ''
candidates = start
satisfied_dependencies = []
worker_pool = [Worker(), Worker(), Worker(), Worker(), Worker()]
seconds = 0
while True:
    # Check endstate
    if len(candidates) == 0:
        any_busy_workers = False
        for worker in worker_pool:
            if worker.busy:
                any_busy_workers = True
                break
        if not any_busy_workers:
            break
    # Assign workers tasks if they aren't busy
    for worker in worker_pool:
        if not worker.busy:
            for candidate in candidates:
                graph[candidate].satisfy_dependencies(satisfied_dependencies)
                if len(graph[candidate].dependencies) == 0:
                    worker.give_task(candidate)
                    candidates.remove(candidate)
                    break
    # Work one second
    outputs = []
    for worker in worker_pool:
        output = worker.work()
        if output is not None:
            outputs.append(output)
            satisfied_dependencies.append(output)
    seconds += 1
    # Update the answer
    # outputs.sort()
    for output in outputs:
        answer += output
    # Generate new candidates
    new_candidates = []
    for output in outputs:
        new_candidates = new_candidates + graph[output].children
    new_candidates = list(set(new_candidates + candidates))
    new_candidates.sort()
    candidates = new_candidates

print(seconds)