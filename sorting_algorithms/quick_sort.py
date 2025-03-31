def quick_sort(array: list[int], low: int, high: int) -> None:
    """
    Performs an in-place Quick Sort on the given list.

    :param arr: List of integers to sort.
    :param low: Starting index of the segment to sort.
    :param high: Ending index of the segment to sort.

    Time Complexity:
      - Best/Average: O(n log n)
      - Worst (if poorly pivoted): O(n^2)
    Space Complexity: O(log n) due to recursion.
    """
    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index - 1)
        quick_sort(array, pivot_index + 1, high)

def partition(array: list[int], low: int, high: int) -> int:
    """
    Partitions the array for Quick Sort.

    :param arr: List of integers.
    :param low: Starting index.
    :param high: Ending index.
    :return: The final index of the pivot.
    """
    pivot = array[(low + high) // 2]  # Middle pivot
    i, j = low, high

    while i <= j:
        while array[i] < pivot:
            i += 1
        while array[j] > pivot:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]  # Swap
            i += 1
            j -= 1
    return i  # New pivot index

def main():
    """
    Demonstrates the usage of Quick Sort on an example array.

    This function initializes an unordered list, prints it, sorts it using Quick Sort,
    and prints the ordered list.

    Time Complexity: O(n log n) on average.
    Space Complexity: O(log n) due to recursive calls.
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print(f"Unsorted array: {array}")

    quick_sort(array, 0, len(array) - 1)

    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
