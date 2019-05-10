import aiohttp


class Translated(object):
    """Translate result object

    :param src: source langauge (default: auto)
    :param dest: destination language (default: en)
    :param origin: original text
    :param text: translated text
    :param pronunciation: pronunciation
    """
    def __init__(self, src, dest, origin, text, pronunciation, extra_data=None):
        self.src = src
        self.dest = dest
        self.origin = origin
        self.text = text
        self.pronunciation = pronunciation
        self.extra_data = extra_data

    def __str__(self):  # pragma: nocover
        return self.__unicode__()

    def __unicode__(self):  # pragma: nocover
        return u'Translated(src={src}, dest={dest}, text={text}, pronunciation={pronunciation}, ' \
               u'extra_data={extra_data})'.format(
            src=self.src, dest=self.dest, text=self.text, pronunciation=self.pronunciation,
            extra_data='"' + repr(self.extra_data)[:10] + '..."')


class Detected(object):
    """Language detection result object

    :param lang: detected language
    :param confidence: the confidence of detection result (0.00 to 1.00)
    """
    def __init__(self, lang, confidence):
        self.lang = lang
        self.confidence = confidence

    def __str__(self):  # pragma: nocover
        return self.__unicode__()

    def __unicode__(self):  # pragma: nocover
        return u'Detected(lang={lang}, confidence={confidence})'.format(
            lang=self.lang, confidence=self.confidence)


class TranslateSession:

    BASE_TIMEOUT = 10

    def __init__(self, proxy=None, headers=None, cookies=None, timeout=None):
        self.timeout = timeout
        self.cookies = cookies
        self.headers = headers
        if proxy is not None and 'http' in proxy:
            self.proxy = proxy['http']
        elif proxy is not None and 'http' in proxy:
            self.proxy = proxy['https']
        else:
            self.proxy = None
        self.session = None

    def _init_session(self):
        if self.timeout is not None:
            timeout = aiohttp.ClientTimeout(total=self.timeout)
        else:
            timeout = aiohttp.ClientTimeout(total=self.BASE_TIMEOUT)

        if self.headers is not None:
            headers = self.headers
        else:
            headers = {}

        if self.cookies is not None:
            cookies = self.cookies
        else:
            cookies = {}

        self.session = aiohttp.ClientSession(headers=headers, cookies=cookies, timeout=timeout)

    async def get(self, url: str) -> aiohttp.ClientResponse:
        if self.session is None:
            self._init_session()

        return await self.session.get(url=url)


