# 指定した文字列が何回含まれるのかを取得するcountメソッド
from typing import DefaultDict


print("Good School".count("oo"))
print("Good School".count("oo", 3, 10))

# 指定した区切り文字で分割しリストとして取得するsplitメソッド
print("My First Album".split())

print("a,b,c,d".split(","))
print("a,b,c,d".split(",", 2))

# 指定した文字を文字列の先頭および末尾から取り除くstripメソッド
# 値を指定しないと空白を取り除く
print("  Hello ".strip())
print("...hello...".strip("."))

# 指定した文字列を別の文字列に置換するreplaceメソッド
print("copyright 2018".replace("2018", "2019"))
