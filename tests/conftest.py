from pytest import fixture


@fixture
def translator():
    from asyncgltrans import Translator
    return Translator()