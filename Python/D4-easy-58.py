

def last_words(str):
    words = str.split()
    result = 0
    if len(words) > 1:
        result = len(words[-1])
    elif len(words) == 0:
        result = 0
    return result


