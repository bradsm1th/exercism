def leap_year(year):
    if year % 2: 
        return False
    elif year % 100 == 0 and year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100: 
        return True
    else:
        return False

"""
A leap year (in the Gregorian calendar) occurs:
    - In every year that is evenly divisible by 4.
    - Unless the year is evenly divisible by 100, in which case it's only a leap year if the year is also evenly divisible by 400.
    """

print(leap_year(1997))      # False
print(leap_year(1900))      # False
print(leap_year(2000))      # True
print(leap_year(1996))      # True
print(leap_year(1970))      # False
print(leap_year(2100))      # False