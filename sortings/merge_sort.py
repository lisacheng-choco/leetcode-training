data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if (left[0] < right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    return result + left + right

def merge_sort(input):
    """
    params
        input: List
    """
    # split the input list in half until the length of sub-list is equal to 1
    if (len(input) == 1):
        ## base case
        return input

    mid = len(input) // 2
    left = merge_sort(input[:mid])
    right = merge_sort(input[mid:])

    # merge and sort 2 sorted sub-lists
    return merge(left, right)

print(merge_sort(data))