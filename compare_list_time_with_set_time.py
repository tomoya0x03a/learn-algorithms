from timeit import timeit


def search_value_in_collection(collection, value):
    """コレクション内で特定の値を検索します。

    Args:
        collection: 検索対象のコレクション（リストやセットなど）
        value: 検索する値

    Returns: コレクション内に値が存在する場合はTrue、存在しない場合はFalse
    """

    if value in collection:
        return True
    else:
        return False


def compare_list_time_with_set_time():
    """リストと集合の検索時間を比較します。

    この関数は、大きな数のリストとセットを作成し、特定の値を検索し、
    それぞれの操作にかかった時間を計測し、結果を出力します。
    """
    # 大きな数のリストとセットを作成
    stop = 3_000_000
    test_set = set(range(stop))
    test_list = list(range(stop))

    # 検索する値を定義
    target = 2_545_123

    # セット内での検索時間を計測
    time_set = timeit(
        stmt=lambda: search_value_in_collection(test_set, target),
        number=1,
    )

    # リスト内での検索時間を計測
    time_list = timeit(
        stmt=lambda: search_value_in_collection(test_list, target),
        number=1,
    )

    # 時間を出力
    print(f"セット内での検索時間: {time_set}")
    print(f"リスト内での検索時間: {time_list}")
    print(f"リスト検索時間 / セット検索時間 = {time_list / time_set}")


if __name__ == "__main__":
    compare_list_time_with_set_time()
