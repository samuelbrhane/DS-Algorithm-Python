def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1

        while j >= 0 and anchor < elements[j]:
            elements[j + 1] = elements[j]
            j -= 1

        elements[j + 1] = anchor


if __name__ == '__main__':
    elements = [15, 35, 65, 72, 74, 1, 23, 12, 86, 7, 82, 79, 92, 16]
    insertion_sort(elements)
    print(elements)
