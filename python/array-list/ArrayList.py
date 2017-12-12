import unittest

class ArrayList:

    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.list = [None]*capacity

    def insert(self, index, data):
        if index >= self.capacity:
            new_capacity = index + 10 - (index % 10)
            list_temp = new_capacity*[None]
            for i in range(self.capacity):
                list_temp[i] = self.list[i]
            self.list = list_temp
            self.capacity = new_capacity
        temp = self.list[index]
        self.list[index] = data
        if index < self.capacity - 1:
            self.insert(index + 1, temp)
        else:
            self.length += 1

    def remove(self, index):
        if self.length > 0:
            self.length -= 1
        for i in range(index, self.capacity - 1):
            self.list[i] = self.list[i + 1]
        self.list[self.capacity - 1] = None


    def set(self, index, data):
        if self.list[index] == None:
            self.length += 1
        self.list[index] = data


    def push(self, data):
        last_index = self.len()
        self.insert(last_index, data)

    def prepend(self, data):
        self.insert(0, data)

    def len(self):
        i = 0
        count = 0
        while i < self.capacity:
            if self.list[i] != None:
                count += 1
            i += 1
        if self.length > count:
            return self.length
        else:
            return count

    def get(self, index):
        return self.list[index]


    def pop(self):
        last_index = self.len()
        self.remove(last_index - 1)

    def __str__(self):
        return f'{self.list}'

class ArrayTests(unittest.TestCase):
    #For insert(), len(), get(), and remove()

    def test_insert(self):
        size = 10
        my_list = ArrayList(size)
        print(my_list)
        my_list.insert(2, 2)
        my_list.insert(4, 2)
        print(my_list)
        self.assertEqual(10, my_list.capacity)
        self.assertEqual(2, my_list.len())
        self.assertEqual(2, my_list.length)
        my_list.insert(0, 12)
        print(my_list)
        self.assertEqual(3, my_list.length)
        my_list.insert(10, 14)
        print(my_list)
        my_list.insert(16, 12)
        print(my_list)
        self.assertEqual(20, my_list.capacity)
        self.assertEqual(5, my_list.len())
        self.assertEqual(5, my_list.length)

    def test_remove(self):
        size = 10
        my_list = ArrayList(size)
        for i in range(10):
            my_list.insert(i, i)
        print(my_list)
        self.assertEqual(10, my_list.length)
        my_list.remove(2)
        print(my_list)
        my_list.remove(2)
        print(my_list)
        self.assertEqual(8, my_list.len())
        for i in range(100):
            my_list.remove(0)
        print(my_list)
        self.assertEqual(0, my_list.len())

    #I'm not sure how an out of bounds index should be handled, so these tests won't cover that case.
    def test_extended(self):
        size = 10
        my_list = ArrayList(size)
        for i in range(10):
            my_list.insert(i, i)
        #push()
        my_list.push(10)
        self.assertEqual(11, my_list.len())
        self.assertEqual(20, my_list.capacity)
        #get()
        for i in range(11):
            self.assertEqual(i, my_list.get(i))
        #set()
        for i in range(11):
            my_list.set(i, i + 1)
        for i in range(11):
            self.assertEqual(i + 1, my_list.get(i))
        #pop()
        for i in range(11):
            my_list.pop()
        for i in range(my_list.capacity):
            self.assertEqual(None, my_list.get(i))





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
