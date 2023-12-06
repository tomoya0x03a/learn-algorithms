# 2分探索法
def binary_search(values, target):
    None

def test_binary_search():
    values = [1, 4, 7, 9, 10, 16]
    print(binary_search(values, 0) == 1)
    print(binary_search(values, 3) == 9)
    print(binary_search(values, 5) == 16)
    print(binary_search(values, 8) == None)

if __name__ == '__main__':
    test_binary_search()