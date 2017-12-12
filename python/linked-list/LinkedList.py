class LinkedList:
    def __init__(self, head):
        self.head = head

    def append(self, item):
        if not self.head:
            self.head = Node(item, None)
        else:
            has_next = self.head.pointer
            while has_next:
                has_next = self.head.pointer

    def len(self):
        jmp_count = 1
        maybe_node = self.head.pointer
        while maybe_node:
            maybe_node = self.head.pointer
            jmp_count += 1
        return jmp_count

class Node:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer

list1 = LinkedList(0)
list1.append(22)
list1.append(44)
v = list1.len()
print(v)