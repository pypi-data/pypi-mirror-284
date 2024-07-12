from .insertion_sort import insertion_sort
from .merge_sort import merge_sort

MIN_RUN = 32

def tim_sort(arr):
    n = len(arr)
    for i in range(0, n, MIN_RUN):
        insertion_sort(arr, i, min((i + MIN_RUN - 1), n - 1))

    size = MIN_RUN
    while size < n:
        for start in range(0, n, size * 2):
            mid = start + size - 1
            end = min((start + size * 2 - 1), (n - 1))
            if mid < end:
                merge_sort(arr[start:end+1])  # using merge_sort from the library
        size *= 2
    return arr
