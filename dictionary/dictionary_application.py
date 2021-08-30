# getメソッドを使用し値を取得

dictionary = {0:"Orange", 1:"Lemon", 2:"Peach"}
print(dictionary.get(1))
print(dictionary.get(5))

# 辞書の要素の値を変更する。
dict = {0:"Movie", 1:"Foods", 2:"Reading"}
dict[0] = "Sports"
print(dict)


# 辞書に新しい要素を追加する。
dict[3] = "Movie"
print(dict)

# ほかの辞書のデータを使って辞書の要素の値を更新したり新しい要素を追加する。
otherdict = {1:"Programming", 4:"Music"}
dict.update(otherdict)
print(dict)

# del文を使用し要素を削除
del dict[4]
print(dict)
