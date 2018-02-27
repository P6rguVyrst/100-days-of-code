from codeclub.second.alpha import count_mixified

def test_count_mixified():
    paragraph = 'Teretulemast maailma lõppu'
    num_words = count_mixified(paragraph)
    print(num_words)
