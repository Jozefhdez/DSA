def exchange_sort(array: list[int]) -> None:
    """
    Performs an in-place Exchange Sort on the given list.

    :param array: List of integers to sort.

    Time Complexity:
      - Best/Worst/Average: O(n^2) due to nested iteration.
    Space Complexity: O(1) since it operates in-place.
    """
    n = len(array)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]  # Swap

def main():
    """
    Demonstrates the usage of Exchange Sort on an example array.

    This function initializes an unordered list, prints it, sorts it using Exchange Sort,
    and prints the ordered list.

    Time Complexity: O(n^2) due to the nested loops.
    Space Complexity: O(1) since it operates in-place.
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print(f"Unsorted array: {array}")

    exchange_sort(array)

    print(f"Sorted array: {array}")

if __name__ == "__main__":
    main()
