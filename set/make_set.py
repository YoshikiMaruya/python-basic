# 値を指定して集合を作成する。
# {}を使用する点は辞書型と同様

# set = {"H", "a", "p", "p", "y"}
# print(set)

# 文字列から集合を作成する。
frozenset = frozenset("Hello Python")
print(frozenset)

# リストから集合を作成する。
data_list = [104, 195, 195, 104, 512, 592, 902, 421]
#set()関数を使って、リストを set（集合）に変換します。
data_set = set(data_list)
#確認しましょう。
print(data_set)
