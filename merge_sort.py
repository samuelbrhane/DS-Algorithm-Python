def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted_lists(left, right, arr)


def merge_sorted_lists(a, b, arr):
    left_pointer = right_pointer = main_pointer = 0

    while left_pointer < len(a) and right_pointer < len(b):
        if a[left_pointer] <= b[right_pointer]:
            arr[main_pointer] = a[left_pointer]
            left_pointer += 1
        else:
            arr[main_pointer] = b[right_pointer]
            right_pointer += 1
        main_pointer += 1

    while left_pointer < len(a):
        arr[main_pointer] = a[left_pointer]
        left_pointer += 1
        main_pointer += 1

    while right_pointer < len(b):
        arr[main_pointer] = b[right_pointer]
        right_pointer += 1
        main_pointer += 1


if __name__ == '__main__':
    a = [4, 7, 9, 10, 11, 15]
    b = [2, 6, 8, 10]

    arr = [12, 54, 75, 23, 72, 86, 1, 25, 47, 84, 92, 17, 68]

    # print(merge_sorted_lists(a, b))
    merge_sort(arr)
    print(arr)
