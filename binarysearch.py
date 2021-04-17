def binarysearch(arr: list[int], low: int, high: int, item: int) -> int:
    if high >= low:
        mid = int((high - low) / 2) + low
        if item == arr[mid]:
            return mid
        elif item < mid:
            return binarysearch(arr, low, mid - 1, item)
        else:
            return binarysearch(arr, mid + 1, high, item)
    else:
        return None