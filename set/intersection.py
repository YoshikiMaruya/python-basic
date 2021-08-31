set1 = set(range(1, 6))
set2 = set(range(2, 7, 2))
set3 = {x for x in range(6) if x % 2}

# 積は集合の共通部分
# 集合の積を求める。(intersectionメソッド)
set4 = set1.intersection(set2)
print(set4)

# 集合の積を求める。(&演算子)
set4 = set1 & set3
print(set4)
