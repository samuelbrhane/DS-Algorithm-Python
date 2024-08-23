def bubble_sort(elements):
    for i in range(len(elements) - 1):
        is_swapped = False
        for j in range(len(elements) - 1 - i):
            if elements[j] > elements[j + 1]:
                temp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = temp
                is_swapped = True

        if not is_swapped:
            break


if __name__ == '__main__':
    numbers_list = [12, 53, 64, 11, 8, 23, 7, 24, 72, 84, 26]
    bubble_sort(numbers_list)
    print(numbers_list)
