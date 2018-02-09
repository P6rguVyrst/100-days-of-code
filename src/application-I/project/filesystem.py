from os import walk

class FSDiscovery(object):

    def __init__(self):
        pass

    def discover_rawdata(self, filetypes, home):
        payload = {'data': []}
        for (dirpath, dirnames, filenames) in walk(home):
            hit = [f for f in filenames if f.endswith(tuple(filetypes))]
            if hit:
                payload['data'].append({'folder': {'files': hit, 'path': dirpath}})
        return payload

    def filter_series(self, disco):
        d = Definitions()
        series = []
        for item in disco['data']:
            files = item['folder']['files']
            for name in files:
                if d.series(name):
                    series.append(name)
        return series
