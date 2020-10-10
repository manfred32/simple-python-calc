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


print(profit({
    "cost_price": 32.67,
    "sell_price": 45.00,
    "inventory": 1200
}))
