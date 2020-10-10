import math


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


def profit(product):
    return product["inventory"] * product["sell_price"] - product["inventory"] * product["cost_price"]


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_primes(numberlist):
    sum = 0
    for number in numberlist:
        if is_prime(number):
            sum += number
    return sum


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
