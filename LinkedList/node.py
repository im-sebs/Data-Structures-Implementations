class Node:

    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.nextNode = None

    def print_node_in_list(self):
        node_string = f"({self.key}, {self.data})"
        if self.nextNode:
            return node_string + " -> "
        else:
            return node_string

    def print_individual_node(self):
        print(f"({self.key}, {self.data})")

