class CircularListNode:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None


class CircularDoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_at_end(self, value):
        new_node = CircularListNode(value)
        if self.start_node is None:
            new_node.next_node = new_node
            new_node.prev_node = new_node
            self.start_node = new_node
        else:
            last_node = self.start_node.prev_node
            last_node.next_node = new_node
            new_node.prev_node = last_node
            new_node.next_node = self.start_node
            self.start_node.prev_node = new_node

    def insert_at_beginning(self, value):
        self.insert_at_end(value)
        self.start_node = self.start_node.prev_node

    def remove_by_value(self, value):
        if self.start_node is None:
            print("The list is empty. Cannot remove any node.")
            return

        current_node = self.start_node

        while True:
            if current_node.value == value:
                if current_node.next_node == current_node:  # only one node
                    self.start_node = None
                else:
                    current_node.prev_node.next_node = current_node.next_node
                    current_node.next_node.prev_node = current_node.prev_node
                    if current_node == self.start_node:
                        self.start_node = current_node.next_node
                return

            current_node = current_node.next_node
            if current_node == self.start_node:
                print(f"Value {value} not found in the list.")
                break

    def show_list_forward(self):
        if self.start_node is None:
            return "The list is empty."

        current_node = self.start_node
        values_list = []

        while True:
            values_list.append(str(current_node.value))
            current_node = current_node.next_node
            if current_node == self.start_node:
                break

        return " -> ".join(values_list)

    def backward_display(self):
        if self.start_node is None:
            return "The list is empty."

        last_node = self.start_node.prev_node
        current_node = last_node
        values_list = []

        while True:
            values_list.append(str(current_node.value))
            current_node = current_node.prev_node
            if current_node == last_node:
                break

        return " <- ".join(values_list)


# Example usage (if not being run in unit tests)
if __name__ == "__main__":
    my_circular_list = CircularDoublyLinkedList()

    my_circular_list.insert_at_end("QUICK")
    my_circular_list.insert_at_end("BROWN")
    my_circular_list.insert_at_end("FOX")
    print("List after inserting at the end:")
    print(my_circular_list.show_list_forward())
    print()

    my_circular_list.insert_at_beginning("THE")
    print("List after inserting at the beginning:")
    print(my_circular_list.show_list_forward())
    print()

    print("List displayed backward:")
    print(my_circular_list.backward_display())
    print()

    my_circular_list.remove_by_value("QUICK")
    print("List after removing QUICK:")
    print(my_circular_list.show_list_forward())
    print()

    my_circular_list.remove_by_value("QUICK")  # Not found
    my_circular_list.remove_by_value("SLOW")   # Not found
    print()

    my_circular_list.remove_by_value("BROWN")
    print("List after removing BROWN:")
    print(my_circular_list.show_list_forward())
    print()

    my_circular_list.remove_by_value("THE")
    my_circular_list.remove_by_value("FOX")
    print("List after removing all:")
    print(my_circular_list.show_list_forward())
