import unittest
from arachnea import arachnea

class TestArachnea(unittest.TestCase):
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_map_and_filter(self):
        # Mapping and filtering: Square the elements and filter odd numbers
        result = (
            arachnea(self.arr)
            .map(lambda ele: ele * ele)
            .filter(lambda ele: ele % 2 == 0)
            .collect()
        )
        expected = [4, 16, 36, 64, 100]
        self.assertEqual(result, expected)

    def test_reduce_to_sum(self):
        # Reduce to sum: Sum all elements
        result = (
            arachnea(self.arr)
            .reduce(lambda acc, ele: acc + ele, 0)
        )
        expected = sum(self.arr)
        self.assertEqual(result, expected)

    def test_find_element(self):
        # Find element: Find the first element greater than 5
        result = (
            arachnea(self.arr)
            .find(lambda ele: ele > 5)
        )
        expected = 6
        self.assertEqual(result, expected)

    def test_remove_element(self):
        # Remove element: Remove the first occurrence of 3
        result = (
            arachnea(self.arr)
            .remove(3)
            .collect()
        )
        expected = [1, 2, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(result, expected)

    def test_for_each_operation(self):
        # ForEach operation: Print each element
        output = []
        (
            arachnea(self.arr)
            .forEach(lambda ele: output.append(ele))
            .collect()
        )
        expected = self.arr
        self.assertEqual(output, expected)

    def test_chaining_operations(self):
        # Chaining operations: Filter numbers greater than 5, double them, and sum
        result = (
            arachnea(self.arr)
            .filter(lambda ele: ele > 5)
            .map(lambda ele: ele * 2)
            .reduce(lambda acc, ele: acc + ele, 0)
        )
        expected = sum([ele * 2 for ele in self.arr if ele > 5])
        self.assertEqual(result, expected)

    def test_combining_operations(self):
        # Combining operations: Remove even numbers, square elements, and collect as strings
        result = (
            arachnea(self.arr)
            .filter(lambda ele: ele % 2 != 0)
            .map(lambda ele: ele * ele)
            .map(lambda ele: str(ele))
            .collect()
        )
        expected = [str(ele * ele) for ele in self.arr if ele % 2 != 0]
        self.assertEqual(result, expected)

    def test_error_cases(self):
        # Error cases: Test removing elements and handling an empty array
        result = (
            arachnea([])
            .remove(1)
            .collect()
        )
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
