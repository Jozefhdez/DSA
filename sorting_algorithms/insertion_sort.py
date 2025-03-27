def insertion_sort(array: list[int]) -> None:
    """
    Sorts the given list in ascending order using the Insertion Sort algorithm.

    This algorithm builds the sorted list one element at a time by repeatedly taking 
    the next element from the input list and inserting it into its correct position 
    within the sorted portion of the list.

    :param array: The list of integers to be sorted.

    Time Complexity: 
        - Best case: O(n) when the list is already sorted.
        - Average and worst case: O(n^2) due to nested iterations.
    
    Space Complexity: O(1), as sorting is performed in-place without using extra memory.
    """
    n = len(array)

    for i in range(n):
        key = array[i]
        j = i - 1

        # Move elements of array[0..i-1] that are greater than key one position ahead
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


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
    Demonstrates the usage of insertion sort on an example array.

    This function initializes an unordered list, prints it, sorts it using insertion sort,
    and prints the ordered list.

    Time Complexity: O(n^2) in the average and worst case, O(n) in the best case.
    Space Complexity: O(1), because insertion sort is an in-place algorithm.
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print("Unordered array: ")
    print_array(array)
    
    insertion_sort(array)
    print("\nOrdered array: ")
    print_array(array)


if __name__ == "__main__":
    main()
