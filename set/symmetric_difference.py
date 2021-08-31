set1 = set(range(4))
set2 = set(range(2, 6))
set3 = set(range(-2, 2))

# 対称差とは和集合-積集合のこと
# 対称差を求める。(symmetric_differenceメソッド)
set4 = set1.symmetric_difference(set2)
print(set4)

# 対称差を求める。(^演算子)
set4 = set1 ^ set3
print(set4)

