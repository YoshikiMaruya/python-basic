# 指定した値と同じ値を持つ要素が含まれているか確認する。

list = ["A", "B", "C", "D", "F"]
print("B" in list)

# 指定した値を同じ要素がリストに何個含まれいるか取得する。
print(list.count("A"))

# 指定した値を同じ値をもつ要素のインデックスを取得する。
# 複数ある場合は最初の値
print(list.index("A"))

# 要素を並び替える
# sort()メソッドも存在している。
numlist = [7, 3, 2, 5]
print(numlist)
print(sorted(numlist))

# 降順にしたい場合
print(sorted(numlist, reverse=True))
