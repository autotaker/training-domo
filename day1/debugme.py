def convert_fizzbuzz(n: int) -> str:
    s = str(n)
    if n % 3 == 0 and n % 5 == 0:
        s = "FizzBuzz"
    if n % 3 == 0:
        s = "Fizz"
    if n % 5 == 0:
        s = "Buzz"
    return s


def fizzbuzz():
    """
    1から100までの整数nに対して
    * nが3の倍数かつ5の倍数の時はFizzBuzz
    * nが3の倍数の時はFizz
    * nが5の倍数の時はBuzz
    * それ以外の時はn

    を標準出力に一行ずつプリントする
    """
    for i in range(100):
        print(convert_fizzbuzz(i))


if __name__ == "__main__":
    fizzbuzz()
