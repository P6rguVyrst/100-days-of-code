parse_name = lambda sentence: ' '.join([_ for _ in sentence.split(' ') if _.encode('ascii', errors='ignore').isalpha() and ( _[0].isupper())][1:])
