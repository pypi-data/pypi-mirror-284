import unittest
from MoSort import ms


class TestMoSort(unittest.TestCase):

    def setUp(self):
        # Initialize test data
        self.unsorted_array = [64, 25, 12, 22, 11]
        self.sorted_array = [11, 12, 22, 25, 64]

    def test_bubble_sort(self):
        sorted_array = ms.bubble_sort(self.unsorted_array.copy())
        self.assertEqual(sorted_array, self.sorted_array)

    def test_quick_sort(self):
        sorted_array = ms.quick_sort(self.unsorted_array.copy())
        self.assertEqual(sorted_array, self.sorted_array)

    def test_merge_sort(self):
        sorted_array = ms.merge_sort(self.unsorted_array.copy())
        self.assertEqual(sorted_array, self.sorted_array)

    def test_insertion_sort(self):
        sorted_array = ms.insertion_sort(self.unsorted_array.copy())
        self.assertEqual(sorted_array, self.sorted_array)

    def test_selection_sort(self):
        sorted_array = ms.selection_sort(self.unsorted_array.copy())
        self.assertEqual(sorted_array, self.sorted_array)

    def test_heap_sort(self):
        sorted_array = ms.heap_sort(self.unsorted_array.copy())
        self.assertEqual(sorted_array, self.sorted_array)


if __name__ == '__main__':
    unittest.main()
