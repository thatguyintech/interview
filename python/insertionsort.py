inp = [2, 7, 4, 6, 8]
b = [-1, 3, 5, 10, 0, 0, 1, 0]

def insertionSort(ar):
    for i in range(1, len(ar)):
        j = i
        while j > 0 and ar[j-1] >= ar[j]:
            temp = ar[j-1]
            ar[j-1] = ar[j]
            ar[j]= temp
            j -= 1
    return ar
