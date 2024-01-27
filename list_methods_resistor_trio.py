COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def convert_colors_to_index(colors):
    color_indexes = []
    for color in colors:
        color_indexes.append(COLORS.index(color))
    return color_indexes

def label(colors):
    
    # get colors
    color1, color2, rating = colors[:3]
    
    # convert colors to their index
    index_1, index_2, rating_index = convert_colors_to_index((color1, color2, rating))
    # print(index_1, index_2, suffix)

    # construct numerical part (first two colors)
    prefix = "".join((str(index_1), str(index_2)))
    # print(prefix)
    
    # construct suffix (last color)
    suffix = "0" * rating_index
    
    # start building result string
    result = int((f"{prefix}{suffix}"))
    # print(result)
    
    # count zeroes, do "ohms"
    if result // (10 ** 9) > 0:
        pass # 'giga ohms
        return f"{result // 10 ** 9} gigaohms"
    if result // (10 ** 6) > 0:
        pass # 'mega ohms
        return f"{result // 10 ** 6} megaohms"
    if result // (10 ** 3) > 0:
        pass # 'kilo ohms
        return f"{result // 10 ** 3} kiloohms"
    return f"{result} ohms"
    
    # zeros = result.count("0")
    # if zeros > 11:
    #     return "that's too big for me"
    # if zeros > 8:
    #     return f"{result[:-zeros]} gigaohms"
    # if zeros > 5:
    #     return f"{result[:-zeros]} megaohms"
    # if zeros > 2:
    #     return f"{result[:zeros - 1]} kiloohms"
    # return f"{result} ohms"
    

print(label(["orange", "orange", "black"]))         # "33 ohms"
print(label(["orange", "orange", "red"]))           # "3300 ohms"
print(label(["orange", "orange", "orange"]))        # "33 kiloohms"
print(label(["orange", "orange", "white"]))         # "33 gigaohms"
print(label(["red", "black", "red"]))               # "2 kiloohms"
print(label(["yellow", "violet", "yellow"]))               # "470 kiloohms"