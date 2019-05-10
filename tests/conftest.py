from pytest import fixture


@fixture
def translator():
    from asyncgltranslate import Translator
    return Translator()