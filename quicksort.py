def partition(arr: list[int], low: int, high: int) -> int:
    x = low - 1
    for i in range(low, high):
        if arr[i] < arr[high]:
            x += 1
            arr[i], arr[x] = arr[x], arr[i]
        
    arr[x + 1], arr[high] = arr[high], arr[x + 1]

    return x + 1


def quicksort(arr: list[int], low: int, high: int):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)