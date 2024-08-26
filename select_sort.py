import unittest

class SelectSort():
    def __init__(self, data: list[int]) -> None:
        self.data = data[:]

    def sort(self) -> list[int]:
        length = len(self.data)

        for i in range(0, length -1):
            min = i # 最小値のindex
            
            for j in range(i + 1, length):
                if self.data[min] > self.data[j]: # 小さな値が見つかった時
                    min = j

            # 値を入れ替える
            tmp = self.data[min]
            self.data[min] = self.data[i]
            self.data[i] = tmp

        return self.data[:]


class TestSelectSort(unittest.TestCase):
  
    def test_sort(self):
        input_list = [8, 5, 2, 1, 7]
        expected_list = [1, 2, 5, 7, 8]
    
        select_sort = SelectSort(input_list)
        self.assertEqual(select_sort.sort(), expected_list)


if __name__ == "__main__":
    unittest.main()        


