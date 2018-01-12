import lang

def get_localizer(language='English'):
    languages = dict(
        English=lang.EnglishGetter,
        Greek=lang.GreekGetter
    )
    return languages[language]()


if __name__ == '__main__':
    e, g = get_localizer(language='English'), get_localizer(language='Greek')

    for msgid in 'cat dog parrot tiger'.split():
        print(e.get(msgid), g.get(msgid))

