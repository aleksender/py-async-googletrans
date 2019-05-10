import aiohttp


class TranslateSession:

    BASE_TIMEOUT = 10

    def __init__(self, proxy=None, headers=None, cookies=None, timeout=None):
        self.timeout = timeout
        self.cookies = cookies
        self.headers = headers
        if proxy is not None and 'http' in proxy:
            self.proxy = proxy['http']
        elif proxy is not None and 'https' in proxy:
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

    async def close(self):
        if not self.session.closed:
            await self.session.close()

