def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """

    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = []
    for each in range(number - 1, 0, -1):
        if number % each == 0:
            factors.append(each)

    aliquot = sum(factors)

    if number == aliquot:
        return 'perfect'
    if number < aliquot:
        return 'abundant'
    else:
        return 'deficient'



print(classify(6))       # True
print(classify(28))      # True
