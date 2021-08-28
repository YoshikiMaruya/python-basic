# islower メソッドは文字列中の大文字と小文字の区別のある文字が
# 1 文字以上あり、そのすべてが小文字の場合に真を返します

print("apple".islower())
print("Hello".islower())

# 上記とは逆のisupperメソッドがある。

print("APPLE".isupper())
print("Hello".isupper())

# 文字列に含まれる単語毎に最初の文字が大文字で他は小文字かどうかを判定するistitleメソッド
print("Music Video".istitle())
print("THE Movie".istitle())

# すべての文字が10進数の文字かどうかを判定するisdecimalメソッド
print("77777".isdecimal())
print("4h5j6".isdecimal())

# すべての文字が数字の文字かどうかを判定するisdigitメソッド
print("77777".isdigit())
print("-8765".isdigit())

# 指定した文字列が最初に現れるインデックスを取得するfindメソッド
print("hello".find("ll"))
print("orange".find("aa"))
# ３番目から１０番目までの間で探す
print("Good School".find("oo", 3, 10))
