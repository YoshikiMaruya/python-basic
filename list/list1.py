# listを作成する
colorlist = ["Red", "Blue", "Green"]
print(colorlist[0])
print(colorlist[-2])

# 変数に代入された値を要素として指定する
x = 1
y = 10

numlist = [x, y]
print(numlist)

# リストの最後の要素のインデックスを調べる
print(colorlist[len(colorlist) - 1])

# リストでスライス機能を使用する
numlist = ["1", "2", "23", "31", "78"]

print(numlist[0:2])
print(numlist[0:])

# len関数を使用し、リストの長さを取得する。
print(len(numlist))
