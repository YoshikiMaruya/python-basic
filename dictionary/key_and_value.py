# 辞書に含まれるすべてのキーを取得する。
dict = {"L":"Lemon", "O":"Orange", "G":"Grapes"}
print(dict.keys())

for mykey in dict.keys():
  print(mykey)

# リストを取得することも
key_list = list(dict.keys())
print(key_list)


# 辞書に含まれるすべての値を取得する。
print(dict.values())
for myvalue in dict.values():
  print(myvalue)

# リスト化も
value_list = list(dict.values())
print(value_list)

# itemsメソッドを使用すればすべてのキーと値を取得できる。
for mykey, myvalue in dict.items():
  print(mykey + " : " + myvalue)
