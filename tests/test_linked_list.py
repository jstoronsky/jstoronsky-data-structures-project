"""Здесь надо написать тесты с использованием unittest для модуля linked_list."""
import unittest
from src.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    ll = LinkedList()
    ll.insert_beginning({'id': 1})
    ll.insert_at_end({'id': 2})
    ll.insert_at_end({'id': 3})
    ll.insert_beginning({'id': 0})

    def test_head_tail(self):
        self.assertEqual(self.ll.tail.data, {'id': 2})
        self.assertEqual(self.ll.tail.next.data, {'id': 3})
        self.assertEqual(self.ll.tail.next.next, None)
        self.assertEqual(self.ll.head.data, {'id': 0})
        self.assertEqual(self.ll.head.next.data, {'id': 1})
        self.assertEqual(self.ll.head.next.next.data, {'id': 2})

    def test_str(self):
        self.assertEqual(str(self.ll), "{'id': 0} -> {'id': 1} -> {'id': 2} -> {'id': 3} -> None")

    def test_to_list(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mik.roz'})
        ll.insert_at_end({'id': 3, 'username': 'mosh_s'})
        ll.insert_beginning({'id': 0, 'username': 'serebro'})
        lst = ll.to_list()
        self.assertEqual(lst[0]["id"], 0)

    def test_get_data(self):
        ll = LinkedList()
        ll.insert_beginning({'id': 1, 'username': 'lazzy508509'})
        ll.insert_at_end({'id': 2, 'username': 'mosh_s'})
        user_data = ll.get_data_by_id(2)
        self.assertEqual(user_data["username"], "mosh_s")
