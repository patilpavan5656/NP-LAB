class NetworkGraph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_edge(self, from_node, to_node, cost):
        self.nodes.add(from_node)
        self.nodes.add(to_node)
        self.edges[(from_node, to_node)] = cost

def bellman_ford(graph, source):
    distance = {node: float('inf') for node in graph.nodes}
    distance[source] = 0

    for _ in range(len(graph.nodes) - 1):
        for from_node, to_node in graph.edges:
            new_distance = distance[from_node] + graph.edges[(from_node, to_node)]
            if new_distance < distance[to_node]:
                distance[to_node] = new_distance

    return distance

def main():
    network = NetworkGraph()
    network.add_edge("A", "B", 1)
    network.add_edge("B", "C", 1)
    network.add_edge("A", "D", 1)
    network.add_edge("B", "D", 1)
    network.add_edge("C", "D", 1)
    network.add_edge("C", "E", 1)
    network.add_edge("C", "F", 1)
    network.add_edge("D", "E", 1)
    network.add_edge("D", "F", 1)
    network.add_edge("E", "F", 1)

    source_node = "A"
    distances = bellman_ford(network, source_node)

    for node, distance in distances.items():
        print(f"Distance from {source_node} to {node}: {distance}")

if __name__ == "__main__":
    main()