def convert(number):
    result = ''
    if number % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'
    if number % 3 and number % 5 and number % 7:
        result = str(number)
    return result


print(convert(28))  # "Plong"
print(convert(30))  # "PlingPlong"
print(convert(34))  # "34"