import unittest

class InsertSort():
    def __init__(self, data: list[int]) -> None:
        self.data: list[int] = data

    def sort(self) -> list[int]:
        length: int = len(self.data)

        for target_index in range(1, length):
            insert_index: int = target_index # ターゲットの挿入位置
            target_value: int = self.data[target_index] # ターゲットの値
            
            for temp_index in range(target_index - 1, -1, -1): # ターゲットよりも左側の値
                # ターゲットの値が左の値より小さければ
                if target_value < self.data[temp_index]:
                    insert_index = temp_index # 挿入位置を変更する

            # ターゲットの位置に変化があれば
            if insert_index != target_index:

                # ターゲットよりも大きい値を右にずらす
                for i in range(target_index -1, insert_index -1, -1):
                    self.data[i + 1] = self.data[i]

                # ターゲットを挿入する
                self.data[insert_index] = target_value

        return self.data
                    
class TestInsertSort(unittest.TestCase):
    """
    InsertSortクラスのユニットテストクラス。
    """

    def test_sort(self):
        """一般的なソートのテスト"""
        input_list = [8, 5, 2, 1, 7]
        expected_list = [1, 2, 5, 7, 8]
        insert_sort = InsertSort(input_list)
        self.assertEqual(insert_sort.sort(), expected_list)

    def test_empty_list(self):
        """空リストのソートテスト"""
        insert_sort = InsertSort([])
        self.assertEqual(insert_sort.sort(), [])

    def test_single_element_list(self):
        """単一要素のリストのソートテスト"""
        insert_sort = InsertSort([1])
        self.assertEqual(insert_sort.sort(), [1])

    def test_sorted_list(self):
        """既にソート済みのリストのテスト"""
        insert_sort = InsertSort([1, 2, 3, 4, 5])
        self.assertEqual(insert_sort.sort(), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        """重複要素を含むリストのテスト"""
        insert_sort = InsertSort([3, 2, 1, 2, 3])
        self.assertEqual(insert_sort.sort(), [1, 2, 2, 3, 3])


if __name__ == "__main__":
    unittest.main()
                    
