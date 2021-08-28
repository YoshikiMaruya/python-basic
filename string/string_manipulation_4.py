# スライス機能を使うと開始位置から終了位置までの範囲の部分文字列を取得できる。
string1 = "Hello"
print(string1[1:3])
print(string1[2:4])

# 開始位置のみの指定
string2 = "yoshimaru"
print(string2[4:])

# 終了位置のみの指定
print(string2[:4])

# 開始インデックスと終了インデックスを共に省略した場合
print(string2[:])

# スライスで何文字ごとに抜き出すかを指定する。
print(string2[1::2])
