COLORS = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def value(colors):

    color1, color2 = colors[0], colors[1]
    
    color1_index = str(COLORS.index(color1))
    color2_index = str(COLORS.index(color2))
    
    joined = ''.join((color1_index, color2_index))
    return int(joined)



# tests
print(value(['brown', 'green']))              # 15
print(value(['brown', 'green', 'violet']))    # 15
print(value(['brown', 'black']))              # 10