"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """

    # Linear search checks each element one at a time.
    # In the worst case, every item in the list must be examined.
    # This gives linear search O(n) time complexity.
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:

        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        # If target is smaller, eliminate the right half.
        if target < lst[middle]:
            right = middle - 1

        # If target is larger, eliminate the left half.
        else:
            left = middle + 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    small_data = [5, 10, 15, 20, 25]

    print("Dataset:", small_data)

    print("Linear Search for 15:",
          linear_search(small_data, 15))

    print("Binary Search for 15:",
          binary_search(small_data, 15))

    print("Linear Search for 99:",
          linear_search(small_data, 99))

    print("Binary Search for 99:",
          binary_search(small_data, 99))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    large_data = list(range(1, 1001))

    print("Searching for 875 in a dataset of 1000 elements.")

    print("Linear Search:",
          linear_search(large_data, 875))

    print("Binary Search:",
          binary_search(large_data, 875))

    # Binary search becomes more efficient as data grows because
    # it repeatedly cuts the remaining search space in half.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("Empty list search:")
    print("Linear:", linear_search(empty_list, 10))
    print("Binary:", binary_search(empty_list, 10))

    # Edge Case 2: Single-element list
    single_item = [50]

    print("\nSingle-element list:")
    print("Linear:", linear_search(single_item, 50))
    print("Binary:", binary_search(single_item, 50))

    # Edge Case 3: First element
    print("\nFirst element search:")
    print("Linear:", linear_search(small_data, 5))
    print("Binary:", binary_search(small_data, 5))

    # Edge Case 4: Last element
    print("\nLast element search:")
    print("Linear:", linear_search(small_data, 25))
    print("Binary:", binary_search(small_data, 25))

    # ===============================
    # REAL-WORLD EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD SEARCH SCENARIO ===")
    print("A student information system may use binary search")
    print("to quickly find student scores in a sorted dataset.")
    print("Linear search may still be useful for small or")
    print("unsorted datasets where sorting is not practical.")


if __name__ == "__main__":
    main()