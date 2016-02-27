'''Sum n numbers and find digits from a to b of that sum'''


def add(arr, a, b):
    """

    :param arr: Array of numbers
    :param a: Index to start
    :param b: Index to end
    :return: Digits in the sum of numbers.
    """
    add = 0
    for i in range(0, len(arr)):  # range because i is the index. If only 'for in arr' is used, it means i is the
        # value and not the index. And we need index to sum the numbers in the array.
        add += arr[i]
    return str(add)[a:b]


def test_euler_13():
    assert add([1, 3, 45, 10, 220, 1000, 150], 0, 3) == '142'
    assert add([1, 3, 45, 10, -220, 1000, -150], 0, 3) == '689'
    assert add([1, 3.9, 45, 10, -220, -1000, -150], 0, 3) == '-13'
