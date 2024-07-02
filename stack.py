import unittest

class stack():
    """
    スタックデータ構造を表現するクラス。
    最初に指定されたサイズの配列を使用して、要素を積み上げることができる。
    """

    def __init__(self, size):
        """
        スタックの初期化を行う。
        指定されたサイズの空の配列を生成し、ポインタを-1に設定する。
        """
        self.values = [None] * size
        self.pointer = -1

    def push(self, value):
        """
        スタックに新しい要素を積む。
        指定された値をスタックの頂部に積み込む。
        スタックが満杯になるとMemoryErrorをスローする。
        """
        if self.pointer + 1 < len(self.values):
            self.pointer += 1
            self.values[self.pointer] = value
        else:
            raise MemoryError('これ以上データを入れられません')

    def pop(self):
        """
        スタックから最上位の要素を取り出す。
        スタックの頂部にある要素を取り出し、ポインタを1つ戻す。
        スタックが空になるとIndexErrorをスローする。
        """
        if self.pointer >= 0:
            value = self.values[self.pointer]
            self.pointer -= 1
            return value
        else:
            raise IndexError('取り出すデータが存在しません')


class TestStack(unittest.TestCase):

    def test_push_and_pop_order(self):
        # スタックに要素をpushし、逆順でpopする操作が正しく行われるかを検証
        input_values = [i for i in range(1, 11)]
        output_values = []
        expected_values = [i for i in range(10, 0, -1)]

        t_stack = stack(10)

        for i in input_values:
            t_stack.push(i)
        
        for _ in range(10, 0, -1):
            output_values.append(t_stack.pop())

        self.assertEqual(output_values, expected_values)

    def test_exceeding_stack_capacity(self):
        # スタック領域を超えた場合のテスト
        t_stack = stack(10)
        with self.assertRaises(MemoryError):
            for i in range(1, 12):
                t_stack.push(i)

    def test_popping_from_empty_stack(self):
        # 取り出すデータが存在しない場合のテスト
        t_stack = stack(10)
        with self.assertRaises(IndexError):
            t_stack.pop()

if __name__ == "__main__":
    unittest.main()