import util
'''
    Selection Sort
    - Pretty simple, and pretty bad
    - Sorts in-place by default, but can also leave the original unharmed, and then return a new sorted list 
    
    - Running time: quadratic (hint: the nested for loop)
    --> actually it is N^2 / 2 compares, and N swaps
    --> running time is agnostic to the input

    Adapted from Algorithms, 4th edition, by Robert Sedgewick & Kevin Wayne
    --> page 249
'''
def sort(a, inplace=True):
    if not inplace:
        a = list(a)
    n = len(a)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if a[j] < a[min]:
                min = j
        util.swap(a, i, min)
    return a
