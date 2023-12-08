# 2分探索法
def binary_search(values, target):
    lo = 0
    hi = len(values) - 1

    while lo <= hi:
        mid = int((lo + hi) / 2)
        if values[mid] == target:
            return mid
        elif values[mid] > target:
            hi = mid -1 
        elif values[mid] < target:
            lo = mid + 1
    return None

def test_binary_search():
    values = [1, 4, 7, 9, 10, 16]
    print(binary_search(values, 1) == 0)
    print(binary_search(values, 9) == 3)
    print(binary_search(values, 16) == 5)
    print(binary_search(values, 8) == None)

if __name__ == '__main__':
    test_binary_search()