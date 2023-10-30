from DSExceptions import Empty
from copy import deepcopy


class MinHeap:
    """
            A class that implements the Min Heap data structure by making use of a list

            to create a min heap:
                test_heap = MinHeap([1, 2, 3])

            heapify the Min heap
                test_heap.heapify()

            access the heapified internal list representing the heap
                test_heap.heap

            change the internal list of the heap

                # changing the internal list might break the internal key, set it too
                test_heap.heap = [1.5, 2.2, .3]

            set a new key for the heap

                test_heap.key = lambda x:x//1

            sorting the heap

                new_heap = test_heap.heapsort()

                print(new_heap)

            adding an element to the heap

            new_heap.add(2.5)

            print(new_heap)
        """

    def __init__(self, arr: list, key=lambda x: x):
        """

        :param arr: the initial value of the Min Heap
        :param key: if the elements of the heap are objects, pass a function that accesses the member of each element
            to use for comparison within the heapify_down method
        """
        self.__heap = arr
        self.__key = key

    @property
    def heap(self):
        """
            A getter for the internal list of the heap
        :return: the list representing the heap
        """
        return self.__heap

    @heap.setter
    def heap(self, arr):
        """
            A setter for the internal list of the heap
        :param arr: the array to use
        :return: None; modifies the heap instance
        """

        self.__heap = arr

    @property
    def key(self):
        """
            A getter for the passed key of the heap
        :return: the function or key of the heap that it uses to access the values of the instances within the internal
            list
        """
        return self.__key

    @key.setter
    def key(self, key):
        """
            A setter for the passed key of the heap
        :param key: the new function or key of the heap, to use to access the values of the instances within the
            internal list
        :return: None; modifies the heap instance
        """
        self.__key = key

    def peek(self):
        """
        :return: the first or the root element of the heap
        """
        if self.is_empty():
            raise Empty("Min heap is empty! Set a value by setting the internal array and heapify the instance!")
        return self.__heap[0]

    def is_empty(self):
        """
        :return: if the heap is empty, return false, else return true
        """
        return len(self.__heap) == 0

    def __swap(self, i, j):
        """
            A private method that swaps the elements of internal list of the heap
        :param i: the first index of the element to swap
        :param j: the second index of the element to swap
        :return: None; modifies the internal list of the heap
        """
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __heapify_down(self, n, i):
        """
            A method that maintains the "heap" property
        :param n: the length of the tree or the subtree of the heap to conform the heap property to
        :param i: the index of the heap tree node represented by the internal list to conform the heap property to
        :return: None; modifies the internal list representing the heap
        """
        access = self.__key
        lowest_i = i
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        if left_child < n and access(self.__heap[lowest_i]) > access(self.__heap[left_child]):
            lowest_i = left_child
        if right_child < n and access(self.__heap[lowest_i]) > access(self.__heap[right_child]):
            lowest_i = right_child

        if lowest_i != i:
            self.__swap(lowest_i, i)
            self.__heapify_down(n, lowest_i)

    def __heapify_up(self, i):
        """
            A method that maintains the "heap" property when adding a new element in the heap
        :param i: the index of the heap tree node represented by the internal list to conform the heap property to
        :return: None; modifies the internal list representing the heap
        """

        access = self.__key
        # calculate the parent index in the internal list of the heap
        parent_i = (i - 1) // 2
        # check if the index has a parent, all nodes have parents except the root node
        if parent_i >= 0:
            # check if the parent element has a larger value
            if access(self.__heap[parent_i]) > access(self.__heap[i]):
                # swap the parent and child element
                self.__swap(parent_i, i)
                # recursively call heapify_up until the heap property is fixed
                self.__heapify_up(parent_i)
        else:
            return

    def heapify(self):
        """
            A method that applies the heap property on a heap represented by a list
        :return: None; modifies the internal list of the heap
        """
        if self.is_empty():
            raise Empty("Min heap is empty! Set a value by setting the internal array and heapify the instance!")
        n = len(self.__heap)
        # loop through the leaf node of the tree then heapify each node going upward
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify_down(n, i)

    def heapsort(self):
        """
            A method that sorts the internal list of the heap in ascending order
        :return: a sorted copy of the internal list of the heap
        """
        temp = deepcopy(self)
        temp.heapify()
        n = len(temp.heap)
        for i in range(n - 1, 0, -1):
            temp.__swap(0, i)
            temp.__heapify_down(i, 0)
        return temp

    def delete(self, i):
        """
            A method that removes or pops the element of the heap specified with by an index

            instead of creating a new method that returns the removed element, this method is modified and has
            deviated from the instruction to return the removed element
        :param i: the index of the element in the heap to remove
        :return: the removed element of the heap
        """
        # check if heap is empty
        if self.is_empty():
            raise Empty("Min heap is empty! Set a value by setting the internal array and heapify the instance!")
        # store the length of the internal list
        n = len(self.__heap)
        # swap the index to delete and the last element
        self.__swap(i, n - 1)
        # store the element to be removed
        temp = self.__heap[-1]
        # delete the last element which is the value of the previous element with index i
        del self.__heap[-1]
        # decrement the heap by 1 because of the removal of the last element
        n -= 1
        # heapify the new element in the index i to fix the heap property
        self.__heapify_down(n, i)
        return temp

    def removeMin(self):
        """
             A method that removes the root or the first element of the heap
        :return: the root or top of the heap
        """
        # check if heap is empty
        if self.is_empty():
            raise Empty("Min heap is empty! Set a value by setting the internal array and heapify the instance!")
        return self.delete(0)

    def add(self, element):
        """
            A method that adds new element in the heap
        :param element: the element to add
        :return: None; modifies the internal list of the heap
        """
        # append the element to the end of the internal list
        self.__heap.append(element)
        # get the new length of the heap (or the internal list)
        n = len(self.__heap)
        # heapify or bubble the last element upwards to fix the heap property
        self.__heapify_up(n - 1)

    def __str__(self):
        """
            The string representation of the heap
        :return: the string representation of the internal list
        """
        return str(self.__heap)


