from .bubble_sort import bubble_sort
from .merge_sort import merge_sort
from .quick_sort import quick_sort
from .insertion_sort import insertion_sort
from .selection_sort import selection_sort
from .heap_sort import heap_sort

class MoSort:
    def __init__(self):
        # Assign sorting functions as attributes
        self.bubble_sort = bubble_sort
        self.merge_sort = merge_sort
        self.quick_sort = quick_sort
        self.insertion_sort = insertion_sort
        self.selection_sort = selection_sort
        self.heap_sort = heap_sort

# Create an instance of MoSort to use as 'ms'
ms = MoSort()
