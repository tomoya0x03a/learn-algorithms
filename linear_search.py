import unittest


def linear_search(values, target):
    """リスト内で目標値を線形探索する関数。

    Args:
        values (list): 探索対象のリスト。
        target: 探したい値。

    Returns:
        int or None: 見つかった場合はインデックス、見つからない場合はNone。
    """
    for i, value in enumerate(values):
        if value == target:
            return i
    return None


class TestLinearSearch(unittest.TestCase):
    def setUp(self):
        # テスト用のデータセット
        self.values = [7, 4, 2, 8, 10, 9, 1, 5, 3, 6]

    def test_existing_value(self):
        # 存在する値の場合のテスト
        result = linear_search(self.values, 8)
        self.assertEqual(result, 3)

    def test_non_existing_value(self):
        # 存在しない値の場合のテスト
        result = linear_search(self.values, 11)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
