from codeclub.first.delta import parse_name
import re
def test_parse_name():
    sentences = {
        'I was having fun at CodeClub the other night!': 'CodeClub',
        'My name is Taavi': 'Taavi',
        'Hey look, is this Elon Musk over there?': 'Elon Musk',
        'You know, Taavi told me that you can always ask Alan if you have any questions related to Python': 'Taavi Alan Python',
        'Ärtu Ööbik Toomas, Ülle, Mõts': 'Toomas',
    }
    for test, expected in sentences.items():
        result = parse_name(test)
        assert result == expected
    test = 'Ärtu Ööbik Toomas'
    for i in test:
        print(i, i.encode('ascii', errors='ignore').isalpha())
