def steps(number):
    count = 0
    next_number = number
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
        
    
    while next_number != 1:
        if next_number % 2 == 0:
            count += 1
            next_number = next_number / 2
        else:
            count += 1
            next_number = next_number * 3 + 1
    
    return count
    # return f"Got to 1! It took {count} steps…"

# print(steps(1))         # 0
# print(steps(16))        # 4
# print(steps(12))        # 9
# print(steps(1000000))   # 152
print(steps(0))         # err
print(steps(-15))       # err