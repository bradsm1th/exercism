def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    new_exchange_rate = exchange_rate + (spread/100 * exchange_rate)

    if new_exchange_rate == 0:
        return int(budget // denomination * denomination)
    else: 
        return int((budget / new_exchange_rate) // denomination * denomination)

    
print(exchangeable_value(127.25, 1.20, 10, 20))      # 80
print(exchangeable_value(127.25, 1.20, 10, 5))       # 95
print(exchangeable_value(100000, 10.61, 10, 1))       # 8568
print(exchangeable_value(425.33, .0009, 30, 700))       # 363300
print(exchangeable_value(1500, .84, 25, 40))       # 1400