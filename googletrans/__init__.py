"""Free Google Translate API for Python. Translates totally free of charge."""
__all__ = 'Translator',
__version__ = '0.0.1'


from googletrans.client import Translator, AsyncTranslator
from googletrans.constants import LANGCODES, LANGUAGES
