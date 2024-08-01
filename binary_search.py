import unittest

class BinarySearch():
    """
    二分探索を実行するクラス。
    
    Attributes:
        sequence (list): ソートされたデータのリスト。
    """
    
    def __init__(self, sequence):
        """
        BinarySearchのコンストラクタ。
        
        Args:
            sequence (list): ソートされたデータのリスト。
        """
        self.sequence = sequence

    def search(self, target):
        """
        二分探索を用いてtargetをsequenceの中から探す。
        
        Args:
            target (int): 探索対象の値。
        
        Returns:
            int or None: targetが見つかった場合はそのインデックス、見つからなかった場合はNoneを返す。
        """
        low = 0
        hi = len(self.sequence) - 1

        while low <= hi:
            mid = (low + hi) // 2
            
            # 値が見つかったらインデックスを返す
            if self.sequence[mid] == target:
                return mid

            # 探索範囲を半分に絞り込む
            if target < self.sequence[mid]:
                hi = mid - 1  # 対象値が中央値より小さい場合、探索範囲を下半分に絞り込む
            else:
                low = mid + 1  # 対象値が中央値より大きい場合、探索範囲を上半分に絞り込む

        # 最後まで探索してtargetが見つからなかった場合Noneを返す
        return None

class TestBinarySearch(unittest.TestCase):
    """
    BinarySearchクラスのテストケースを実行するクラス。
    """
    
    def test_even_number_of_elements_target_exists(self):
        """
        偶数の要素数を持つsequenceでtargetが存在する場合のテスト。
        """
        sequence = [1, 2, 9, 12, 20, 25, 32, 39]
        binary_search = BinarySearch(sequence)

        # それぞれのtargetが正しいインデックスで見つかるかを確認
        self.assertEqual(binary_search.search(1), 0)
        self.assertEqual(binary_search.search(2), 1)
        self.assertEqual(binary_search.search(9), 2)
        self.assertEqual(binary_search.search(12), 3)
        self.assertEqual(binary_search.search(20), 4)
        self.assertEqual(binary_search.search(25), 5)
        self.assertEqual(binary_search.search(32), 6)
        self.assertEqual(binary_search.search(39), 7)

    def test_odd_number_of_elements_target_exists(self):
        """
        奇数の要素数を持つsequenceでtargetが存在する場合のテスト。
        """
        sequence = [1, 2, 9, 12, 20, 25, 32]
        binary_search = BinarySearch(sequence)

        # それぞれのtargetが正しいインデックスで見つかるかを確認
        self.assertEqual(binary_search.search(1), 0)
        self.assertEqual(binary_search.search(2), 1)
        self.assertEqual(binary_search.search(9), 2)
        self.assertEqual(binary_search.search(12), 3)
        self.assertEqual(binary_search.search(20), 4)
        self.assertEqual(binary_search.search(25), 5)
        self.assertEqual(binary_search.search(32), 6)

    def test_even_number_of_elements_target_does_not_exist(self):
        """
        偶数の要素数を持つsequenceでtargetが存在しない場合のテスト。
        """
        sequence = [1, 2, 9, 12, 20, 25, 32, 39]
        binary_search = BinarySearch(sequence)

        # targetが存在しないことを確認
        self.assertEqual(binary_search.search(0), None)
        self.assertEqual(binary_search.search(4), None)
        self.assertEqual(binary_search.search(10), None)
        self.assertEqual(binary_search.search(14), None)
        self.assertEqual(binary_search.search(24), None)
        self.assertEqual(binary_search.search(31), None)
        self.assertEqual(binary_search.search(37), None)
        self.assertEqual(binary_search.search(40), None)

    def test_odd_number_of_elements_target_does_not_exist(self):
        """
        奇数の要素数を持つsequenceでtargetが存在しない場合のテスト。
        """
        sequence = [1, 2, 9, 12, 20, 25, 32]
        binary_search = BinarySearch(sequence)

        # targetが存在しないことを確認
        self.assertEqual(binary_search.search(0), None)
        self.assertEqual(binary_search.search(4), None)
        self.assertEqual(binary_search.search(10), None)
        self.assertEqual(binary_search.search(14), None)
        self.assertEqual(binary_search.search(24), None)
        self.assertEqual(binary_search.search(31), None)
        self.assertEqual(binary_search.search(37), None)

if __name__ == "__main__":
    unittest.main()
