import unittest

# 1.1 - O(n)
def all_unique(string):
    return len(set(string)) == len(string)

# 1.2 O(n)
def reverse_string(string):
    return string[::-1]

    # rev = ""
    # length = len(string)
    # for i in range(length)[::-1]:
    #     rev += string[i]
    # return rev

# 1.3 - should be O(n), two passes through both strings
def is_permutation(first, second):
    return len(first) == len(second) and set(first) == set(second)

# 1.4 - should be O(n), two passes through the string
def replace_spaces(string, length):
    return string.replace(" ", "%20") 

# 1.6 - should be O(n^2), minimum you touch every element in the matrix
def rotate_matrix(matrix, N):
    for layer in range(N/2):
        # indices for rows
        first = layer
        last = N - first - 1
        for i in range(first, last):
            offset = i - first # for iterating backwards in a list
            temp = matrix[first][i]
            matrix[first][i] = matrix[i][last]
            matrix[i][last] = matrix[last][offset]
            matrix[last][offset] = matrix[offset][first]
            matrix[offset][first] = temp
        return matrix


class Test_Stuff(unittest.TestCase):
    # 1.1
    def test_all_unique(self):
        self.assertEquals(all_unique("hello"), False)
        self.assertEquals(all_unique("ll"), False)
        self.assertEquals(all_unique(""), True)
        self.assertEquals(all_unique("obligatory"), False)
        self.assertEquals(all_unique("sharp"), True)

    # 1.2
    def test_reverse_string(self):
        self.assertEquals(reverse_string(""), "")
        self.assertEquals(reverse_string("a"), "a")
        self.assertEquals(reverse_string("ab"), "ba")
        self.assertEquals(reverse_string("abc"), "cba")

    def test_permutations(self):
        self.assertTrue(is_permutation("hello", "holle"))
        self.assertTrue(is_permutation("", ""))
        self.assertFalse(is_permutation("hello", "hole"))
        self.assertFalse(is_permutation("aaaa", "aaa"))

    # 1.4
    def test_replace_spaces(self):
        string = "Hi my name is Albert   "
        replaced = 'Hi%20my%20name%20is%20Albert%20%20%20'
        self.assertEquals(replace_spaces(string, len(string)), replaced)

    # 1.6
    def test_rotate_matrix(self):
        matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        rotated = [[0, 5, 6], [1, 4, 7], [2, 3, 8]]
        self.assertEquals(rotate_matrix(matrix, 3), rotated)


if __name__ == "__main__":
    unittest.main()