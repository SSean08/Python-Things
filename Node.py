class SNode:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    def set_next(self, e):
        self.__next = e

    def get_next(self):
        return self.__next

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return f"SNode({self.__data}, {self.__next}"


class DNode:

    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, e):
        self.__next = e

    def get_next(self):
        return self.__next

    def set_prev(self, e):
        self.__prev = e

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return f"DNode({self.__data}, {self.__next}"


class TreeNode:
    """
        Setter methods must be TreeNode instances!
    """

    def __init__(self, data):
        self.__left = None
        self.__right = None
        self.__parent = None
        self.__data = data

    def get_parent(self):
        return self.__parent

    def set_parent(self, e):
        self.__parent = e

    def get_left(self):
        return self.__left

    def set_left(self, e):
        self.__left = e

    def get_right(self):
        return self.__right

    def set_right(self, e):
        self.__right = e

    def get_data(self):
        return self.__data

    def __str__(self):
        return str(self.__data)

    def __repr__(self):
        return f"TreeNode({self.__data, self.__left, self.__right}"
