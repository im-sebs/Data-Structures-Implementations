from LinkedList.linked_list import *

arr = ["1", "2", "3", "4", "5", "6"]
# arr = ["1"]
# arr = []

linked_list = LinkedList()

for number in arr:
    linked_list.insert_to_back(number, number)

# linked_list.insert_after_node("5", "64", "64")

# linked_list.delete_node("37")

print(linked_list.size())

linked_list.print_list()