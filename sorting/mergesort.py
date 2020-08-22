'''
    Mergesort
    - first the list is recursively divided down to pairs of 2
    - then sorts those pairs, and then
    - merges all the pairs until the entire list is mergesorted
'''

def sort(a, inplace=True):
    if not inplace:
        a = list(a)
    n = len(a)
    aux = [None] * n
    rec_sort(a, aux, 0, n - 1)
    return a

def rec_sort(a, aux, lo, hi):
    # first sort a[lo .. hi]
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2
    rec_sort(a, aux, lo, mid) # sort left half
    rec_sort(a, aux, mid + 1, hi) # sort the right half
    merge(a, aux, lo, mid, hi) # merge the two halfs

def merge(a, aux, lo, mid, hi):
    i = lo
    j = mid + 1
    
    # copy a[lo .. hi] to aux[lo .. hi]
    k = lo
    while k <= hi:
        aux[k] = a[k]
        k += 1
    
    # merge back to a[lo .. hi]
    k = lo
    while k <= hi:
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1
        k += 1
