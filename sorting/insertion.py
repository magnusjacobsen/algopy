import util

'''
    Insertion sort
    - is sensitive to input

    - Running time: quadratic
    --> worst case: N^2/2 compares, N^2/2 swaps
    --> avg case: N^2/4 compares, N^2/4 swaps
    --> best case: N - 1 compares, 0 swaps
    
    Adapted from Algorithms, 4th edition, by Robert Sedgewick & Kevin Wayne
    --> page 251
'''
def sort(a, inplace=True):
    if not inplace:
        a = list(a)
    n = len(a)
    for i in range(1,n):
        j = i
        while j > 0 and a[j] < a[j - 1]:
            util.swap(a, j, j -1)
            j = j - 1
    return a
