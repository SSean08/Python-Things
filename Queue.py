from Node import SNode
from Node import DNode
from DSExceptions import Empty


class LQueue:

    def __init__(self):
        self.__first = None
        self.__back = None

    def enqueue(self, e):
        if self.is_empty():
            temp = SNode(e)
            self.__first = temp
            self.__back = temp
            return
        temp = SNode(e)
        self.__back.set_next(temp)
        self.__back = temp

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        temp = self.__first
        self.__first = self.__first.get_next()
        return temp.get_data()

    def peek(self):
        if self.is_empty():
            raise Empty("Queue is empty!")
        return self.__first.get_data()

    def is_empty(self):
        return self.__first is None


# Bugged
class LDequeue:

    def __init__(self):
        self.__first = None
        self.__back = None

    def add_first(self, e):
        if self.is_empty():
            temp = DNode(e)
            self.__first = temp
            self.__back = temp
        temp = DNode(e)
        temp.set_next(self.__first)
        self.__first = temp

    def add_last(self, e):
        if self.is_empty():
            temp = DNode(e)
            self.__first = temp
            self.__back = temp
        temp = DNode(e)
        temp.set_prev = self.__back
        self.__back.set_next(temp)
        self.__back = temp

    def delete_first(self):
        if self.is_empty():
            raise Empty("Dequeue is empty!")
        temp = self.__first
        self.__first = self.__first.get_next()
        return temp.get_data()

    def delete_last(self):
        if self.is_empty():
            raise Empty("Dequeue is empty!")
        temp = self.__back
        self.__back = self.__back.get_prev()
        return temp.get_data()

    def peek_first(self):
        if self.is_empty():
            raise Empty("Dequeue is empty!")
        return self.__first.get_data()

    def peek_last(self):
        if self.is_empty():
            raise Empty("Dequeue is empty!")
        return self.__back.get_data()

    def is_empty(self):
        # redundant, checking the first element is enough
        # print(self.__first, self.__back)
        return self.__first is None or self.__back is None
