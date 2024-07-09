import unittest

class RingBuffer():
    def __init__(self, size):
        self.memory = [None] * size # 保持できる要素数
        self.head = None # 先頭データの位置
        self.tail = 0 # 挿入するデータの位置

    def enqueue(self, value):
        if self.head == self.tail: # データが満杯のとき
            self._raise_memory_error()

        if self.head is None: # データが空のとき
            self.head = self.tail # 挿入するデータを先頭にする

        self.memory[self.tail] = value # データを挿入する

        self.tail = self._loop_index(self.tail + 1) # tailを一つ後ろに移動する

        return None

    def dequeue(self):
        if self.head is None: # データが空のとき
            self._raise_index_error()

        value = self.memory[self.head]
        self.head = self._loop_index(self.head + 1) # headを一つ後ろに移動する

        if self.head == self.tail: # データが空になったとき
            self.head = None

        return value

    def _loop_index(self, index):
        return index % len(self.memory) 

    def _raise_index_error(self):
        raise IndexError('取り出すデータが存在しません')

    def _raise_memory_error(self):
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