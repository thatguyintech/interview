test_array = [9, 1, 23, 45, 14, 12, 22, 2, 2, 2, 3, 8, 0, 16]
test1 = [0, 1, 3, 2, 4,	6]


# Quicksort 
def quicksort(a):
	if not a:
		return []
	pivot = a[0]
	smaller = []
	bigger = []
	equals = []
	for num in a:
		if num < pivot:
			smaller.append(num)
		elif num > pivot:
			bigger.append(num)
		else:
			equals.append(num)
	return quicksort(smaller) + equals + quicksort(bigger)


# Mergesort using lists
def mergesort(a):
	if len(a) <= 1:
		return a
	left = []
	right = []
	midpt = len(a) / 2
	for index in range(len(a)):
		if index < midpt:
			left.append(a[index])
		else:
			right.append(a[index])
	return merge(mergesort(left), mergesort(right))

def merge(a, b):
	result = []
	if len(a) == 0:
		return b
	if len(b) == 0:
		return a
	while len(a) and len(b) > 0:
		if a[0]	< b[0]:
			result.append(a.pop(0))
		else:
			result.append(b.pop(0))
	if len(a) > 0:
		result += a
	elif len(b) > 0:
		result += b
	return result
