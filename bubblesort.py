def bubblesort(arr: list[int]):
    for i in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            return