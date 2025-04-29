def BinarySearch(arr, item):
    lowBorder = 0
    hightBorder = len(arr) - 1

    while lowBorder <= hightBorder:
        middle = (hightBorder + lowBorder) // 2
        searchValue = arr[middle]
        if (searchValue == item):
            return middle
        elif searchValue > item:
            hightBorder = middle - 1
        else:
            lowBorder = middle + 1
    return None


