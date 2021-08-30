# リストに要素を挿入する。
list = ["A", "B", "C"]

list.insert(1, "S")
print(list)

# スライス機能を使ってリストに挿入
addlist = ["D", "F"]

list[len(list):len(list)]  = addlist
print(list)


# del文を使って要素を削除
del list[1]
print(list)

# スライス機能を使用し、削除する。
del list[3:]
print(list)

# インデックスで指定した要素を削除する。
# 引数を指定しなかった場合は最後
list.pop()
print(list)

# 指定した値と同じ値を持つ要素を削除する。
colorlist = ["Red", "Green", "Blue", "Orange"]
colorlist.remove("Red")
print(colorlist)

# リストからすべての要素を削除する。
colorlist.clear()
print(colorlist)
