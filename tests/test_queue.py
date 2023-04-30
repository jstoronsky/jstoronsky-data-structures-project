"""Здесь надо написать тесты с использованием unittest для модуля queue."""
import unittest
from src.queue import Queue


class TestQueue(unittest.TestCase):
    queue = Queue()
    queue1 = Queue()
    queue1.enqueue('data1')
    queue1.enqueue('data2')
    queue1.enqueue('data3')

    def test_enqueue(self):
        self.assertEqual(str(Queue()), "")
        self.assertEqual(str(self.queue1), "data1\ndata2\ndata3")
        self.assertEqual(self.queue1.head.data, "data1")
        self.assertEqual(self.queue1.head.next_node.data, "data2")
        self.assertEqual(self.queue1.tail.data, "data3")
        self.assertEqual(self.queue1.tail.next_node, None)
