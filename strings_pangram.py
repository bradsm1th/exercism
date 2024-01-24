def is_pangram(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = ''
    for each in sentence.lower():
        if each.isalpha():
            new_alphabet += each

    return sorted(alphabet) == sorted(set(new_alphabet))

print(is_pangram('The quick brown fox jumps over the lazy dog.'))
# True