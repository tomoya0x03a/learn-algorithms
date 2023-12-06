# 線形探索法のアルゴリズム
def linear_search(values, target):
    for i, value in enumerate(values):
        if value == target:
            return i
    # 見つからない場合はNoneを返す。

values = [7,4,2,8,10,9,1,5,3,6]
print(linear_search(values, 2))
print(linear_search(values, 11))

