def bubble_sort(array: list[int]) -> None:
    """
    Sorts the given list in ascending order using the Bubble Sort algorithm.

    This algorithm repeatedly steps through the list, compares adjacent elements,
    and swaps them if they are in the wrong order. The process is repeated until
    the list is sorted.

    :param array: The list of integers to be sorted.

    Time Complexity: 
        - Best case: O(n) when the list is already sorted.
        - Worst and average case: O(n^2) due to nested loops.
    
    Space Complexity: O(1), as sorting is performed in-place without extra memory.
    """
    n = len(array)
    
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j + 1] :
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break


def print_array(array: list[int]) -> None:
    """
    Prints the elements of an array in a single line.

    :param arr: The list of integers to be printed.

    Time Complexity: O(n), where n is the number of elements in `arr`.
    Space Complexity: O(1), as no additional space is used.
    """
    for i in array:
        print(i, end=" ")
    print()

def main():
    """
    Demonstrates the usage of bubble sort on an example array.

    This function initializes an unordered list, prints it, sorts it using bubble sort,
    and prints the ordered list.

    Time Complexity: O(n^2), where n is the number of elements in `array`.
    Space Complexity: O(1), because bubble sort is an in-place algorithm that modifies the input array directly
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print("Unordered array: ")
    print_array(array)
    
    bubble_sort(array)
    print("\nOrdered array: ")
    print_array(array)

if __name__ == "__main__":
    main()
