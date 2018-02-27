#DONE
def coolest_word(words):
    return None if not words else max(words, key=lambda x: len(set(x)))
