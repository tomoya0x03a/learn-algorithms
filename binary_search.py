import unittest

def binary_search(sequence, target):
   """リスト内で目標値を２分探索する関数。

   sequence: 整列されたリスト
   target: 探索対象の値
   return: targetがsequence内に存在する場合はそのインデックスを、存在しない場合はNoneを返す
   """
   length = len(sequence)
   low = 0
   high = length - 1

   # 二分探索の実行
   while low <= high:
       middle = (low + high) // 2

       # 対象値が中央値と一致する場合、そのインデックスを返す
       if target == sequence[middle]:
           return middle

       # 対象値が中央値より小さい場合、下半分を探索
       elif target < sequence[middle]:
           high = middle - 1

       # 対象値が中央値より大きい場合、上半分を探索
       elif target > sequence[middle]:
           low = middle + 1

   # 対象値がsequence内に存在しない場合、Noneを返す
   return None

class TestBinarySearch(unittest.TestCase):
    def setUp(self):
        # テスト用のデータセット
        self.sequence = [1, 4, 7, 9, 10, 16]

    def test_existing_value(self):
        # 存在する値の場合のテスト
        result = binary_search(self.sequence, 1)
        self.assertEqual(result, 0)

   def test_target_at_start_of_list(self):
       # リストの最初に対象値が存在する場合のテスト
       result = binary_search(self.sequence, 1)
       self.assertEqual(result, 0)

   def test_target_at_end_of_list(self):
       # リストの最後に対象値が存在する場合のテスト
       result = binary_search(self.sequence, 16)
       self.assertEqual(result, 5)

    def test_non_existing_value(self):
        # 存在しない値の場合のテスト
        result = binary_search(self.sequence, 8)
        self.assertIsNone(result)

   def test_empty_list(self):
       # 空のリストの場合のテスト
       result = binary_search([], 1)
       self.assertIsNone(result)

   def test_single_element_list(self):
       # 単一要素のリストの場合のテスト
       result = binary_search([1], 1)
       self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()