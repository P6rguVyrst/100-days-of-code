from src import encoding as exc

def test_encode():

    test_data = {
        'A': '1A',
        'AABBBCCCC': '2A3B4C',
        'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW': '12W1B12W3B24W1B14W',

    }
    print('\n')
    for k, v in test_data.items():
        print(k, v)
        assert exc.encode(k) == v
        assert exc.decode(v) == k




