"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # When a value is inserted, existing elements at that position
    # and beyond shift one position to the right.
    # Insertions near the beginning require more shifting than
    # insertions at the end.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validating the index prevents runtime errors and allows
    # the program to safely handle invalid user requests.
    if index < 0 or index >= len(lst):
        return None

    return lst.pop(index)


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because each element is examined
    # sequentially until the value is found or the list ends.
    for i in range(len(lst)):
        if lst[i] == value:
            return i

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    contacts = ["Alice", "Bob", "Charlie", "David"]

    print("Original list:", contacts)

    insert_at(contacts, 0, "Zoe")
    print("After inserting at beginning:", contacts)

    insert_at(contacts, len(contacts) // 2, "Emma")
    print("After inserting in middle:", contacts)

    insert_at(contacts, len(contacts), "Frank")
    print("After inserting at end:", contacts)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    removed = delete_at(contacts, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", contacts)

    removed = delete_at(contacts, len(contacts) // 2)
    print("Removed from middle:", removed)
    print("Updated list:", contacts)

    removed = delete_at(contacts, len(contacts) - 1)
    print("Removed from end:", removed)
    print("Updated list:", contacts)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    result = search_value(contacts, "Bob")
    print("Search for 'Bob':", result)

    result = search_value(contacts, "Michael")
    print("Search for 'Michael':", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    print("Deleting using invalid index:")
    print(delete_at(contacts, 100))

    empty_list = []

    print("\nInsert into empty list:")
    insert_at(empty_list, 0, "First Item")
    print(empty_list)

    print("\nDelete from empty list:")
    print(delete_at([], 0))

    # Real-world application
    print("\n=== REAL-WORLD SCENARIO ===")
    print("This list represents a contact list application.")
    print("Contacts can be added, removed, and searched as needed.")

    print("\n=== MEMORY DISCUSSION ===")
    print("As more items are added to the list, more memory is used")
    print("because each element must be stored in memory.")


if __name__ == "__main__":
    main()