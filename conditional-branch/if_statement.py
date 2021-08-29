i = list(map(int, input().split())) #i_1 i_2を取得し、iに値を入れる

if i[0] > i[1]:
  print(str(i[0]) + " > " + str(i[1]))
elif i[0] == i[1]:
  print(str(i[0]) + " = " + str(i[1]))
else:
  print(str(i[0]) + " < " + str(i[1]))
