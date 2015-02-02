import random
import unittest
from util import *

class Node(CommonEqualityMixin):
    next = None
    data = None

    def __init__(self, *args, **kwargs):
        if not args:
            self.data = None
            self.next = None
            return
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

    def __iter__(self):
        return self

    def generator(self):
        p = self
        while p:
            try:
                yield p.data
                p = p.next 
            except StopIteration:
                return


    def appendToTail(self, data):
        if self.data == None:
            self.data = data
        else:
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

# 2.3 Implement an algorithm to delete a node in the middle of a singly linked list
def delete_middle(node):
    next_data = node.next.data
    node.data = next_data
    bloop = node.next
    node.next = node.next.next
    bloop.next = None

# 2.4 Write code to partition a linked list around a value x, such that all nodes
#     that are less than x come before and all nodes greater than or equal come after
def partition(node, x):
    less, more = Node(), Node()
    for data in node.generator():
        if data < x:
            less.appendToTail(data)
        else:
            more.appendToTail(data)
    runner = less
    while runner.next:
        runner = runner.next
    runner.next = more
    return less

def partition_in_place(node, x):
    head, tail = node, node
    # find the tail
    while tail.next:
        tail = tail.next
    p = tail 
    # stop checking at the end
    while head != tail: 
        if head.data >= x:
            p.next = head
            p = p.next
        head = head.next
    # don't forget to seal list 
    p.next = None
    return node 

# 2.5 add numbers stored in linked lists
def add_lists(first, second):
    new_list = Node()
    carry = 0
    while first and second:
        add = first.data + second.data + carry
        carry = 1 if add > 9  else 0
        first, second = first.next, second.next
        add %= 10
        new_list.appendToTail(add)
    while first:
        add = first.data + carry
        carry = 1 if add > 9 else 0
        add %= 10
        new_list.appendToTail(add)
        first = first.next
    while second:
        add = second.data + carry
        carry = 1 if add > 9 else 0
        add %= 10
        new_list.appendToTail(add)
        second = second.next
    if carry:
        new_list.appendToTail(carry)

    return new_list

class TestNodeThings(unittest.TestCase):

    def test_create_single(self):
        n = Node(1)
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next, None)

        m = Node()
        self.assertEqual(m.data, None)
        self.assertEqual(m.next, None)

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

        m = Node()
        m.appendToTail(1)
        self.assertEqual(m.data, 1)
        self.assertEqual(m.next, None)
        m.appendToTail(2)
        self.assertEqual(m.next.data, 2)

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
        self.assertEqual(array.next.print_nodes(), "[2]->[3]->None")

    def test_generator(self):
        n = Node([1, 2, 3, 4, 5])
        data_list = list()
        for node_data in n.generator():
            data_list.append(node_data)
        self.assertEqual("[1, 2, 3, 4, 5]", str(data_list))

class TestInterviewQuestions(unittest.TestCase):

    # 2.1
    def test_remove_dups(self):
        n = Node([1, 2, 2, 3])
        n = remove_dups(n)
        self.assertEqual(n.print_nodes(), Node([1, 2, 3]).print_nodes())

    def test_remove_dups_sorted(self):
        n = Node([1, 2, 2, 3])
        n = remove_dups_sorted(n)
        self.assertEqual(n, Node([1, 2, 3]))

    # 2.2
    def test_kth_to_last(self):
        n = Node([0, 1, 2, 3, 4, 5])
        self.assertEqual(kth_to_last(n, 3), 3)

    # 2.3
    def test_delete_middle(self):
        n = Node([0, 1, 2, 3, 4, 5])
        p = n.next.next
        delete_middle(p)
        self.assertEqual(n, Node([0, 1, 3, 4, 5]))

    # 2.4
    def test_partition(self):
        n = Node([9, 7, 2, 4, 6, 5, 9, 1, 0, 8])
        x = 6
        blarp = partition(n, x)

        r, p = blarp, blarp
        while p.data < x:
            p = p.next
        while r != p:
            self.assertTrue(r.data < x)
            r = r.next
        while p != None:
            self.assertTrue(p.data >= x)
            p = p.next

    def test_partition_in_place(self):
        n = Node([9, 7, 2, 4, 6, 5, 9, 1, 0, 8])
        x = 6
        blarp = partition_in_place(n, x)

        r, p = blarp, blarp
        while p.data < x:
            p = p.next
        while r != p:
            self.assertTrue(r.data < x)
            r = r.next
        while p != None:
            self.assertTrue(p.data >= x)
            p = p.next

    # 2.5
    def test_add_lists(self):
        first = Node(0)
        second = Node(1)
        added = add_lists(first, second)
        self.assertEqual(added.print_nodes(), Node(1).print_nodes())

        first = Node(9)
        second = Node(1)
        added = add_lists(first, second)
        self.assertEqual(added.print_nodes(), Node([0, 1]).print_nodes())


if __name__ == '__main__':
    unittest.main()