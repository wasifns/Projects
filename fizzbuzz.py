for number in range(1,101):
    if number%3==0:
        print("Fizz\n")
    elif number%5==0:
        print("Buzz\n")
    elif number%3==0 and number%5==0:
        print("FizzBuzz\n")
    else:
        print(number)
pi = open("first.py", "r")
print(pi.read())