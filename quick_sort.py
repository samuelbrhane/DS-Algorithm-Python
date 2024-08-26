def quick_sort(elements, start, end):
    if start < end:
        end_index = partition(elements, start, end)
        quick_sort(elements, start, end_index - 1)
        quick_sort(elements, end_index + 1, end)


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap_element(start, end, elements)

    swap_element(pivot_index, end, elements)

    return end


def swap_element(a, b, arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]


if __name__ == '__main__':
    elements = [19, 32, 54, 12, 4, 15, 92, 26, 76, 95, 16]
    quick_sort(elements, 0, len(elements) - 1)
    print(elements)
