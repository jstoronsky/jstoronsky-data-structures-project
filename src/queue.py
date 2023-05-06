class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node=None):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None
        self.list = []

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next_node = node
            self.tail = node
        self.list.append(self.tail.data)

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if len(self.list) == 0:
            return None
        dequeue_show = self.list[0]
        del self.list[0]
        return dequeue_show

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        self.list_to_str = "\n".join(self.list)
        return self.list_to_str
