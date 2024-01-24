def is_isogram(string):
    string = string.lower()
    chars = [] 
    for ch in string:
        if ch.isalpha() == True:
            chars.append(ch)
    
    set_chars = set(chars)
    return len(chars) == len(set_chars)


# ============================
# tests
# ============================
print(is_isogram("lumberjacks"))       # True
print(is_isogram("background"))        # True
print(is_isogram("downstream"))        # True
print(is_isogram("six-year-old"))      # True
print(is_isogram("isograms"))          # False