# ３で割り切れたら `Fizz`
# ５で割り切れたら `Buzz`
# １５で割り切れたら `FizzBuzz`
# と出力する。

def fizz_buzz():
  for i in range(31):
    print(str(i) + ":", end="")
    if i % 15 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print("☻")

def main():

  fizz_buzz()

if __name__ == "__main__":
  main()
