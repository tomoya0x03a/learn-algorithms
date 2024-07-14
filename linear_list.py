import unittest

class LinearList():
    def __init__(self, size):
        self.data = [None] * size
        self.pointer = [None] * size
        self.head = 0

    def add(self, value):
        current = None

        # 空いてる場所にデータを挿入する
        for i in range(0, len(self.data)):
            if self.data[i] is None:
                current = i
                self.data[current] = value
                break

        # 空きがない場合
        if current is None:
            self._raise_full_error()

        # 先頭なら処理を終了する
        if current == self.head:
            return

        tail = self.head
        while True:
            if self.pointer[tail] is None: # 末尾のデータなら
                self.pointer[tail] = current # 末尾のデータのポインタに、挿入するデータのポインタを設定する
                return

            # ポンタを進める
            tail = self.pointer[tail]

    def delete(self, value):
        prev = None
        current = self.head

        while current is not None:
            if self.data[current] == value: # 削除するデータなら
                # データを削除する
                self.data[current] = None

                if prev is None: # 削除するデータが先頭の時
                    self.head = self.pointer[current] # 削除するデータのポインタを、headに設定する
                else:
                    # 削除するデータのポインタを、削除するデータの前のデータのポインタに設定する
                    self.pointer[prev] = self.pointer[current]

                return True
            
            # ポインタを進める
            prev = current
            current = self.pointer[current]

        # 削除するデータが見つからない場合
        return False

    def _raise_full_error(self):
        raise MemoryError('これ以上データを入れられません')    


class TestLinearList(unittest.TestCase):
    # データが正しく追加されるかを検証する
    def test_add_data(self):
        input_values = [0, 1, 2, 3, 4]
        expected_values = [0, 1, 2, 3, 4]


        linear_list = LinearList(5)

        for i in input_values:
            linear_list.add(i)

        self.assertEqual(linear_list.data, expected_values)


    # 保持できる要素数を超えたデータの追加でエラーが発生するかを検証する
    def test_raise_error_on_overflow(self):
        linear_list = LinearList(5)

        for i in range(5):
            linear_list.add(i)

        with self.assertRaises(MemoryError):
            linear_list.add(5)

    # データが正しく削除されるかを検証する
    def test_delete_data(self):
        input_values = [0, 1, 2, 3, 4]
        expected_values = [0, None, 2, 3, 4]

        linear_list = LinearList(5)

        for i in input_values:
            linear_list.add(i)        

        result = linear_list.delete(1)

        self.assertEqual(result, True)
        self.assertEqual(linear_list.data, expected_values)

    # 存在しないデータを削除しようとした時の動作を検証する
    def test_delete_nonexistent_data(self):
        input_values = [0, 1, 2, 3, 4]
        expected_values = [0, 1, 2, 3, 4]

        linear_list = LinearList(5)

        for i in input_values:
            linear_list.add(i)        

        result = linear_list.delete(5)

        self.assertEqual(result, False)
        self.assertEqual(linear_list.data, expected_values)

    # データを満杯にした後、一つ削除して、一つ追加する
    def test_delete_one_add_one_after_capacity(self):
        input_values = [0, 1, 2, 3, 4]
        expected_values = [0, 5, 2, 3, 4]

        linear_list = LinearList(5)

        for i in input_values:
            linear_list.add(i)

        linear_list.delete(1)
        linear_list.add(5)

        self.assertEqual(linear_list.data, expected_values)

    # 初期状態でデータを削除しようとした時の動作を検証する
    def test_delete_initial_state(self):
        expected_values = [None, None, None, None, None]

        linear_list = LinearList(5)
        result = linear_list.delete(5)

        self.assertEqual(result, False)
        self.assertEqual(linear_list.data, expected_values)


if __name__ == "__main__":
    unittest.main()