def is_triangle(sides):
    a, b, c = sides
    if 0 in sides:
        return False
    else:
        return a + b >= c and b + c >= a and a + c >= b


def equilateral(sides):
    a, b, c = sides
    if not is_triangle(sides):
        return False
    return True if a == b == c else False


def isosceles(sides):
    if not is_triangle(sides):
        return False
    for num in sides:
        if sides.count(num) > 1:
            return True
    else:
        return False


# print(isosceles([4, 4, 4]))         # True
# print(isosceles([2, 3, 4]))         # False
# print(isosceles([3, 4, 4]))         # True


def scalene(sides):
    a, b, c = sides
    if not is_triangle(sides):
        return False 
    return True if a != b and b != c and c != a else False

# print(scalene([4, 4, 4]))           # False