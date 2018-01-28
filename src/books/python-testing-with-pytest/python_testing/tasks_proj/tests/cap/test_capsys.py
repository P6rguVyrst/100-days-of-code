import sys


def greeting(name):
    print('Hey {}!'.format(name))

def test_greeting(capsys):
    greeting('Earthling')
    out, err = capsys.readouterr()
    assert out == 'Hey Earthling!\n'
    assert err == ''

    greeting('Brian')
    greeting('Nerd')

    out, err = capsys.readouterr()
    assert out == 'Hey Brian!\nHey Nerd!\n'
    assert err == ''

def yikes(problem):
    print('YIKES! {}'.format(problem), file=sys.stderr)

def test_yikes(capsys):
    yikes('Out of coffee!')
    out, err = capsys.readouterr()
    assert out == ''
    assert 'Out of coffee!' in err

def test_capsys_disabled(capsys):
    with capsys.disabled():
        print('\nAlways print this.')
    print('Normal print, usually captured.')




