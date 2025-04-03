def combo_sort(array: list[int]) -> None:
    """
    Performs an in-place Combo Sort on the given list.

    :param array: List of integers to sort.

    Time Complexity:
      - Best/Average: O(n log n) in the ideal case.
      - Worst: O(n^2) when the gap sequence is not efficient.
    Space Complexity: O(1) since it operates in-place.
    """
    shrink_factor = 1.3  # Gap shrink factor
    n = len(array)
    gap = n  # Initial gap
    swapped = True
    
    while gap > 1 or swapped:
        # Reduce the gap using the shrink factor
        gap = max(1, int(gap / shrink_factor))
        swapped = False
        
        # Traverse the array comparing and swapping elements separated by the current gap
        for i in range(n - gap):
            if array[i] > array[i + gap]:
                array[i], array[i + gap] = array[i + gap], array[i]  # Swap
                swapped = True

def main():
    """
    Demonstrates the usage of Combo Sort on an example array.

    This function initializes an unordered list, prints it, sorts it using Combo Sort,
    and prints the ordered list.

    Time Complexity: O(n^2) in the worst case, O(n log n) on average.
    Space Complexity: O(1) since it operates in-place.
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print(f"Unsorted array: {array}")

    combo_sort(array)

    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
