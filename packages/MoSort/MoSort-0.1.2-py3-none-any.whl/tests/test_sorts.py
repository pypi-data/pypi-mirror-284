import unittest
from MSort import bubble_sort, merge_sort, quick_sort, insertion_sort, selection_sort, heap_sort

class TestSortingAlgorithms(unittest.TestCase):

    def setUp(self):
        self.unsorted_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        self.sorted_list = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.unsorted_list.copy()), self.sorted_list)

    def test_heap_sort(self):
        self.assertEqual(heap_sort(self.unsorted_list.copy()), self.sorted_list)

if __name__ == '__main__':
    unittest.main()
