import pytest

@pytest.fixture(name='lue')
def ultimate_anwser_to_life_the_universe_and_everytjing():
    return 42

def test_everything(lue):
    assert lue == 42




