import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

"""
Example:

session = BetterRequests.session()
response = session.get()
response = session.post()
"""
class BetterRequests:
    def __init__(self, *args, **kw):
        self._session = None
        self.last_error = None
        super().__init__(*args, **kw)

    def get(self, *args, **kwargs):
        try:
            return self._session.get(*args, **kwargs)
        except Exception as e:
            self.last_error = repr(e)
            return None

    def post(self, *args, **kwargs):
        try:
            return self._session.post(*args, **kwargs)
        except Exception as e:
            self.last_error = repr(e)
            return None

    def session(
        self,
        retries=3,
        backoff_factor=0.3,
        status_forcelist=(500, 502, 504),
        session=None,
        proxies = {},
        timeout = 10
    ):
        session = session or requests.Session()
        retry = Retry(
            total=retries,
            read=retries,
            connect=retries,
            backoff_factor=backoff_factor,
            status_forcelist=status_forcelist,
        )
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        session.proxies = proxies
        session.timeout = timeout
        self._session = session
        return True