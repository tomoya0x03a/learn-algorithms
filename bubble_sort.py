import unittest

class BubbleSort:
    """
    バブルソートアルゴリズムを実装するクラス。
    
    Attributes:
        data (list[int]): ソート対象の整数のリスト。
    """
    
    def __init__(self, data: list[int]) -> None:
        """
        バブルソートの初期化メソッド。

        Args:
            data (list[int]): ソート対象の整数のリスト。
        """
        self.data: list[int] = data

    def sort(self) -> list[int]:
        """
        バブルソートを実行し、ソートされたリストを返す。

        Returns:
            list[int]: ソートされた整数のリスト。
        """
        length: int = len(self.data) - 1  # データの長さを計算

        for outer_index in range(length):  # 外側のループ
            current_index: int = outer_index  # 現在のインデックスを設定
            for inner_index in range(length, current_index, -1):  # 内側のループ
                # 隣接要素の比較と入れ替え
                if self.data[inner_index] < self.data[inner_index - 1]:  
                    # 要素を入れ替える
                    self.data[inner_index], self.data[inner_index - 1] = self.data[inner_index - 1], self.data[inner_index]
        
        return self.data  # ソートされたリストを返す

                    

class TestBubbleSort(unittest.TestCase):
    """
    BubbleSortクラスのユニットテストクラス。
    """

    def test_sort(self):
        """一般的なソートのテスト"""
        input_list = [8, 5, 2, 1, 7]
        expected_list = [1, 2, 5, 7, 8]
        bubble_sort = BubbleSort(input_list)
        self.assertEqual(bubble_sort.sort(), expected_list)

    def test_empty_list(self):
        """空リストのソートテスト"""
        bubble_sort = BubbleSort([])
        self.assertEqual(bubble_sort.sort(), [])

    def test_single_element_list(self):
        """単一要素のリストのソートテスト"""
        bubble_sort = BubbleSort([1])
        self.assertEqual(bubble_sort.sort(), [1])

    def test_sorted_list(self):
        """既にソート済みのリストのテスト"""
        bubble_sort = BubbleSort([1, 2, 3, 4, 5])
        self.assertEqual(bubble_sort.sort(), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        """重複要素を含むリストのテスト"""
        bubble_sort = BubbleSort([3, 2, 1, 2, 3])
        self.assertEqual(bubble_sort.sort(), [1, 2, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
