import unittest
from typing import List

class SelectionSort:
    """
    SelectionSort クラスは、選択ソートアルゴリズムを実装します。
    """

    def __init__(self, data: List[int]) -> None:
        """
        クラスの初期化メソッド。

        Args:
            data (List[int]): ソート対象の整数リスト。
        """
        self.data = data[:]  # 入力リストのコピーを作成

    def sort(self) -> List[int]:
        """
        リストを選択ソートアルゴリズムでソートします。

        Returns:
            List[int]: ソートされたリスト。
        """
        n = len(self.data)

        for i in range(n - 1):
            min_index = i  # 最小値のインデックス

            for j in range(i + 1, n):
                if self.data[min_index] > self.data[j]:
                    min_index = j

            # 最小値を先頭の値と入れ替える
            self.data[i], self.data[min_index] = self.data[min_index], self.data[i]

        return self.data


class TestSelectionSort(unittest.TestCase):
    """
    SelectionSort クラスのユニットテストクラス。
    """

    def test_sort(self):
        """一般的なソートのテスト"""
        input_list = [8, 5, 2, 1, 7]
        expected_list = [1, 2, 5, 7, 8]
        selection_sort = SelectionSort(input_list)
        self.assertEqual(selection_sort.sort(), expected_list)

    def test_empty_list(self):
        """空リストのソートテスト"""
        selection_sort = SelectionSort([])
        self.assertEqual(selection_sort.sort(), [])

    def test_single_element_list(self):
        """単一要素のリストのソートテスト"""
        selection_sort = SelectionSort([1])
        self.assertEqual(selection_sort.sort(), [1])

    def test_sorted_list(self):
        """既にソート済みのリストのテスト"""
        selection_sort = SelectionSort([1, 2, 3, 4, 5])
        self.assertEqual(selection_sort.sort(), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        """重複要素を含むリストのテスト"""
        selection_sort = SelectionSort([3, 2, 1, 2, 3])
        self.assertEqual(selection_sort.sort(), [1, 2, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()