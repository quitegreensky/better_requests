import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import os
import time

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
        return self.request("get", *args, **kwargs)

    def post(self, *args, **kwargs):
        return self.request("post", *args, **kwargs)

    def request(self, method,  *args, retry_sleep=1, retries=5, **kw):
        _tries = 0

        PREFIX = "BETTER_REQUESTS_"

        proxies = {}
        proxy_env = os.environ.get(f"{PREFIX}PROXY")
        proxies_kw = kw.get("proxies")
        kw.pop("proxies", None)
        if proxy_env:
            proxies = {
                "http": proxy_env,
                "https": proxy_env
            }
        if proxies_kw:
            proxies = proxies_kw

        timeout = 10
        timeout_env = os.environ.get(f"{PREFIX}TIMEOUT")
        timeout_kw = kw.get("timeout")
        kw.pop("timeout", None)
        if timeout_env:
            timeout = timeout_env
        if timeout_kw:
            timeout = timeout_kw

        retries_env = os.environ.get(f"{PREFIX}RETRIES")
        if retries_env:
            retries = retries_env
        while _tries < retries :
            try:
                response = requests.request(method, *args, timeout=timeout, proxies=proxies, **kw)
                return response
            except Exception as e:
                time.sleep(retry_sleep)
                _tries+=1
                continue
        return None