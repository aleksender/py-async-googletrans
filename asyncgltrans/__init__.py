"""Free Google Translate API for Python. Translates totally free of charge."""
__all__ = 'Translator',
__version__ = '0.0.18'


from asyncgltrans.client import Translator, AsyncTranslator
from asyncgltrans.constants import LANGCODES, LANGUAGES
