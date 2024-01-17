import psutil
import os


# 指定された長さのリストを生成する
def generate_list(length):
    return list(range(length))


# 指定された長さのジェネレータを生成する
def generate_generator(length):
    for num in range(length):
        yield num


# メモリ使用量を計算する
def calculate_memory_usage(func, length):
    process = psutil.Process(os.getpid())
    mem_before = process.memory_info().rss

    result = func(length)
    for value in result:
        pass

    mem_after = process.memory_info().rss
    return mem_after - mem_before


# リストとジェネレータのメモリ使用量を比較する
def compare_list_memory_with_generator_memory():
    length = 1_000_000
    list_memory_usage = calculate_memory_usage(generate_list, length)
    generator_memory_usage = calculate_memory_usage(generate_generator, length)

    print(f"List memory usage: {list_memory_usage / 1024} KB")
    print(f"Generator memory usage: {generator_memory_usage / 1024} KB")


# メイン関数としてメモリ使用量の比較を実行する
if __name__ == "__main__":
    compare_list_memory_with_generator_memory()
