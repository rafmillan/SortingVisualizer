def partition(Arr, start, end, win):
    array = Arr.getArr()
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place and we can move to next element
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]
    return high

def runQuickSort(Arr, start, end, win):
    array = Arr.getArr()
    #sleep(0.2)
    if start >= end:
        return

    p = partition(Arr, start, end, win)
    #time.sleep(0.5)
    runQuickSort(Arr, start, p-1, win)
    #sleep(0.5)
    runQuickSort(Arr, p+1, end, win)