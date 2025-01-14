"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest
from src.stack import Node, Stack


class TestNode(unittest.TestCase):
    n1 = Node(5, None)
    n2 = Node('a', n1)

    def test_node_init(self):
        self.assertEqual(self.n1.data, 5)
        self.assertEqual(self.n2.data, 'a')


class TestStack(unittest.TestCase):
    stack = Stack()
    stack.push('data1')
    stack.push('data2')
    stack.push('data3')

    def test_push(self):
        self.assertEqual(self.stack.top.data, 'data3')
        self.assertEqual(self.stack.top.next_node.data, 'data2')
        self.assertEqual(self.stack.top.next_node.next_node.data, 'data1')
        self.assertEqual(self.stack.top.next_node.next_node.next_node, None)

    stack_ = Stack()
    stack_.push('data1')
    data = stack_.pop()
    stack1 = Stack()
    stack1.push('data1')
    stack1.push('data2')
    data1 = stack1.pop()

    def test_pop(self):
        self.assertEqual(self.stack_.top, None)
        self.assertEqual(self.data, 'data1')
        self.assertEqual(self.stack1.top.data, 'data1')
        self.assertEqual(self.data1, 'data2')
        self.assertEqual(str(self.stack1), "data1")
