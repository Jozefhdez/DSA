def linear_search(arr: list[int], target: int) -> int:
    """
    Performs a linear search on a list.

    This function scans the list from left to right and returns the index
    of the first occurrence of `target`, if found.

    :param arr: A list of integers to search in.
    :param target: The integer to find.
    :return: The index of the target if found, otherwise -1.

    Time Complexity: O(n), where n is the length of `arr`.
    Space Complexity: O(1) (constant extra space usage).
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1  # Target not found

def main():
    # Example usage
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    target = 6
    result = linear_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

if __name__ == "__main__":
    main()
