# 別のタプルと結合して新しいタプルを作成する。
tuple1 = ("A", "B", "C")
tuple2 = ("D", "F")
combine_tuple = tuple1 + tuple2
print(combine_tuple)

# 指定した値と同じ値を持つ要素が含まれているかを確認する。
if "B" in combine_tuple:
  print("OK")
else:
  print("No")

# 指定した値と同じ要素がタプルに何個含まれているか取得
print(tuple1.count("A"))
print(tuple2.count("A"))

# 基本的にlistと様相は同様だが特性が異なるので意識すべきはそこ！
