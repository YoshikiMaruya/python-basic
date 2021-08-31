# ユーザー定義関数利用意義

# プログラム中で何度も利用するコードを１つにまとめる
# まとまったコードに名前をつけて、コードの意図をわかりやすくする。
# プログラムを関数の形でほかのプログラムから利用できるようにする。

# 簡単な関数を定義してみる
def hello(whom):
  message = "Hello " + str(whom)
  print(message)

def main():
  hello("World")
if __name__ == "__main__":
  main()
