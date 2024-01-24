def rotate(text, key):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    upper_letters = [l.upper() for l in letters]
    # for a, A in zip(letters, upper_letters):
        # print(f"{a} / {A}")
    
    # for i, val in enumerate(letters):
        # print(f"{i}: {val}")
        
    # print(key)
    
    c = ''
    
    for i, val in enumerate(text):
        if val.isalpha() == False:
            c += val
        if val in letters:
            c += letters[(letters.index(text[i]) + key) % 26]
        # print(f"{i}: {val}")
        if val in upper_letters:
            c += upper_letters[(upper_letters.index(text[i]) + key) % 26]
            
        # print(f"{i + key}: {letters[(i + key) % 26]}")
        
    return c

# print(rotate('abcdefg', 13))       # 'nopqrst'
# print(rotate('m', 13))             # 'z'
print(rotate('O M G', 5))             # 'T R L