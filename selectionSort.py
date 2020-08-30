def runSelectionSort(array):
    for i in range(len(array)-1):
        minIndex = i
        for j in range(i+1, len(array)-1):
            if array[j] < array[minIndex]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]