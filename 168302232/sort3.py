def quickSort(ls, low, high):
    i = low
    j = high
 
    if i >= j:
        return ls
 
    key = ls[i]
 
    while i < j:
        while i < j and ls[j] >= key:
            j -= 1
        ls[i], ls[j] = ls[j], ls[i]
 
        while i < j and ls[i] <= key:
            i += 1
        ls[i], ls[j] = ls[j], ls[i]
 
    quickSort(ls, low, i - 1)
    quickSort(ls, j + 1, high)
 
    return ls


