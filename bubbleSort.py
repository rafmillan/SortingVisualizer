def runBubbleSort(array):
    hasSwapped = True

    numIterations = 0

    while(hasSwapped):
        hasSwapped = False
        for i in range(len(array) - numIterations - 1):
            if array[i] > array[i+1]:
                # Swap
                array[i], array[i+1] = array[i+1], array[i]
                hasSwapped = True
        numIterations += 1