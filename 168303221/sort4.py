def twoSort(ls1, ls2):
    ls1 = ls1 if type(ls1) is list else [ls1]
    result = []
    len1, len2, i, j = len(ls1), len(ls2), 0, 0
    while i < len1 and j < len2:
        if ls1[i] <= ls2[j]:
            result.append(ls1[i])
            i += 1
        else:
            result.append(ls2[j])
            j += 1
    result += ls1[i: ] + ls2[j: ]
    return result
 
 
def mergeSort(ls):
    if len(ls) == 1:
        return ls
 
    new_len = len(ls) // 2
    return twoSort(mergeSort(ls[: new_len]), mergeSort(ls[new_len: ]))
 

