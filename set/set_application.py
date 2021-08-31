# 集合に要素を追加する。
data_list = [104, 195, 195, 104, 512, 592, 902, 421]
data_set = set(data_list)

data_set.add(514)
print(data_set)


# 集合から要素を削除する。
data_set.remove(104)
print(data_set)

# discardメソッドというものもある。
# これは集合に指定されたitemが存在しなくてもエラーを発生させないというもの

# 要素数と最大要素を求めるlenメソッドとmaxメソッド
print(len(data_set))
print(max(data_set))


