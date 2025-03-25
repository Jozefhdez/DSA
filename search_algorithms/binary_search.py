def binary_search(arr: list[int], target: int) -> int:
    """
    Performs a binary search on a sorted list.

    This function assumes that `arr` is sorted in ascending order.
    If `arr` is not sorted, the results are undefined.

    :param arr: A sorted list of integers to search in.
    :param target: The integer to find.
    :return: The index of the target if found, otherwise -1.

    Time Complexity: O(log n), where n is the length of `arr`.
    Space Complexity: O(1) (iterative implementation, no extra space used).
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Avoids potential overflow in some languages
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # Target not found

def main():
    # Example usage (array must be sorted)
    arr = [1, 2, 6, 7, 8, 12, 16, 18, 32]
    target = 12
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

if __name__ == "__main__":
    main()
