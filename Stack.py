from DSExceptions import Empty
from Node import SNode


class LStack:

    def __init__(self):
        self.__top = None

    def push(self, e):
        temp = SNode(e)
        temp.set_next(self.__top)
        self.__top = temp

    def pop(self):
        if self.is_empty():
            raise Empty("Stack underflow error")
        temp = self.__top
        self.__top = self.__top.get_next()
        return temp.get_data()

    def peek(self):
        if self.is_empty():
            raise Empty("Stack underflow error")
        return self.__top.get_data()

    def is_empty(self):
        return self.__top is None
