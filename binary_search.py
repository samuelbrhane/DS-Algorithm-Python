def linear_search(nums_list, num):
    for index, val in enumerate(nums_list):
        if val == num:
            return index

    return -1


def binary_search(nums_list, num):
    start = 0
    end = len(nums_list) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums_list[mid] == num:
            return mid

        elif num > nums_list[mid]:
            start = mid + 1

        else:
            end = mid - 1

    return -1


if __name__ == '__main__':
    numbers_list = [12, 15, 19, 21, 22, 27, 34, 37, 40, 45, 51, 54, 56, 63]
    num_to_find = 40
    linear_idx = linear_search(numbers_list, num_to_find)
    print(linear_idx)
    binary_index = binary_search(numbers_list, num_to_find)
    print(binary_index)

