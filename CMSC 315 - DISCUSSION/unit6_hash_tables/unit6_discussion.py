"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Dictionaries behave like hash tables by storing
    # key-value pairs. Keys are hashed internally,
    # allowing fast access to associated values.

    student_scores = {}

    student_scores["Alice"] = 95
    student_scores["Bob"] = 87
    student_scores["Charlie"] = 91
    student_scores["David"] = 84
    student_scores["Emma"] = 98

    print("\n=== INSERT OPERATIONS ===")
    print("Dictionary contents:")
    print(student_scores)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Dictionary lookup uses a key to quickly locate
    # a value through hashing.

    print("\n=== LOOKUP OPERATIONS ===")

    print("Alice's score:", student_scores["Alice"])
    print("Charlie's score:", student_scores["Charlie"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Assigning a new value to an existing key updates
    # the stored value while keeping the same key.

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(student_scores)

    student_scores["Bob"] = 92

    print("After updating Bob's score:")
    print(student_scores)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Removing a key deletes both the key and its value
    # from the dictionary.

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:")
    print(student_scores)

    del student_scores["David"]

    print("After deleting David:")
    print(student_scores)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Lookup a missing key
    print("\nLookup missing key:")
    print(student_scores.get("Michael", "Key not found"))

    # Edge Case 2: Delete a missing key safely
    print("\nDelete missing key safely:")
    removed_value = student_scores.pop("Sarah", "Key not found")
    print(removed_value)

    # Edge Case 3: Empty dictionary
    print("\nEmpty dictionary:")
    empty_dict = {}
    print(empty_dict)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD HASH TABLE EXAMPLE ===")
    print("A social media platform can store user profiles")
    print("using usernames as keys and profile information")
    print("as values. Hash tables allow profiles to be")
    print("retrieved quickly even when millions of users")
    print("exist in the system.")


if __name__ == "__main__":
    main()