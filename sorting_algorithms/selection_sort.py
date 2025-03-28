def selection_sort(array: list[int]) -> None:
    """
    Sorts the given list in ascending order using the Selection Sort algorithm.

    This algorithm repeatedly finds the minimum element from the unsorted part and
    swaps it with the first unsorted element. The process is repeated until
    the entire list is sorted.

    :param array: The list of integers to be sorted.

    Time Complexity: 
        - Best, worst, and average case: O(n^2) due to nested loops.
    
    Space Complexity: O(1), as sorting is performed in-place without extra memory.
    """
    n = len(array)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def print_array(array: list[int]) -> None:
    """
    Prints the elements of an array in a single line, separated by spaces.

    :param array: The list of integers to be printed.

    Time Complexity: O(n), where n is the number of elements in `array`.
    Space Complexity: O(1), as no additional space is used.
    """
    for i in array:
        print(i, end=" ")
    print()


def main():
    """
    Demonstrates the usage of selection sort on an example array.

    This function initializes an unordered list, prints it, sorts it using selection sort,
    and prints the ordered list.

    Time Complexity: O(n^2), where n is the number of elements in `array`.
    Space Complexity: O(1), because selection sort is an in-place algorithm that modifies the input array directly.
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print("Unordered array:")
    print_array(array)
    
    selection_sort(array)
    print("\nOrdered array:")
    print_array(array)


if __name__ == "__main__":
    main()
