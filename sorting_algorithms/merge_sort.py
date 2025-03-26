def merge(array: list[int], front: int, mid: int, back: int) -> None:
    """
    Merges two subarrays of `array` in sorted order.

    The first subarray is `array[front:mid+1]` and the second subarray is `array[mid+1:back+1]`.
    This function assumes that both subarrays are already sorted.

    :param array: The list of integers to merge.
    :param front: The starting index of the first subarray.
    :param mid: The ending index of the first subarray.
    :param back: The ending index of the second subarray.

    Time Complexity: O(n), where n is the total number of elements in the merged subarrays.
    Space Complexity: O(n), as additional space is used for temporary arrays.
    """
    n1 = mid - front + 1
    n2 = back - mid

    left = [0] * n1
    right = [0] * n2

    for i in range(n1):
        left[i] = array[front + i]

    for i in range(n2):
        right[i] = array[mid + 1 + i]

    i = 0
    j = 0
    k = front

    while i < n1 and j < n2:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort(array: list[int], left: int, right: int) -> None:
    """
    Sorts an array using the merge sort algorithm.

    This function recursively divides the array into two halves,
    sorts them individually, and then merges the sorted halves.

    :param array: The list of integers to be sorted.
    :param left: The starting index of the portion to be sorted.
    :param right: The ending index of the portion to be sorted.

    Time Complexity: O(n log n), where n is the number of elements in `array`.
    Space Complexity: O(n), due to the additional space required for merging.
    """
    if left >= right:
        return
    else:
        mid = left + (right - left) // 2
        merge_sort(array, left, mid)
        merge_sort(array, mid + 1, right)
        merge(array, left, mid, right)

def print_array(arr_1: list[int]) -> None:
    """
    Prints the elements of an array in a single line.

    :param arr: The list of integers to be printed.

    Time Complexity: O(n), where n is the number of elements in `arr`.
    Space Complexity: O(1), as no additional space is used.
    """
    for i in arr_1:
        print(i, end=" ")
    print()

def main():
    """
    Demonstrates the usage of merge sort on an example array.

    This function initializes an unordered list, prints it, sorts it using merge sort,
    and prints the ordered list.

    Time Complexity: O(n log n), where n is the number of elements in `array`.
    Space Complexity: O(n), due to the merge sort implementation.
    """
    array = [1, 4, 2, 3, 12, 9, 28, 39, 33, 35]
    print("Unordered array: ")
    print_array(array)
    
    merge_sort(array, 0, len(array) - 1)
    print("\nOrdered array: ")
    print_array(array)

if __name__ == "__main__":
    main()
