import sys
import numpy as np
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):

        graph = {}
        for node in nodes:
            graph[node] = {}
        
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    graph[node][adjacent_node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())
    shortest_path = {}
    previous_nodes = {}
    max_value = sys.maxsize
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    shortest_path[start_node] = 0
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes:
            if current_min_node == None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node
                
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                previous_nodes[neighbor] = current_min_node
        unvisited_nodes.remove(current_min_node)
    
    return previous_nodes, shortest_path

def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    path.append(start_node)
    print("We found the following best path with a value of {}.".format(shortest_path[target_node]))
    print(" -> ".join(reversed(path)))

inp = input().split
params = list(map(int, inp))
print(params)

nodes = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8"]
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}
    

init_graph["s1"]["s3"] = np.random.randint(1,11)
init_graph["s1"]["s8"] = np.random.randint(1,11)
init_graph["s2"]["s4"] = np.random.randint(1,11)
init_graph["s2"]["s5"] = np.random.randint(1,11)
init_graph["s2"]["s7"] = np.random.randint(1,11)
init_graph["s3"]["s4"] = np.random.randint(1,11)
init_graph["s3"]["s6"] = np.random.randint(1,11)
init_graph["s3"]["s8"] = np.random.randint(1,11)
init_graph["s4"]["s5"] = np.random.randint(1,11)
init_graph["s4"]["s6"] = np.random.randint(1,11)
init_graph["s5"]["s6"] = np.random.randint(1,11)
init_graph["s5"]["s7"] = np.random.randint(1,11)
init_graph["s6"]["s8"] = np.random.randint(1,11)
init_graph["s7"]["s8"] = np.random.randint(1,11)

	
graph = Graph(nodes, init_graph)
#print(graph.graph)
inp = input("Type start and target switches:").split()
start,target = int(inp[0]),int(inp[1])
previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node="s"+str(start))

print_result(previous_nodes, shortest_path, start_node="s"+str(start), target_node="s"+str(target))

