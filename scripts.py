def calc_age(age):
    return 365 * age


def fizzbuzz(number):
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    if number % 5 == 0 and number % 3 == 0:
        return "FizzBuzz"
    return str(number)


print(fizzbuzz(21))
