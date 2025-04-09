class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_node = None

    def append(self, value):
        new_node = DoublyNode(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            # Si estamos en el medio del historial, elimina todo lo que viene después
            if self.current_node and self.current_node != self.tail:
                self._truncate_after_current()

            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.current_node = new_node

    def _truncate_after_current(self):
        node = self.current_node.next
        while node:
            temp = node
            node = node.next
            del temp
        self.current_node.next = None
        self.tail = self.current_node

    def move_backward(self):
        if self.current_node and self.current_node.prev:
            self.current_node = self.current_node.prev

    def move_forward(self):
        if self.current_node and self.current_node.next:
            self.current_node = self.current_node.next

    def current(self):
        return self.current_node.value if self.current_node else ""
