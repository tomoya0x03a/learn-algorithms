import unittest


class BinaryTree():
    def __init__(self, nodes=None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = [
                [1, 2, 10],
                [3, 4, 5],
                [5, None, 12],
                [None, None, 2],
                [6, 7, 8],
                [None, None, 11],
                [None, None, 6],
                [None, None, 9],
            ]

    def traverse(self):
        current = 0
        stack = []
        result = []

        def recursive(current):
            next = None

            if self.nodes[current][0]: # 左のポインタが有れば
                # currentをスタックに格納する
                stack.append(current)

                # nextを左のポインタにする
                next = self.nodes[current][0]
            else: # 左のポインタが無ければ
                # currentの値を出力する
                result.append(self.nodes[current][2])
                print(self.nodes[current][2])

                def recursive_stack():
                    next = None

                    if len(stack) > 0: # スタックにデータが有れば

                        # スタックを一つ取り出す
                        s = stack.pop()
                        result.append(self.nodes[s][2])
                        print(self.nodes[s][2])
                
                        if self.nodes[s][1]: # 取り出したスタックに右のポインタが有れば
                            # nextを取り出したスタックの右のポインタにする
                            next = self.nodes[s][1]
                        else:
                            recursive_stack()

                    return next

                # スタックの値を出力する
                next = recursive_stack()

            if next:
                recursive(next)

            return result

        return recursive(current)


class TestBinaryTree(unittest.TestCase):
    def setUp(self):
        # テスト用のデータセット
        self.nodes = [
                [1, 2, 10],
                [3, 4, 5],
                [5, None, 12],
                [None, None, 2],
                [6, 7, 8],
                [None, None, 11],
                [None, None, 6],
                [None, None, 9],
            ]

    def test_traverse(self):
        expected_values = [2, 5, 6, 8, 9, 10, 11, 12]

        binary_tree = BinaryTree(self.nodes)
        self.assertEqual(binary_tree.traverse(), expected_values)


if __name__ == "__main__":
    unittest.main()