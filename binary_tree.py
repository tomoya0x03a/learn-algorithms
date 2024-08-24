import unittest
from typing import Optional

Node = tuple[Optional[int], Optional[int], int]
Nodes = list[Node]

class BinaryTree():
    def __init__(self, nodes: Nodes) -> None:
        self.nodes = nodes

    def traverse(self):
        def inorder_traversal(index: Optional[int]) -> list[int]:
            if index is None:
                return []

            left_child = self.nodes[index][0]
            right_child = self.nodes[index][1]
            value = self.nodes[index][2]

            return inorder_traversal(left_child) + [value] + inorder_traversal(right_child)

        return inorder_traversal(0)


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        # テスト用のデータセット
        self.nodes = [
            (1, 2, 10),
            (3, 4, 5),
            (5, None, 12),
            (None, None, 2),
            (6, 7, 8),
            (None, None, 11),
            (None, None, 6),
            (None, None, 9),
        ]

    def test_traverse(self):
        expected_values = [2, 5, 6, 8, 9, 10, 11, 12]

        binary_tree = BinaryTree(self.nodes)
        self.assertEqual(binary_tree.traverse(), expected_values)


if __name__ == "__main__":
    unittest.main()
