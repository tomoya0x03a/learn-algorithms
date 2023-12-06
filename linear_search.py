# 線形探索法
def linear_search(values, target):
    for i, value in enumerate(values):
        if value == target:
            return i
    # 見つからない場合はNoneを返す。

def test_linear_search():
    values = [7,4,2,8,10,9,1,5,3,6]
    print(linear_search(values, 8) == 3)
    print(linear_search(values, 11) == None)

if __name__ == '__main__':
    test_linear_search()