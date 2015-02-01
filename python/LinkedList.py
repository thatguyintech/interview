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

    def __str__(self):
        return str(self.data)

    def appendToTail(self, data):
        end = Node(data)
        n = self
        while n.next:
            n = n.next
        n.next = end

    @classmethod
    def delete(cls, head, data=None):

        n = head

        if n.data == data or not data:
            return head.next

        while n.next:
            if n.next.data == data:
                n.next = n.next.next
                return head
            n = n.next
        return head


    def print_nodes(self):
        bloop = list()
        n = self
        while n != None:
            bloop.append("[" + str(n.data) + "]->")
            n = n.next
        bloop.append("None")
        return str(''.join(bloop))

# CTCI Chapter 2 coding questions

# 2.1 Write code to remove duplicates from an unsorted linked list
def remove_dups(node):
    seen = {} 
    result = list()
    while node:
        if node.data not in seen.keys():
            seen[node.data] = True
            result.append(node.data)
        node = node.next
    return Node(result)

def remove_dups_sorted(node):
    last = None
    result = list()
    while node:
        if node.data != last:
            last = node.data
            result.append(node.data)
        node = node.next
    return Node(result)



# 2.2 Implement an agorithm to find the kth to last element of a singly linked list
def kth_to_last(node, k):
    # use a runner
    n, p = node, node
    while k:
        p = p.next
        k -= 1
    while p.next:
        p = p.next
        n = n.next
    return n.next.data


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
        one = Node(1)
        one = Node.delete(one, 1)
        self.assertEqual(one, None)

        two = Node([1, 2])
        two = Node.delete(two, 2)
        self.assertEqual(two.data, 1)
        self.assertEqual(two.next, None)

        three = Node([1, 2, 3])
        three = Node.delete(three, 2)
        self.assertEqual(three.next.data, 3)

    def test_print_nodes(self):
        single = Node(1)
        self.assertEqual(single.print_nodes(), "[1]->None")

        array = Node([1, 2, 3])
        self.assertEqual(array.print_nodes(), "[1]->[2]->[3]->None")

class TestInterviewQuestions(unittest.TestCase):

    def test_remove_dups(self):
        n = Node([1, 2, 2, 3])
        n = remove_dups(n)
        self.assertEqual(n.print_nodes(), Node([1, 2, 3]).print_nodes())

    def test_remove_dups_sorted(self):
        n = Node([1, 2, 2, 3])
        n = remove_dups_sorted(n)
        self.assertEqual(n.print_nodes(), Node([1, 2, 3]).print_nodes())

    def test_kth_to_last(self):
        n = Node([0, 1, 2, 3, 4, 5])
        self.assertEqual(kth_to_last(n, 3), 3)

    def test_kth_to_last_recursive(self):
        n = Node([0, 1, 2, 3, 4, 5])

if __name__ == '__main__':
    unittest.main()