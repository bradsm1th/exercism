def square(number):
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)
    

def total():
    grains = 0
    for num in range(1, 65):
        grains += square(num)
    return grains


# print(square(1))        # 1
# print(square(2))        # 2
# print(total())