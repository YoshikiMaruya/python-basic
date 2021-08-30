# 多次元リストから要素を取り出す。
stafflist = [["Yamada", 25], ["Suzuki", 29], ["Tanaka", 33]]
print(stafflist[0])

for i in range(len(stafflist)):
  for j in range(len(stafflist[0])):
    print(stafflist[i][j])

# リスト内包表記
list = [i for i in range(1, 6)]
print(list)

# 条件を加えたリスト内包表記
list2 = [i for i in range(30) if i % 3 == 0]
print(list2)

# リスト内包表記による多重ループの記述方法
list3 = [i * 5 + j for i in range(10) for j in range(3)]
print(list3)

# リスト内包表記を使った2次元配列
list4 = [[i + j for j in range(3)] for i in range(2)]
print(list4)
