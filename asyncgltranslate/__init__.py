"""Free Google Translate API for Python. Translates totally free of charge."""
__all__ = 'Translator',
__version__ = '0.0.6'


from asyncgltranslate.client import Translator, AsyncTranslator
from asyncgltranslate.constants import LANGCODES, LANGUAGES
