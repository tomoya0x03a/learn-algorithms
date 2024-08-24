import unittest
from typing import Optional

Node = tuple[Optional[int], Optional[int], int]
Nodes = list[Node]

class BinaryTree():
    """
    二分木を表現するクラス。
    
    Attributes:
        nodes (list): ノードのリスト。各ノードは (左の子ノードのインデックス, 右の子ノードのインデックス, 値) のタプルです。
        
    Methods:
        traverse: 二分木の中間順走査を行い、値のリストを返す。
    """
    
    def __init__(self, nodes: Nodes) -> None:
        """
        コンストラクタ。二分木のノードのリストを受け取り、二分木を初期化します。
        
        Args:
            nodes (list): ノードのリスト。各ノードは (左の子ノードのインデックス, 右の子ノードのインデックス, 値) のタプルです。
        """
        self.nodes = nodes

    def traverse(self) -> list[int]:
        """
        二分木の中間順走査を行い、値のリストを返す。
        
        Returns:
            list: 中間順走査による値のリスト。
        """
        def inorder_traversal(index: Optional[int]) -> list[int]:
            if index is None:
                return []
    
            left_child = self.nodes[index][0]
            right_child = self.nodes[index][1]
            value = self.nodes[index][2]
    
            return inorder_traversal(left_child) + [value] + inorder_traversal(right_child)
    
        return inorder_traversal(0)


class TestBinaryTree(unittest.TestCase):
    """
    BinaryTree クラスのユニットテスト。
    
    Methods:
        setUp: テストケースごとに共通のセットアップを行う。
        test_traverse: traverse メソッドのテスト。
    """
    
    def setUp(self):
        """
        テスト用のデータセットを準備する。
        """
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
        """
        traverse メソッドが正しく中間順走査を行い、期待される値のリストを返すことを確認する。
        """
        expected_values = [2, 5, 6, 8, 9, 10, 11, 12]
    
        binary_tree = BinaryTree(self.nodes)
        self.assertEqual(binary_tree.traverse(), expected_values)


if __name__ == "__main__":
    unittest.main()
