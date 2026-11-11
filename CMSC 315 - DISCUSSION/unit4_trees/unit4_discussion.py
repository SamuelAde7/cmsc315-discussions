"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        if value < node.value:
            # Smaller values belong in the left subtree
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)

        elif value > node.value:
            # Larger values belong in the right subtree
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # BST search can ignore half the remaining values
        # by choosing either the left or right subtree.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is None:
            return

        # Visit left subtree first
        self._inorder_recursive(node.left, values)

        # Visit current node
        values.append(node.value)

        # Visit right subtree last
        self._inorder_recursive(node.right, values)

    # In-order traversal produces sorted values because
    # smaller elements are stored left and larger elements
    # are stored right in a BST.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================

    print("\n=== TREE CONSTRUCTION ===")

    bst = BST()

    values = [50, 25, 75, 10, 35, 60, 90]

    print("Values inserted:")
    print(values)

    for value in values:
        bst.insert(value)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = bst.inorder()

    print("Sorted BST values:")
    print(traversal)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    print("Search for 25:", bst.search(25))
    print("Search for 60:", bst.search(60))

    print("Search for 15:", bst.search(15))
    print("Search for 99:", bst.search(99))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Search an empty tree
    empty_tree = BST()

    print("Search empty tree for 50:")
    print(empty_tree.search(50))

    # Edge Case 2: Tree with only one node
    single_node_tree = BST()
    single_node_tree.insert(100)

    print("\nSingle-node tree traversal:")
    print(single_node_tree.inorder())

    # Edge Case 3: Duplicate value insertion
    print("\nAttempting duplicate insertion (50)")
    bst.insert(50)

    print("Traversal after duplicate insertion:")
    print(bst.inorder())

    # Real-world example
    print("\n=== REAL-WORLD BST EXAMPLE ===")
    print("Employee ID numbers can be stored in a BST.")
    print("Smaller IDs are stored in the left subtree.")
    print("Larger IDs are stored in the right subtree.")
    print("This reduces search time compared to checking every record.")


if __name__ == "__main__":
    main()