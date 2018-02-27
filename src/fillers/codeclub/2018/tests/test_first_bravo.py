from codeclub.first.bravo import add

def test_add():
    test_data = [
        (1,2,3),
        (2,3,5),
        (3,4,7),
        (4,5,9),
        (5,6,11),
    ]
    for i, item in enumerate(test_data):
        assert add(test_data[i][0], test_data[i][1]) == test_data[i][2]
