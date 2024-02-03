from LinkedList.node import Node


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head

    def insert_to_front(self, key, data):
        node_to_insert = Node(key, data)
        if self.is_empty():
            self.head = node_to_insert
        else:
            previous_head = self.head
            self.head = node_to_insert
            node_to_insert.nextNode = previous_head

    def insert_to_back(self, key, data):
        node_to_insert = Node(key, data)
        if self.is_empty():
            self.head = node_to_insert
        else:
            current_node = self.head
            while current_node.nextNode is not None:
                current_node = current_node.nextNode
            current_node.nextNode = node_to_insert

    def insert_after_node(self, reference_node_key, new_key, new_data):
        current_node = self.head
        inserted = False
        while current_node.nextNode is not None and not inserted:
            if current_node.key == reference_node_key:
                temp_next = current_node.nextNode
                node_to_insert = Node(new_key, new_data)
                current_node.nextNode = node_to_insert
                node_to_insert.nextNode = temp_next
                inserted = True
            current_node = current_node.nextNode
        if not inserted:
            raise Exception(f"There is no {reference_node_key} node in the List. Cannot insert new node.")

    def get_node(self, key):
        current_node = self.head
        while current_node.nextNode is not None:
            if current_node.key == key:
                return current_node
            current_node = current_node.nextNode
        raise Exception(f"There is no node with a key of {key} in the List.")

    def delete_node(self, key):
        if not self.is_empty():
            current_node = self.head
            prev_node = None
            while current_node.nextNode is not None:
                if current_node.key == key:
                    if prev_node:
                        prev_node.nextNode = current_node.nextNode
                        current_node.nextNode = None
                    else:
                        self.head = current_node.nextNode
                        current_node.nextNode = None
                else:
                    prev_node = current_node
                    current_node = current_node.nextNode
            if current_node.key == key:
                if prev_node:
                    prev_node.nextNode = None
                else:
                    self.head = None
            else:
                raise Exception("Element is not in the list.")
        else:
            raise Exception("List is empty. Cannot remove items.")

    def print_list(self):
        if self.is_empty():
            print("Empty")
        else:
            current_node = self.head
            list_string = ""
            while current_node.nextNode is not None:
                list_string = list_string + current_node.print_node_in_list()
                current_node = current_node.nextNode
            list_string = list_string + current_node.print_node_in_list()
            print(list_string)

    def is_empty(self):
        return True if self.head is None else False

    def head(self):
        return self.head

    def size(self):
        size = 0
        if not self.is_empty():
            current_node = self.head
            size = 1
            while current_node.nextNode is not None:
                current_node = current_node.nextNode
                size += 1
        return size

