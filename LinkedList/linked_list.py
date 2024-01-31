from LinkedList.node import Node

class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head

    def insert_to_front(self, node_to_insert: Node):
        if self.is_empty():
            self.head = node_to_insert
        else:
            previous_head = self.head
            self.head = node_to_insert
            node_to_insert.nextNode = previous_head

    def insert_in_back(self, node_to_insert: Node):
        current_node = self.head
        while current_node.nextNode is not None:
            current_node = current_node.nextNode()
        current_node.nextNode = node_to_insert

    def print_list(self):
        current_node = self.head
        list_string = ""
        while current_node.nextNode is not None:
            list_string = list_string + f"({current_node.data}) -> "
            current_node = current_node.nextNode
        list_string = list_string + f"({current_node.data})"
        print(list_string)

    def is_empty(self):
        return True if self.head is None else False

