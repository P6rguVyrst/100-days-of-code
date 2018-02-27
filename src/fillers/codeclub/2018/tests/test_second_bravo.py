from codeclub.second.bravo import coolest_word

def test_coolest_word():
    assert coolest_word(
        ['hello', 'asd', 'decomposition']) == 'decomposition'
    assert coolest_word(
        ['hello', 'apple']) == 'hello'
    assert coolest_word([]) == None
    assert coolest_word(
        ['expectation', 'discomfort',
         'half', 'decomposition']
    ) == 'decomposition'


