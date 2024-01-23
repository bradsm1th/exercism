def response(hey_bob):
    responses = {
        'question': "Sure.",
        'YELL': 'Whoa, chill out!',
        'yelled question': "Calm down, I know what I'm doing!",
        'silence': "Fine. Be that way!",
        'default': "Whatever."
    }
    
    if hey_bob.isspace() or bool(hey_bob) == False:
        return responses['silence']
    elif hey_bob.rstrip().endswith("?") and hey_bob.isupper():
        return responses['yelled question']
    elif hey_bob.rstrip().endswith("?"):
        return responses['question']
    elif hey_bob.isupper():
        return responses['YELL']
    else:
        return responses['default']    

        
print(response("Okay if like my  spacebar  quite a bit?   ")) # "Sure."