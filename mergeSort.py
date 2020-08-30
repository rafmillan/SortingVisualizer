def merge(array, leftIndex, rightIndex, middle):
    leftCopy = array[leftIndex:middle + 1]
    rightCopy = array[middle+1:rightIndex+1]
    leftCopyIndex = 0
    rightCopyIndex = 0
    sortedIndex = leftIndex

    while leftCopyIndex < len(leftCopy) and rightCopyIndex < len(rightCopy):

        if leftCopy[leftCopyIndex] <= rightCopy[rightCopyIndex]:
            array[sortedIndex] = leftCopy[leftCopyIndex]
            leftCopyIndex = leftCopyIndex + 1
        else:
            array[sortedIndex] = rightCopy[rightCopyIndex]
            rightCopyIndex = rightCopyIndex + 1

        sortedIndex = sortedIndex + 1

    while leftCopyIndex < len(leftCopy):
        array[sortedIndex] = leftCopy[leftCopyIndex]
        leftCopyIndex = leftCopyIndex + 1
        sortedIndex = sortedIndex + 1

    while rightCopyIndex < len(rightCopy):
        array[sortedIndex] = rightCopy[rightCopyIndex]
        rightCopyIndex = rightCopyIndex + 1
        sortedIndex = sortedIndex + 1

def runMergeSort(array, leftIndex, rightIndex):
    if leftIndex >= rightIndex:
        return

    middle = (leftIndex + rightIndex)//2
    runMergeSort(array, leftIndex, middle)
    runMergeSort(array, middle + 1, rightIndex)
    merge(array, leftIndex, rightIndex, middle)