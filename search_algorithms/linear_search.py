def linear_search(arr: list[int], target: int) -> int:
    """
    Performs a linear search on the given list.

    :param arr: List of integers to search in.
    :param target: The integer to find.
    :return: The index of the target if found, otherwise -1.
    """
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1

if __name__ == "__main__":
    # Example usage
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    target = 6
    result = linear_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")