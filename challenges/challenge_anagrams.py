def merge(left: str, right: str) -> str:
    data = []
    i = i2 = 0

    while i < len(left) and i2 < len(right):
        if left[i] < right[i2]:
            data.append(left[i])
            i += 1
        else:
            data.append(right[i2])
            i2 += 1

    data.extend(left[i:])
    data.extend(right[i2:])

    return ''.join(data)


def merge_sort(string: str) -> str:
    if len(string) <= 1:
        return string

    middle = len(string) // 2
    left = merge_sort(string[:middle])
    right = merge_sort(string[middle:])

    return merge(left, right)


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return (merge_sort(first_string), merge_sort(second_string), False)

    new_first_string = merge_sort(first_string.lower())
    new_second_string = merge_sort(second_string.lower())

    is_anagram = new_first_string == new_second_string

    return (new_first_string, new_second_string, is_anagram)
