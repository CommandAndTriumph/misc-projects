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

    # def test_insert2(self):
    #     size = 10
    #     my_list = ArrayList(size)
    #     print(my_list)
    #     my_list.insert(0, 2)
    #     my_list.insert(1, 2)
    #     # my_list.insert(3, 2)
    #     print(my_list)
    #     my_list.remove(1)
    #     print(my_list)
    #     my_list.remove(0)
    #     print(my_list)
    #     for i in range(55):
    #         my_list.insert(i, i)
    #     print(my_list)
    #     my_list.insert(2, 455)
    #     print(my_list)
    #     self.assertEqual(56, my_list.len())
    #
    # def test_remove(self):
    #     size = 10
    #     my_list = ArrayList(size)
    #     for i in range(10):
    #         my_list.insert(i, i)
    #     print(my_list)
    #     self.assertEqual(10, my_list.len())
    #     my_list.remove(2)
    #     print(my_list)
    #     my_list.remove(2)
    #     print(my_list)
    #     self.assertEqual(8, my_list.len())
    #     for i in range(100):
    #         my_list.remove(0)
    #     print(my_list)
    #     self.assertEqual(0, my_list.len())
    #
    # #I'm not sure how an out of bounds index should be handled, so these tests won't cover that case.
    # def test_extended(self):
    #     size = 10
    #     my_list = ArrayList(size)
    #     for i in range(10):
    #         my_list.insert(i, i)
    #     #push()
    #     my_list.push(10)
    #     self.assertEqual(11, my_list.len())
    #     self.assertEqual(20, my_list.capacity)
    #     #get()
    #     for i in range(11):
    #         self.assertEqual(i, my_list.get(i))
    #     #set()
    #     for i in range(11):
    #         my_list.set(i, i + 1)
    #     for i in range(11):
    #         self.assertEqual(i + 1, my_list.get(i))
    #     #pop()
    #     for i in range(11):
    #         my_list.pop()
    #     for i in range(my_list.capacity):
    #         self.assertEqual(None, my_list.get(i))





    #  def basic_tests(self):
    #     my_list = ArrayList(200)
    #     self.assertEqual(0, my_list.len())
    #     #Insert at i at index i, should populate my_list with 100 elements in range 0:101.
    #     for i in range(0, 101):
    #         my_list.insert(i, i)
    #     self.assertEqual(101, my_list.len())
    #     self.assertEqual(0, my_list.get(0))
    #     self.assertEqual(4, my_list.get(4))
    #     self.assertEqual(100, my_list.get(100))
    #     #Test get() at OoB index:
    #     try:
    #         my_list.get(101)
    #     except ValueError as e:
    #         oob_get = e
    #     self.assertIsNotNone(oob_get)
    #     #Remove at same index.  Target behavior is remove() shifts elements to the 'left'.
    #     for i in range(0, 101):
    #         my_list.remove(0)
    #     self.assertEqual(0, my_list.len())
    #     #Insert at the same address.  Target behavior is shifting what's at the address to the right.
    #     for i in range(0, 101):
    #         my_list.insert(0, 1)
    #     self.assertEqual(100, my_list.len())
    #     #Insert to OoB index.
    #     try:
    #         my_list.insert(1, 1)
    #     except ValueError as a:
    #         oob_insert = a
    #     self.assertIsNotNone(oob_insert)
    #     #Remove OoB index, at 0 and 1, both operations should be invalid.
    #     try:
    #         my_list.remove(0)
    #     except ValueError as a2:
    #         index0_remove = a2
    #     self.assertIsNotNone(index0_remove)
    #     try:
    #         my_list.remove(1)
    #     except ValueError as a3:
    #         index1_remove = a3
    #     self.assertIsNotNone(index1_remove)
    #
    # #For push(), prepend(), set() and pop().
    # def extended_tests(self):
    #     my_list = ArrayList()
    #     self.assertEqual(0, my_list.len())
    #     #Test push(), target behavior is elements are added to the end of the list.
    #     for i in range(0, 50):
    #         my_list.push(0)
    #     self.assertEqual(50, my_list.len())
    #     for i in range(50, 101):
    #         my_list.push(i)
    #     self.assertEqual(101, my_list.len())
    #     self.assertEqual(0, my_list.get(0))
    #     for i in range(50, 101):
    #         self.assertEqual(i, my_list.get(i))
    #     #Test pop(), target behavior is the tail element of a list is removed when the method is called on said list.
    #     for i in range(0, 50):
    #         my_list.pop()
    #     self.assertEqual(0, my_list.get(49))
    #     #Depopulate my_list.
    #     for i in range(0, 50):
    #         my_list.pop()
    #     self.assertEqual(0, my_list.len())
    #     #Test prepend(), target
    #     for i in range(0, 50):
    #         my_list.push(-1)

    #def remove(self, index):
        # try:
        #     self.list[index] = None
        #     self.length -= 1
        # except ValueError:
        #     print("Index out of bounds.")


if __name__ == 'main':
    unittest.main()
