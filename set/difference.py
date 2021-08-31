set1 = set(range(7))
set2 = {x for x in range(4, 9, 2)}
set3 = {x for x in range(0, 4, 2)}

# 集合の差を求める。(differenceメソッド)
set4 = set1.difference(set2)
print(set4)

# 集合の差を求める。(-演算子)
set4 = set1 - set2 - set3
print(set4)
