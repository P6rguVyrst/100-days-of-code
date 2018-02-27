from codeclub.second.charlie import mazeSolver


def test_mazeSolver():
    result = mazeSolver([
	['*', '*', '*', '*', '*'],
	['*', '.', '.', '.', '*'],
	['*', '.', 'O', '.', '*'],
	['*', 'X', '.', '.', '*'],
	['*', '*', '*', '*', '*'],
    ])
    assert result == 2

