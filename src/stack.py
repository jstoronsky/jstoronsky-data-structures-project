class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.top = None
        self.list = []
        self.list_out = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        next_node = self.top
        node = Node(data, next_node)
        self.top = node
        self.list.append(self.top.data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if self.top is None:
            return "Nothing to pop, let's rock"
        remove_show = self.top.data
        self.top = self.top.next_node
        self.list_out.append(remove_show)
        return remove_show

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        self.final_list = set(self.list).difference(set(self.list_out))
        self.list_to_str = "\n".join(reversed(list(self.final_list)))
        return self.list_to_str
