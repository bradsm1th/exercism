def response(hey_bob):
    responses = {
        'question': "Sure.",
        'YELL': 'Whoa, chill out!',
        'yelled question': "Calm down, I know what I'm doing!",
        'silence': "Fine. Be that way!",
        'default': "Whatever."
    }
    
    text = hey_bob.strip()
    
    if text.isspace() or bool(text) == False:
        return responses['silence']
    elif text.endswith("?") and text.isupper():
        return responses['yelled question']
    elif text.endswith("?"):
        return responses['question']
    elif text.isupper():
        return responses['YELL']
    else:
        return responses['default']    

        
print(response("Okay if like my  spacebar  quite a bit?   ")) # "Sure."