from codeclub.first.charlie import solve

def test_solve():
    eq = {}
    eq['0'] = '2x+3y=6'
    eq['1'] = '4x+9y=15'

    solve(*eq.values())



