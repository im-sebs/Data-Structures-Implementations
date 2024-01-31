from LinkedList.linked_list import *

arr = ["1", "2", "3", "4", "5", "6"]

linked_list = LinkedList()

for number in arr:
    linked_list.insert_to_front(Node(number))

linked_list.print_list()