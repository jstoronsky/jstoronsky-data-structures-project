class Node:
    """Класс для узла односвязного списка"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.initial_list = []

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        node_object = Node(data)
        node_object.next = self.head
        self.head = node_object
        self.initial_list.append(self.head.data)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""
        node_object = Node(data)
        self.tail = self.head
        while self.tail.next is not None:
            self.tail = self.tail.next
        self.tail.next = node_object
        self.initial_list.append(self.tail.next.data)

    def to_list(self):
        """
        сортировка списка и перехват ошибки если в изначальном списке есть не dict
        """
        sorted_list = sorted(self.initial_list, key=lambda key: key["id"])
        return sorted_list

    def get_data_by_id(self, index):
        """
        получение словаря по заданному id
        """
        for sample in self.initial_list:
            try:
                index in sample.values()
            except AttributeError:
                return "Данные не являются словарем или в словаре нет id"
            else:
                if index in sample.values():
                    return sample

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next

        ll_string += 'None'
        return ll_string
