import re


class Media(object):

    def unique_titles(self, videos, datatype):
        options = {
            'series': self.series,
            'movies': self.movies,
        }
        data = {'titles': []}
        for title in videos['data']:
            for f in title.get('folder', {}).get('files'):
                f = f.replace('.', ' ')
                f = f.replace('-', ' ')
                f = f.replace(' ', ' ')
                #Handle errors
                m = options[datatype](f)
                if m:
                    data['titles'].append(m)
        return data

    def movies(self, filename):
        pattern = '(.*?)( \d{4}?)'
        #pattern = '(.*?)\d{4}|$'
        movies = re.compile(pattern)
        year_match = re.search(movies, filename.upper())
        if not self.series(filename):
            if year_match:
                return year_match[0]
                #match = year_match[0]
                #if match:
                #    return match
                    #x = str(year_match[0]).split(' ')
                    #data = dict(
                    #    title = ' '.join(x[:-1]),
                    #    year = int(x[-1:][0]),
                    #)
                    #pp(data)
                    #return data


    def series(self, filename):
        pattern = '(.*)S\d{2}E\d{2}.*'
        series = re.compile(pattern)
        episode_match = re.findall(series, filename.upper())
        if episode_match:
            return episode_match[0].rstrip()


