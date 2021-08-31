set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {1, 3, 5, 7}

# 集合の和を求める。(unionメソッド)
set4 = set1.union(set3)
print(set4)
# 集合の和を求める。(|演算子)
set4 = set1 | set2 | set3
print(set4)
