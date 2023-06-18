class YBNNetwork():
    def __init__(self):
        self.node_count = 0
        self.edge_count = 0
        self.connections = []
        self.corrupted_nodes_count = 0
        self.corrupted_nodes = []
        self.remove = 0
        self.removed_nodes = {}

    def test_init(self):
        for node in self.connections:
            print(f"Key: {node[0]}, Value: {node[1]}")

    def secure_network(self):
        for node in self.connections:
            key, value = node[0], node[1]
            print(f"Key: {key}, Value: {value}")
            if key in self.corrupted_nodes or value in self.corrupted_nodes:
                self.remove += 1
                self.removed_nodes[self.remove] = [key, value]
            else:
                pass
        return self.remove, self.removed_nodes
    
new_network = YBNNetwork()
new_network.node_count, new_network.edge_count = 6, 7
new_network.connections = [
    [1, 2],
    [1, 3],
    [2, 3],
    [2, 4],
    [3, 5],
    [4, 5],
    [5, 6],
    [4, 6]
]
new_network.corrupted_nodes_count = 2
new_network.corrupted_nodes = [2, 4]
response = new_network.secure_network()
print(f"Number of removed nodes: {response[0]}")
print(f"Removed edges: {response[1]}")