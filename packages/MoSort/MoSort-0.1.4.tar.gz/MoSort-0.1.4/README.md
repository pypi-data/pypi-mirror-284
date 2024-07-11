# MoSort

MoSort is a Python library that provides implementations of several different sorting algorithms: Bubble Sort, Quick Sort, Merge Sort, Insertion Sort, Selection Sort, and Heap Sort.

## What is it?

MoSort is a Python package that provides fast, flexible, and efficient implementations of various sorting algorithms. It aims to be a comprehensive tool for sorting arrays in different ways, making it easy to use and integrate into your projects.

## Main Features

Here are all the sorting algorithms that MoSort provides:

**Bubble Sort:** A simple comparison-based sorting algorithm.  
**Quick Sort:** An efficient, comparison-based, divide-and-conquer sorting algorithm.  
**Merge Sort:** A stable, comparison-based, divide-and-conquer sorting algorithm.  
**Insertion Sort:** A simple, comparison-based, stable sorting algorithm.  
**Selection Sort:** A simple, in-place comparison-based sorting algorithm.  
**Heap Sort:** A comparison-based sorting algorithm based on binary heap data structure.  


## Installation

You can install MoSort using pip:

```bash
pip install MoSort
```

## Usage

Once installed, you can import and use each sorting algorithm provided by MoSort. Here's an example of how to use Quick Sort:

```bash
from MoSort import ms

array = [64, 25, 12, 22, 11]
sorted_array = ms.quick_sort(array)    #Replace quick_sort with any other sorting algorithm from MoSort library to use it accordingly.
print("Sorted array using Quick Sort:", sorted_array)
```


## Contributing
Contributions, bug reports, and feature requests are welcome! 

## License

This project is licensed under the MIT License.