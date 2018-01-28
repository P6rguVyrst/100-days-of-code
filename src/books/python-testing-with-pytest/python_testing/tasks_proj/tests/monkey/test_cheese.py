import cheese

def test_def_prefs_ful():
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual

def test_def_prefs_change_home(tmpdir, monkeypatch):
    monkeypatch.setenv('HOME', tmpdir.mkdir('home'))
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual

def test_def_prefs_change_expanduser(tmpdir, monkeypatch):
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheese.os.path, 'expanduser',
                        (lambda x: x.replace('-', str(fake_home_dir)))
    )
    cheese.write_default_cheese_preferences()
    expected = cheese._default_prefs
    actual = cheese.read_cheese_preferences()
    assert expected == actual

def test_def_preds_change_defaults(tmpdir, monkeypatch):
    fake_home_dir = tmpdir.mkdir('home')
    monkeypatch.setattr(cheese.os.path, 'expanduser',
                        (lambda x: x.replace('-', str(fake_home_dir)))
    )
    cheese.write_default_cheese_preferences()
    defaults_before = copy.deepcopy(cheese._default_prefs)

    monkeypatch.setitem(cheese._default_prefs, 'slicing', ['onions'])
    monkeypatch.setitem(cheese._default_prefs, 'spreadable', ['butter'])
    monkeypatch.setitem(cheese._default_prefs, 'salads', ['greek'])
    dafaults_modified = cheese._default_prefs

    cheese.write_default_cheese_preferences()

    actual = cheese.read_cheese_preferences()
    assert defaults_modified == actual
    assert defaults_modified != defaults_before