class MaxHeap:
    """
        A class that implements the Max Heap data structure by making use of a list

        to create a max heap:
            test_heap = MaxHeap([1, 2, 3])

        heapify the max heap
            test_heap.heapify()

        access the heapified internal list representing the heap
            test_heap.heap

        change the internal list of the heap

            # changing the internal list might break the internal key, set it too
            test_heap.heap = [1.5, 2.2, .3]

        set a new key for the heap

            test_heap.key = lambda x:x//1

        sorting the heap

            new_heap = test_heap.heapsort()

            print(new_heap)

        adding an element to the heap

            new_heap.add(2.5)

            print(new_heap)
    """

    def __init__(self, arr: list, key=lambda x: x):
        """

        :param arr: the initial value of the Max Heap
        :param key: if the elements of the heap are objects, pass a function that accesses the member of each element
            to use for comparison within the heapify_down method
        """
        self.__heap = arr
        self.__key = key

    @property
    def heap(self):
        """
            A getter for the internal list of the heap
        :return: the list representing the heap
        """
        return self.__heap

    @heap.setter
    def heap(self, arr):
        """
            A setter for the internal list of the heap
        :param arr: the array to use
        :return: None; modifies the heap instance
        """

        self.__heap = arr

    @property
    def key(self):
        """
            A getter for the passed key of the heap
        :return: the function or key of the heap that it uses to access the values of the instances within the internal
            list
        """
        return self.__key

    @key.setter
    def key(self, key):
        """
            A setter for the passed key of the heap
        :param key: the new function or key of the heap, to use to access the values of the instances within the
            internal list
        :return: None; modifies the heap instance
        """
        self.__key = key

    def peek(self):
        """
        :return: the first or the root element of the heap
        """
        if self.is_empty():
            raise Empty("Max heap is empty! Set a value by setting the internal array and heapify the instance!")
        return self.__heap[0]

    def is_empty(self):
        """
        :return: if the heap is empty, return false, else return true
        """
        return len(self.__heap) == 0

    def __swap(self, i, j):
        """
            A private method that swaps the elements of internal list of the heap
        :param i: the first index of the element to swap
        :param j: the second index of the element to swap
        :return: None; modifies the internal list of the heap
        """
        self.__heap[i], self.__heap[j] = self.__heap[j], self.__heap[i]

    def __heapify_down(self, n, i):
        """
            A method that maintains the "heap" property
        :param n: the length of the tree or the subtree of the heap to conform the heap property to
        :param i: the index of the heap tree represented by the internal list to conform the heap property to
        :return: None; modifies the internal list representing the heap
        """
        access = self.__key
        largest_i = i
        left_child = i * 2 + 1
        right_child = i * 2 + 2

        if left_child < n and access(self.__heap[largest_i]) < access(self.__heap[left_child]):
            largest_i = left_child
        if right_child < n and access(self.__heap[largest_i]) < access(self.__heap[right_child]):
            largest_i = right_child

        if largest_i != i:
            self.__swap(largest_i, i)
            self.__heapify_down(n, largest_i)

    def __heapify_up(self, i):
        """
            A method that maintains the "heap" property when adding a new element in the heap
        :param i: the index of the heap tree node represented by the internal list to conform the heap property to
        :return: None; modifies the internal list representing the heap
        """

        access = self.__key
        # calculate the parent index in the internal list of the heap
        parent_i = (i - 1) // 2
        # check if the index has a parent, all nodes have parents except the root node
        if parent_i >= 0:
            # check if the parent element has a larger value
            if access(self.__heap[parent_i]) < access(self.__heap[i]):
                # swap the parent and child element
                self.__swap(parent_i, i)
                # recursively call heapify_up until the heap property is fixed
                self.__heapify_up(parent_i)
        else:
            return

    def heapify(self):
        """
            A method that applies the heap property on a heap represented by a list
        :return: None; modifies the internal list of the heap
        """
        if self.is_empty():
            raise Empty("Max heap is empty! Set a value by setting the internal array and heapify the instance!")
        n = len(self.__heap)
        # loop through the leaf node of the tree then heapify each node going upward
        for i in range(n // 2 - 1, -1, -1):
            self.__heapify_down(n, i)

    def heapsort(self):
        """
            A method that sorts the internal list of the heap in ascending order
        :return: a sorted copy of the internal list of the heap
        """
        temp = deepcopy(self)
        temp.heapify()
        n = len(temp.heap)
        for i in range(n - 1, 0, -1):
            temp.__swap(0, i)
            temp.__heapify_down(i, 0)
        return temp

    def delete(self, i):
        """
            A method that removes or pops the element of the heap specified with by an index

            instead of creating a new method that returns the removed element, this method is modified and has
            deviated from the instruction to return the removed element
        :param i: the index of the element in the heap to remove
        :return: the removed element of the heap
        """
        # check if heap is empty
        if self.is_empty():
            raise Empty("Max heap is empty! Set a value by setting the internal array and heapify the instance!")
        # store the length of the internal list
        n = len(self.__heap)
        # swap the index to delete and the last element
        self.__swap(i, n - 1)
        # store the element to be removed
        temp = self.__heap[-1]
        # delete the last element which is the value of the previous element with index i
        del self.__heap[-1]
        # decrement the heap by 1 because of the removal of the last element
        n -= 1
        # heapify the new element in the index i to fix the heap property
        self.__heapify_down(n, i)
        return temp

    def removeMax(self):
        """
             A method that removes the root or the first element of the heap
        :return: the top of the list
        """
        # check if heap is empty
        if self.is_empty():
            raise Empty("Max heap is empty! Set a value by setting the internal array and heapify the instance!")
        return self.delete(0)

    def add(self, element):
        """
            A method that adds new element in the heap
        :param element: the element to add
        :return: None; modifies the internal list of the heap
        """
        # append the element to the end of the internal list
        self.__heap.append(element)
        # get the new length of the heap (or the internal list)
        n = len(self.__heap)
        # heapify or bubble the last element upwards to fix the heap property
        self.__heapify_up(n - 1)

    def __str__(self):
        """
            The string representation of the heap
        :return: the string representation of the internal list
        """
        return str(self.__heap)
