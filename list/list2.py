# 特定の要素を入れ替える。
colorlist = ["Red", "Green", "Blue", "Orange"]

print(colorlist)
colorlist[0] = "White"

print(colorlist)

# スライス機能を使って複数の要素をまとめて入れ替える。

colorlist[1:4] = ["Black", "Yellow", "Gray"]
print(colorlist)

# リストに要素を追加する。
colorlist.append("Red")
print(colorlist)

# リストでスライス機能を使う際開始インデックスと終了インデックスを
# ともにリストの最後の要素の次の位置を指定することで要素をリストの最後に追加できる。

colorlist[len(colorlist) : len(colorlist)] = ["Green", "Blue"]
print(colorlist)

# extendメソッドとappendメソッドの違い
list = ["A", "B", "C", "D"]
list.extend(["E", "F"])
list.append(["G", "H"])
print(list)

# リストの結合
print(colorlist + list)
