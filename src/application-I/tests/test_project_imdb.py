from project.imdb import Paths

class TestPaths(object):

    def test_make_search_string(self):
        tst = Paths()
        test_titles = [
            'THE SPECTACULAR NOW 2013',
            'THE DARK TOWER 2017',
            'LA LA LAND 2016',
            'RICK AND MORTY ',
            'SOUTH PARK',
            'BOJACK HORSEMAN',
        ]
        for title in test_titles:
            assert tst.make_search_string(title) == title.replace(' ', '+')

    def test_make_name_search_uri(self):
        pass

    def test_search_title(self):
        pass

    """
    def tst(self):
        test_titles = [
            'THE SPECTACULAR NOW 2013',
            #'THE DARK TOWER 2017',
            #'LA LA LAND 2016',
            'RICK AND MORTY',
            #'SOUTH PARK',
            #'BOJACK HORSEMAN',
        ]
        for title in test_titles:
            title_str = self.make_search_string(title)
            uri = self.make_name_search_uri(title_str.lower())
            result = self.search_title(uri)
            pp(result)
            #assert self.make_search_string(title) == title.replace(' ', '+')
    """


