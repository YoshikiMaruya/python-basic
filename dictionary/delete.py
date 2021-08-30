# del文を使用し要素を削除

dict = {0:"Movie", 1:"Foods", 2:"Reading"}

del dict[2]
print(dict)

otherdict = {2:"Sports", 3:"Music"}
dict.update(otherdict)
print(dict)

# 指定したキーの要素を削除する。
value = dict.pop(3)
print(value)
print(dict)

# 最後に追加された要素を取得したうえで削除する。
value2 = dict.popitem()
print(value2)
print(dict)

# listとtaple同様キーの要素が含まれているかはinで判定可能
