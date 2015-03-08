import unittest 

# using only one extra stack (and a tmp var)
def stacksort(s):
    if len(s) <= 1:
        return s
    b = []
    while s:
        tmp = s.pop()
        while b and b[-1] > tmp:
            s.append(b.pop())
        b.append(tmp)
    return b

# using unlimited stacks
def stackQuicksort(s):
    if len(s) <= 1:
        return s
    pivot = s[0]
    less, equals, more = [], [], []
    while s:
        if s[-1] == pivot:
            equals.append(s.pop())
        else:
            less.append(s.pop()) if s[-1] < pivot else more.append(s.pop())
    return stackQuicksort(less) + equals + stackQuicksort(more)

class StackTests(unittest.TestCase):
    def setUp(self):
        self.s = [1, 2, 3]
        self.u = [1, 3, 2]
        self.b = [3, 2, 1]
        self.a = [0]
        self.bl = []
        self.c = [5, 2, 15, 2, -1]

    def test_stacksort(self):
        self.assertEqual(stacksort(self.s), [1, 2, 3])
        self.assertEqual(stacksort(self.u), [1, 2, 3])
        self.assertEqual(stacksort(self.b), [1, 2, 3])
        self.assertEqual(stacksort(self.a), [0])
        self.assertEqual(stacksort(self.bl), [])
        self.assertEqual(stacksort(self.c), [-1, 2, 2, 5, 15])
    
    def test_stackQuicksort(self):
        self.assertEqual(stackQuicksort(self.s), [1, 2, 3])
        self.assertEqual(stackQuicksort(self.u), [1, 2, 3])
        self.assertEqual(stackQuicksort(self.b), [1, 2, 3])
        self.assertEqual(stackQuicksort(self.a), [0])
        self.assertEqual(stackQuicksort(self.bl), [])
        self.assertEqual(stackQuicksort(self.c), [-1, 2, 2, 5, 15])

if __name__ == '__main__':
   unittest.main()
