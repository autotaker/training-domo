
def fizzbuzz():
    for i in range(100):
        if i % 3 == 0:
            print('Fizz')
        if i % 5 == 0:
            print('Buzz')
        print(i)

if __name__ == '__main__':
    fizzbuzz()
