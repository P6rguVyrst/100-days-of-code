
def test_tmpdir(tmpdir):
    a_file = tmpdir.join('alpha.txt')
    a_sub_dir = tmpdir.mkdir('any')
    another_file = a_sub_dir.join('bravo.txt')
    a_file.write('Very good content!')
    another_file.write('Something else')

    assert a_file.read() == 'Very good content!'
    assert another_file.read() == 'Something else'

def test_tmpdir_factory(tmpdir_factory):
    a_dir = tmpdir_factory.mktemp('mydir')
    base_temp = tmpdir_factory.getbasetemp()
    print('base: ', base_temp)

    a_file = a_dir.join('alpha.txt')
    a_sub_dir = a_dir.mkdir('any')
    another_file = a_sub_dir.join('bravo.txt')

    a_file.write('Hello world!')
    another_file.write('Working on stuff.')

    assert a_file.read() == 'Hello world!'
    assert another_file.read() == 'Working on stuff.'

