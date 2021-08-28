# joinメソッド
# リストやタプルなどイテラブルオブジェクトに要素として格納されている
# 複数の文字列を指定した区切り文字で連結した新しい文字列を返す。
# リストに文字列以外を含んでいるとタイプエラー

print("".join(["Apple", "Orange", "Lemon"]))

print(",".join(["Apple", "Orange", "Lemon"]))

# すべての文字を小文字に変換するlowerメソッド
print("Hello".lower())
print("HELLO".lower())

# 上記の逆のupperメソッドが存在する。
print("hello".upper())

# 最初の文字を大文字にして他は小文字に変換するcapitalizeメソッド
print("hello python".capitalize())

# 文字列に含まれる単語ごとに最初の文字を大文字に他は小文字に変換するtitleメソッド
print("hello python".title())

# 大文字を小文字に、小文字を大文字に変換するswapcaseメソッド
print("Hello".swapcase())
