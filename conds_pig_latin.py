def find_first_vowel(str):
    VOWELS = [*'aeiou']
    CLUSTERS = ['xr', 'yt']
    str = str.lower()
    vowel_index = 0
    
    # 'by', 'my'
    if len(str) == 2 and str[-1] == 'y':
        vowel_index = -1
        return vowel_index
    # '{xx}y
    if str[2] == 'y' and str[0] not in VOWELS and str[1] not in VOWELS:
        vowel_index = str.index('y')
        return vowel_index
        
    for idx in range(len(str)):
        # 'xr', 'yt'
        if str[:2] in CLUSTERS:
            continue
        # regular
        if str[idx] in VOWELS:
            # if 'qu'
            if str[idx] == 'u' and str[idx-1] == 'q':
                continue
            else:
                vowel_index = str.index(str[idx])
            break
    return vowel_index

    
def translate(text):
    text = text.lower()
    result = [] 
    # split in words
    words = text.split(' ')
    # print(words)
    for word in words:  
        find_first_vowel(word)
        # print(find_first_vowel(word))
        result.append(word[find_first_vowel(word):] + word[:find_first_vowel(word)] + 'ay')
    return " ".join(result)
    
  
# ============================
# tests
# ============================
# print(translate('xray'))
# print(translate('chair'))
# print(translate('thrush'))
# print(translate('queen'))
# print(translate('square'))
# print(translate('rhythm'))
# print(translate('my'))
# print(translate('quick fast run'))                      # 'ickquay astfay unray'
    
# assert translate('xray') == 'xrayay', 'nope'            # 'xrayay'
# assert translate('apple') == 'appleay', 'nope'          # 'appleay'
# assert translate('doggo') == 'oggoday', 'nope'          # 'oggoday'
# assert translate('chair') == 'airchay', 'nope'          # 'airchay'
# assert translate('square') == 'aresquay', 'nope'        # 'aresquay'
# assert translate('rhythm') == 'ythmrhay', 'nope'        # 'ythmrhay'
# assert translate('my') == 'ymay', 'nope'                # 'ymay'
# assert translate('queen') == 'eenquay', 'nope'          # 'eenquay'
# assert translate('thrush') == 'ushthray', 'nope'        # 'ushthray'
# assert translate('quick fast run') == 'ickquay astfay unray', 'nope'      # 'ickquay astfay unray'
