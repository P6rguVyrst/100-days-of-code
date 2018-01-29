from earth.animalia.chordata.mammalia.primates.haplorhini.simiiformes.hominidae.homo import sapiens as homo_sapiens


class TestHuman(object):

    human = homo_sapiens.Human()

    def test_human_nature(self):
        assert self.human.nature.upper() == 'GOOD'

    def test_humanity(self):
        assert self.human.humanity.upper() == 'INTACT'



class TestMan(object):
    pass


class TestWoman(object):
    pass


def test_pasing():
    pass



