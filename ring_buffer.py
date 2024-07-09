import unittest

class RingBuffer:
    """
    リングバッファを実装したクラス。固定サイズのバッファを使用し、データの挿入と取得を循環的に行う。
    """

    def __init__(self, size):
        """
        指定されたサイズのリングバッファを初期化する。
        """
        self.memory = [None] * size  # バッファのサイズを指定し、メモリを初期化
        self.head = 0  # 先頭データの位置を初期化
        self.tail = 0  # 挿入するデータの位置を初期化
        self.is_full = False  # バッファが満杯かどうかを示すフラグ
        self.is_empty = True  # バッファが空かどうかを示すフラグ

    def enqueue(self, value):
        """
        バッファにデータを挿入する。
        """
        if self.is_full:  # バッファが満杯のとき
            self._raise_full_error()  # エラーを発生させる

        self.memory[self.tail] = value  # データを挿入
        self.tail = self._loop_index(self.tail + 1)  # tailを一つ後ろに移動

        self.is_empty = False  # バッファが空ではなくなる

        if self.head == self.tail:  # 挿入後、バッファが満杯になったとき
            self.is_full = True  # バッファが満杯であることを示すフラグを立てる

        return None

    def dequeue(self):
        """
        バッファからデータを取り出す。
        """
        if self.is_empty:  # バッファが空のとき
            self._raise_empty_error()  # エラーを発生させる

        value = self.memory[self.head]  # 先頭のデータを取得
        self.head = self._loop_index(self.head + 1)  # headを一つ後ろに移動

        self.is_full = False  # バッファが満杯ではなくなる

        if self.head == self.tail:  # 取得後、バッファが空になったとき
            self.is_empty = True  # バッファが空であることを示すフラグを立てる

        return value

    def _loop_index(self, index):
        """
        インデックスをバッファサイズで循環させる。

        """
        return index % len(self.memory)

    def _raise_empty_error(self):
        raise IndexError('取り出すデータが存在しません')

    def _raise_full_error(self):
        raise MemoryError('これ以上データを入れられません')

class TestRingBuffer(unittest.TestCase):
    # 挿入したデータを挿入順に取得できるか
    def test_order_of_enqueue_dequeue(self):
        input_values = [i for i in range(5)]
        output_values = []

        ring_buffer = RingBuffer(5)

        for i in input_values:
            ring_buffer.enqueue(i)
        for _ in range(5):
            output_values.append(ring_buffer.dequeue())

        self.assertEqual(input_values, output_values)

    # 初期状態でのデータ取り出し
    def test_initial_state_dequeue(self):
        ring_buffer = RingBuffer(5)

        with self.assertRaises(IndexError):
            ring_buffer.dequeue()

    # 全データ取り出し後のデータ取り出し
    def test_dequeue_from_empty_buffer(self):
        ring_buffer = RingBuffer(5)

        for i in range(5):
            ring_buffer.enqueue(i)
        for _ in range(5):
            ring_buffer.dequeue()

        with self.assertRaises(IndexError):
            ring_buffer.dequeue()        
    
    # 保持できる要素数を超えた挿入
    def test_exceed_capacity_enqueue(self):
        ring_buffer = RingBuffer(5)

        for i in range(5):
            ring_buffer.enqueue(i)

        with self.assertRaises(MemoryError):
            ring_buffer.enqueue(5)             
        
    # データを満杯にした後、1つ取り出し、1つ挿入する
    def test_dequeue_enqueue_from_capacity_buffer(self):
        input_values = [0, 1, 2, 3, 4, 5]
        expected_values = [1, 2, 3, 4, 5]
        output_values = []

        ring_buffer = RingBuffer(5)

        for i in input_values[0: 5]:
            ring_buffer.enqueue(i)
        
        ring_buffer.dequeue()
        ring_buffer.enqueue(input_values[5])

        for i in range(5):
            output_values.append(ring_buffer.dequeue())

        self.assertEqual(expected_values, output_values)

if __name__ == "__main__":
    unittest.main()