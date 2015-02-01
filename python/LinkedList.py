import random
import unittest

class Node:
    next = None
    data = None

    def __init__(self, *args, **kwargs):
        data = args[0]
        if type(data) is int:
            self.data = data 
        if type(data) is list:
            self.data = data.pop(0)
            p = self
            while data:
                n = Node(data.pop(0))
                p.next = n
                p = p.next

    def appendToTail(self, data):
        end = Node(data)
        n = self
        while n.next:
            n = n.next
        n.next = end

    @classmethod
    def delete(cls, head, data):

        # done if data is in first node
        if head.data == data:
            return head.next

        # otherwise find the node to delete
        pointer = head
        while head.next.data != data:
            pointer = pointer.next

        # manipulate pointers to skip the node
        skip = pointer.next.next
        pointer.next.next = None
        pointer.next = skip

        # head is unchaged
        return head 

class TestNodeThings(unittest.TestCase):

    def test_create_single(self):
        n = Node(1)
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next, None)

    def test_create_array(self):
        n = Node([1, 2, 3])
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next.data, 2)
        self.assertEqual(n.next.next.data, 3)

    def test_append(self):
        n = Node(1)
        n.appendToTail(2)
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next.data, 2)
        self.assertEqual(n.next.next, None)

    def test_delete(self):
        n = Node(1)
        n.appendToTail(2)
        n = Node.delete(n, 1)
        self.assertEqual(n.data, 2)

if __name__ == "__main__":
    unittest.main()