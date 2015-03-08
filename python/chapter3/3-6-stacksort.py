def stacksort(s):
    b = []
    while s:
        tmp = s.pop()
        while b and b[-1] > tmp:
            s.append(b.pop())
        b.append(tmp)
    return b

x = [1, 2, 3]
y = [1, 3, 2]
z = [3, 2, 1]
