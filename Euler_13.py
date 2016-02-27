'''Sum n numbers and find digits from a to b of that sum'''


def add(arr, a, b):
    add = 0
    for i in range(0, len(arr)):  # range because i is the index. If only 'for in arr' is used, it means i is the
        # value and not the index. And we need index to sum the numbers in the array.
        add += arr[i]
    print(str(add)[a:b])


print(add([1, 3, 45, 10, 220, 1000, 150], 1, 3))
