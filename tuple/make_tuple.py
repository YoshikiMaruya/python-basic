# タプルを作成する。
# タプルはリストとは違い要素の値をあとから変更できない。
# タプルの使いどころ
# １：変更を許可しない変数を定義する。
# ２：dictのキーに使用する。
# ３：パフォーマンスの改善に使用する。

value = 9.8
gravitational_acceleration = "G"
tuple = (gravitational_acceleration, value)
print(tuple)

# 要素取り出し

KEY = (2, 5, 1, 2, 0, 5)
print(KEY[0])
print(len(KEY) - 1)
