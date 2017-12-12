class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def prepend(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

        #How would we go about doing insert at an arbitrary position in the list?

    def insert(self, index, data):
        if self.length() == 0:
            self.prepend(data)
        elif index <= self.length():
            current = self.head
            count = 0
            while count < index:
                current = current.get_next()
                count += 1
            temp = current.next_node
            new_node = Node(data, temp)
            current.next_node = new_node
        else:
            raise ValueError("Fuck You.")


    def append(self, data):
        if self.head:
            current = self.head
            while current:
                previous = current
                current = current.get_next()
            previous.set_next(Node(data))
        else:
            self.head = Node(data)

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if not current:
            raise ValueError("Item not in list")
        return current

    def delete(self, data):
        current = self.head
        found = False
        while current and found == False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if not current:
            raise ValueError("Item not in list")
        if not previous:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())



import unittest

class LinkedTests(unittest.TestCase):
    def tests(self):
        test_list = LinkedList()
        self.assertEqual(0, test_list.length())
        try:
            test_list.delete(2)
        except ValueError as a:
            del_error = a
        self.assertIsNotNone(del_error)

        test_list.append(2)
        self.assertEqual(1, test_list.length())
        test_list.prepend(22)
        self.assertEqual(2, test_list.length())
        self.assertEqual(2, test_list.search(2).data)
        test_list.insert(1, 1)
        self.assertEqual(1, test_list.search(1).data)
        self.assertEqual(3, test_list.length())
        try:
            test_list.insert(4, 5)
        except ValueError as b:
            null_index_insert = b
        self.assertIsNotNone(null_index_insert)
        test_list.delete(2)
        self.assertEqual(2, test_list.length())
        try:
            test_list.search(2)
        except ValueError as c:
            null_item_search = c
        self.assertIsNotNone(null_item_search)
        #test search() and delete() for > 1 copies of an element in the list
        test_list.insert(1, 2)
        test_list.insert(2, 2)
        test_list.insert(3, 2)
        test_list.insert(4, 2)
        self.assertEqual(6, test_list.length())
        test_list.delete(2)
        #Verification that the first instance of an element matching the search criteria is removed, rather than all elements which match the criteria.
        self.assertEqual(5, test_list.length())
        self.assertEqual(2, test_list.search(2).data)
        test_list.delete(2)
        test_list.delete(2)
        test_list.delete(2)
        self.assertEqual(2, test_list.length())
        #Delete an appended element.
        test_list.append(345)
        test_list.delete(345)


if __name__ == 'main':
    unittest.main()