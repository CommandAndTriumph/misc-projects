import unittest

class ArrayList:

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.list = [None]*capacity

    def insert(self, index, data):
        if index > self.len():
            raise Exception("Index out of bounds.")
        if self.length == self.capacity:
            self.make_bigger()
        temp = self.list[index]
        self.list[index] = data
        if index < self.len():
            self.insert(index + 1, temp)

    def make_bigger(self):
        new_capacity = self.capacity + 10
        list_temp = new_capacity * [None]
        for i in range(self.capacity):
            list_temp[i] = self.list[i]
        self.list = list_temp
        self.capacity = new_capacity

    def len(self):
        index = 0
        while index < self.capacity:
            if self.list[index] == None:
                break
            else:
                index += 1
        self.length = index
        return index

    def remove(self, index):
        if index >= self.len():
            raise Exception("Index out of bounds.")
        for i in range(index, self.len()):
            self.list[i] = self.list[i + 1]
        self.list[self.capacity - 1] = None

    def set(self, index, data):
        if index > self.len():
            raise Exception("Index out of bounds.")
        if index == self.len() and self.length == self.capacity:
            self.make_bigger()
        self.list[index] = data

    def push(self, data):
        last_index = self.len()
        self.insert(last_index, data)

    def prepend(self, data):
        self.insert(0, data)

    def get(self, index):
        if index >= self.len():
            raise Exception("Index out of bounds.")
        return self.list[index]

    def pop(self):
        last_index = self.len()
        self.remove(last_index - 1)

    def __str__(self):
        return f'{self.list}'

#TODO: Implement negative indexing for insert(), get(), set(), and remove().

class ArrayTests(unittest.TestCase):
    #insert() and len() are co-dependent, test_insert() therefore also includes the tests for len().
    def test_insert(self):
        my_list = ArrayList(10)
        self.assertEqual(0, my_list.len())
        #len() should set self.length to its return value, so self.len() should always == self.length().
        #If this assertion fails, the method in question is not calling len(), but is instead determining the length of self with self.length, which is a problem.
        #In insert(), to cut back on method calls, self.length is used in several places AFTER self.len().
        self.assertEqual(0, my_list.length)
        #Insert within capacity, but outside length.
        with self.assertRaises(Exception):
            my_list.insert(1, 1)
        for i in range(9):
            my_list.insert(i, i)
        self.assertEqual(10, my_list.capacity)
        self.assertEqual(9, my_list.len())
        self.assertEqual(9, my_list.length)
        #Inserting at an index which is equal to self.capacity - 1, doing this should increase the capacity of the array by 10 and the length by 1.
        my_list.insert(9, 9)
        self.assertEqual(20, my_list.capacity)
        self.assertEqual(10, my_list.len())
        self.assertEqual(10, my_list.length)
        #Inserting outside capacity.
        with self.assertRaises(Exception):
            my_list.insert(20, 20)
            my_list.insert(21, 20)
        #Tests for negative indexing, not yet supported in insert().
        # my_list.insert(-1, 10)
        # self.assertEqual(11, my_list.len())
        # self.assertEqual(11, my_list.length)
        # self.assertEqual(10, my_list.get(10))

    def test_remove(self):
        my_list = ArrayList(10)
        for i in range(10):
            my_list.insert(i, i)
        self.assertEqual(10, my_list.len())
        my_list.remove(0)
        self.assertEqual(9, my_list.len())
        self.assertEqual(9, my_list.length)
        self.assertEqual(1, my_list.get(0))
        self.assertEqual(9, my_list.get(8))
        for i in range(9):
            my_list.remove(0)
        self.assertEqual(0, my_list.len())
        self.assertEqual(0, my_list.length)
        #Test removal at an out of bounds index.
        with self.assertRaises(Exception):
            my_list.remove(0)
            my_list.remove(10)
            my_list.remove(20)

    def test_get(self):
        my_list = ArrayList(10)
        for i in range(10):
            my_list.insert(i, i)
        for i in range(10):
            self.assertEqual(i, my_list.get(i))
        #Test at an index >= self.len()
        with self.assertRaises(Exception):
            my_list.get(10)
            my_list.get(20)
        #Tests for negative indexing, not yet supported.
        # self.assertEqual(9, my_list.get(-1))
        # self.assertEqual(8, my_list.get(-2))
        # with self.assertRaises(Exception):
        #     my_list.get(-10)


    def test_set(self):
        my_list = ArrayList(10)
        for i in range(10):
            my_list.insert(i, i)
        for i in range(10):
            my_list.set(i, i + 1)
        for i in range(10):
            self.assertEqual(i + 1, my_list.get(i))
        self.assertEqual(10, my_list.len())
        self.assertEqual(10, my_list.length)
        #Test at an index = self.len().  This should increase the capacity of self by 10.
        my_list.set(10, 11)
        self.assertEqual(11, my_list.len())
        self.assertEqual(11, my_list.length)
        self.assertEqual(20, my_list.capacity)
        #Test at an index > self.len(), this should raise an Exception.
        with self.assertRaises(Exception):
            my_list.set(12, 13)
        #TODO add tests for negative indexing with set()

    def test_push(self):
        my_list = ArrayList(10)
        for i in range(10):
            my_list.push(i)
        for i in range(10):
            self.assertEqual(i, my_list.get(i))
        self.assertEqual(10, my_list.len())
        self.assertEqual(10, my_list.length)
        self.assertEqual(20, my_list.capacity)

    def test_prepend(self):
        my_list = ArrayList(10)
        for i in range(10):
            my_list.prepend(i)
        for i in range(10, 0):
            self.assertEqual(i, my_list.get(i))
        self.assertEqual(10, my_list.len())
        self.assertEqual(10, my_list.length)
        self.assertEqual(20, my_list.capacity)

    def test_pop(self):
        my_list = ArrayList(10)
        for i in range(10):
            my_list.insert(i, i)
        for i in range(10, 0):
            my_list.pop()
            self.assertEqual(i + 1, my_list.len())
            self.assertEqual(i + 1, my_list.length)
            self.assertEqual(20, my_list.capacity)
            self.assertRaises(i - 1, my_list.get(i))
            with self.assertRaises(Exception):
                my_list.get(i)

if __name__ == 'main':
    unittest.main()
