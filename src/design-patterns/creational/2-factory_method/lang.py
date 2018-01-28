
class GreekGetter(object):

    def __init__(self):
        self.trans = dict(
            dog='asd',
            cat='dsa'
        )

    def get(self, msgid):
        return self.trans.get(msgid, str(msgid))

class EnglishGetter(object):

    def get(self, msgid):
        return str(msgid)

